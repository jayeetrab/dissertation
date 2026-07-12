# rag_pipeline.py
# ─────────────────────────────────────────────────────────────
# Core RAG logic. This module handles:
#   1. Loading the vector store from disk
#   2. Running the BASELINE system (LLM only, no retrieval)
#   3. Running the RAG system (retrieval + LLM)
#   4. Returning structured results for comparison
#
# This is the heart of your dissertation experiment.
# ─────────────────────────────────────────────────────────────

import uuid
from datetime import datetime, timezone
from typing import Optional

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage, SystemMessage

from config import (
    OPENAI_API_KEY, CHROMA_DIR, COLLECTION_NAME,
    EMBEDDING_MODEL, LLM_MODEL, TEMPERATURE, MAX_TOKENS, TOP_K,
    SYSTEM_PROMPT_BASELINE, SYSTEM_PROMPT_RAG,
    USER_PROMPT_BASELINE, USER_PROMPT_RAG
)
from models import TaskResult, RetrievedChunk
from spatial import extract_spatial_metadata, haversine_distance


# ── Singleton pattern for the vector store ────────────────────
# We load ChromaDB once when the server starts, not on every request.
# This saves ~2 seconds per request.
_vectorstore: Optional[Chroma] = None
_llm: Optional[ChatOpenAI] = None


def get_vectorstore() -> Chroma:
    """Load ChromaDB from disk (cached after first load)."""
    global _vectorstore
    if _vectorstore is None:
        print("Loading vector store from disk...")
        embeddings = OpenAIEmbeddings(
            model=EMBEDDING_MODEL,
            openai_api_key=OPENAI_API_KEY
        )
        _vectorstore = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=embeddings,
            persist_directory=str(CHROMA_DIR)
        )
        count = _vectorstore._collection.count()
        print(f"✓ Vector store loaded: {count} chunks available")
    return _vectorstore


def get_llm() -> ChatOpenAI:
    """Initialise the LLM (cached after first load)."""
    global _llm
    if _llm is None:
        _llm = ChatOpenAI(
            model=LLM_MODEL,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            openai_api_key=OPENAI_API_KEY
        )
        print(f"✓ LLM initialised: {LLM_MODEL} (temp={TEMPERATURE})")
    return _llm


def run_baseline(task_text: str) -> tuple[str, int]:
    """
    Run the BASELINE system: just the LLM, no retrieval.

    The LLM answers from its training data alone.
    This is what you're comparing RAG against.

    Returns:
        (output_text, tokens_used)
    """
    llm = get_llm()

    messages = [
        SystemMessage(content=SYSTEM_PROMPT_BASELINE),
        HumanMessage(content=USER_PROMPT_BASELINE.format(task=task_text))
    ]

    response = llm.invoke(messages)

    output = response.content
    # Token usage (for cost tracking)
    tokens = response.response_metadata.get("token_usage", {}).get("total_tokens", 0)

    return output, tokens

def _similarity_search_filtered(vs, query: str, k: int, corpus_filter: list = None,
                                city_filter: list = None):
    """
    Run similarity search with optional source_doc and/or city filter.
    Uses ChromaDB native client directly to avoid LangChain filter quirks.
    """
    # Get the embedding for the query
    embedding_fn = vs._embedding_function
    query_embedding = embedding_fn.embed_query(query)

    # Build where clause if filters provided
    clauses = []
    if corpus_filter and len(corpus_filter) > 0:
        if len(corpus_filter) == 1:
            clauses.append({"source_doc": {"$eq": corpus_filter[0]}})
        else:
            clauses.append({"source_doc": {"$in": list(corpus_filter)}})
    if city_filter and len(city_filter) > 0:
        if len(city_filter) == 1:
            clauses.append({"city": {"$eq": city_filter[0]}})
        else:
            clauses.append({"city": {"$in": list(city_filter)}})

    where = None
    if len(clauses) == 1:
        where = clauses[0]
    elif len(clauses) > 1:
        where = {"$and": clauses}

    # Query ChromaDB native collection directly
    collection = vs._collection
    query_kwargs = {
        "query_embeddings": [query_embedding],
        "n_results": k,
        "include": ["documents", "metadatas", "distances"],
    }
    if where:
        query_kwargs["where"] = where

    results = collection.query(**query_kwargs)

    # Reformat to match LangChain (doc, score) tuple format
    from langchain_core.documents import Document
    output = []
    docs = results["documents"][0]
    metas = results["metadatas"][0]
    distances = results["distances"][0]
    for doc_text, meta, dist in zip(docs, metas, distances):
        doc = Document(page_content=doc_text, metadata=meta)
        output.append((doc, dist))
    return output
def run_rag(task_text: str, corpus_filter: list = None,
            city_filter: list = None) -> tuple[str, int, list[RetrievedChunk]]:
    """
    Run the RAG system: retrieve relevant chunks, then generate answer.

    Steps:
    1. Convert task_text to a vector (embedding)
    2. Find TOP_K most similar chunks in ChromaDB
    3. Build a context string from those chunks
    4. Pass context + task to the LLM

    Returns:
        (output_text, tokens_used, retrieved_chunks)
    """
    vectorstore = get_vectorstore()
    llm = get_llm()

    # ── Step 1: Detect Spatial Context in Query ──────────────
    query_spatial = extract_spatial_metadata(task_text)
    has_spatial_query = query_spatial.lat is not None and query_spatial.lon is not None
    fetch_k = TOP_K * 4 if has_spatial_query else TOP_K
    
    if has_spatial_query:
        print(f"    📍 Spatial query detected: {query_spatial.location_name} ({query_spatial.lat}, {query_spatial.lon})")

    # ── Step 2: Retrieve relevant chunks (Over-fetch if spatial) ─
    # similarity_search_with_score returns (Document, score) pairs
    # Score is L2 distance — LOWER means MORE similar
    raw_results = _similarity_search_filtered(vectorstore, task_text, fetch_k,
                                              corpus_filter, city_filter)

    # ── Step 3: Spatial Re-ranking ────────────────────────────
    retrieved_chunks = []
    for doc, score in raw_results:
        similarity = round(1.0 / (1.0 + score), 4)
        
        c_lat = doc.metadata.get("lat")
        c_lon = doc.metadata.get("lon")
        
        distance_km = None
        spatial_boost = 0.0
        
        # Calculate distance and boost if both query and chunk have coordinates
        if has_spatial_query and c_lat is not None and c_lon is not None:
            distance_km = round(haversine_distance(query_spatial.lat, query_spatial.lon, c_lat, c_lon), 2)
            
            # Boost chunks that are very close (within 10km gets up to +0.15 similarity)
            # This pushes geographically relevant but less semantically matched chunks higher
            if distance_km <= 15:
                spatial_boost = max(0, 0.15 * (1 - (distance_km / 15)))
                
        final_score = similarity + spatial_boost
        
        chunk = RetrievedChunk(
            content=doc.page_content,
            source_doc=doc.metadata.get("source_doc", "unknown"),
            page_number=doc.metadata.get("page_number", 0),
            relevance_score=round(final_score, 4),
            city=doc.metadata.get("city"),
            lat=c_lat,
            lon=c_lon,
            distance_km=distance_km
        )
        retrieved_chunks.append(chunk)

    # Sort descending by the final re-ranked score and take TOP_K
    retrieved_chunks.sort(key=lambda x: x.relevance_score, reverse=True)
    retrieved_chunks = retrieved_chunks[:TOP_K]

    # ── Step 4: Build context string ──────────────────────────
    # Format retrieved chunks clearly so the LLM can follow them
    context_parts = []
    for i, chunk in enumerate(retrieved_chunks, 1):
        dist_str = f", Distance: {chunk.distance_km}km" if chunk.distance_km is not None else ""
        context_parts.append(
            f"[Extract {i} — Source: {chunk.source_doc}, Page {chunk.page_number}{dist_str}]\n"
            f"{chunk.content}"
        )
    context = "\n\n---\n\n".join(context_parts)

    # ── Step 5: Generate answer with context ──────────────────
    messages = [
        SystemMessage(content=SYSTEM_PROMPT_RAG),
        HumanMessage(content=USER_PROMPT_RAG.format(
            context=context,
            task=task_text
        ))
    ]

    response = llm.invoke(messages)

    output = response.content
    tokens = response.response_metadata.get("token_usage", {}).get("total_tokens", 0)

    return output, tokens, retrieved_chunks


def run_task(task_id: str, task_text: str, task_category: str,
             run_baseline_flag: bool = True, run_rag_flag: bool = True,
             corpus_filter: list = None, city: str = None,
             city_filter: list = None) -> TaskResult:
    """
    Run a single task through one or both systems and return a TaskResult.

    `city` records which city the task targets (for per-city analysis).
    `city_filter` optionally restricts retrieval to given cities — leave
    None for the default cross-city condition, where retrieving another
    city's policy counts as spatial misattribution.

    This is the main function called by the API endpoints.
    """
    result = TaskResult(
        result_id=str(uuid.uuid4()),
        task_id=task_id,
        task_text=task_text,
        category=task_category,
        city=city or "bristol",
        timestamp=datetime.now(timezone.utc).isoformat()
    )

    # ── Run Baseline ──────────────────────────────────────────
    if run_baseline_flag:
        print(f"  → Running BASELINE for {task_id}...")
        try:
            output, tokens = run_baseline(task_text)
            result.baseline_output = output
            result.baseline_tokens_used = tokens
            print(f"    ✓ Baseline done ({tokens} tokens)")
        except Exception as e:
            result.baseline_output = f"[ERROR: {str(e)}]"
            print(f"    ✗ Baseline failed: {e}")

    # ── Run RAG ───────────────────────────────────────────────
    if run_rag_flag:
        print(f"  → Running RAG for {task_id}...")
        try:
            output, tokens, chunks = run_rag(task_text, corpus_filter=corpus_filter,
                                             city_filter=city_filter)
            result.rag_output = output
            result.rag_tokens_used = tokens
            result.retrieved_chunks = chunks
            print(f"    ✓ RAG done ({tokens} tokens, {len(chunks)} chunks retrieved)")
        except Exception as e:
            result.rag_output = f"[ERROR: {str(e)}]"
            print(f"    ✗ RAG failed: {e}")

    return result


def check_vectorstore_ready() -> dict:
    """Health check — is the vector store loaded and has data?"""
    try:
        vs = get_vectorstore()
        count = vs._collection.count()
        return {
            "ready": count > 0,
            "chunk_count": count,
            "message": f"Vector store ready with {count} chunks" if count > 0
                       else "Vector store is empty — run ingest.py first"
        }
    except Exception as e:
        return {
            "ready": False,
            "chunk_count": 0,
            "message": f"Vector store not available: {str(e)}"
        }
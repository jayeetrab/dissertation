# ingest.py
# ─────────────────────────────────────────────────────────────
# Run this script ONCE to load your planning PDFs into ChromaDB.
# After running, the vector database persists to disk — you don't
# need to re-run unless you add new documents.
#
# Usage:
#   python ingest.py
#   python ingest.py --reset    (clears existing DB and re-ingests everything)
#   python ingest.py --dry-run  (shows what would happen without doing it)
# ─────────────────────────────────────────────────────────────

import sys
import argparse
import time
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import chromadb

from spatial import CITY_CENTROIDS

# Import our config (all settings in one place)
from config import (
    OPENAI_API_KEY, DOCS_DIR, CHROMA_DIR,
    CHUNK_SIZE, CHUNK_OVERLAP,
    EMBEDDING_MODEL, COLLECTION_NAME
)


def city_for_pdf(pdf_path: Path, docs_dir: Path) -> str:
    """
    Derive the city tag from the PDF's subfolder within docs/.
    docs/bristol/Core_Strategy.pdf  -> "bristol"
    docs/national/NPPF_....pdf      -> "national"
    docs/loose_file.pdf             -> "national" (top-level = national policy)
    """
    rel = pdf_path.relative_to(docs_dir)
    return rel.parts[0].lower() if len(rel.parts) > 1 else "national"


def load_documents(docs_dir: Path, city_filter: str = None) -> list:
    """
    Load all PDFs from docs/ and its per-city subfolders.
    Every page is tagged with a `city` metadata field derived from its
    subfolder, so chunks can be filtered/analysed per city later.
    Returns a list of LangChain Document objects (one per page).
    """
    pdf_files = sorted(docs_dir.rglob("*.pdf"))
    if city_filter:
        pdf_files = [f for f in pdf_files
                     if city_for_pdf(f, docs_dir) == city_filter.lower()]

    if not pdf_files:
        print(f"\n❌ No PDFs found in {docs_dir}"
              + (f" for city '{city_filter}'" if city_filter else ""))
        print("   Add planning documents to docs/<city>/ subfolders "
              "(national policy like the NPPF goes in docs/national/)")
        sys.exit(1)

    print(f"\n📄 Found {len(pdf_files)} PDF(s) in {docs_dir}:")
    for f in pdf_files:
        size_mb = f.stat().st_size / 1_000_000
        print(f"   - [{city_for_pdf(f, docs_dir)}] {f.name} ({size_mb:.1f} MB)")

    all_docs = []
    for pdf_path in pdf_files:
        city = city_for_pdf(pdf_path, docs_dir)
        print(f"\n   Loading: {pdf_path.name} (city: {city})...")
        try:
            loader = PyPDFLoader(str(pdf_path))
            pages = loader.load()

            # Enrich metadata on every page so we know where each chunk came from
            for page in pages:
                page.metadata["source_doc"] = pdf_path.name
                page.metadata["source_path"] = str(pdf_path)
                page.metadata["city"] = city
                # page.metadata["page"] is already set by PyPDFLoader (0-indexed)
                # We convert to 1-indexed for human readability
                page.metadata["page_number"] = page.metadata.get("page", 0) + 1

            all_docs.extend(pages)
            print(f"   ✓ Loaded {len(pages)} pages")

        except Exception as e:
            print(f"   ⚠ Failed to load {pdf_path.name}: {e}")
            print("     (Skipping this file and continuing)")

    print(f"\n✓ Total pages loaded: {len(all_docs)}")
    return all_docs


def chunk_documents(documents: list) -> list:
    """
    Split documents into overlapping chunks for vector storage.

    RecursiveCharacterTextSplitter tries to split at natural boundaries:
    1. First tries to split at paragraph breaks (\\n\\n)
    2. Then at sentence breaks (\\n)
    3. Then at word boundaries (space)
    4. Only as last resort splits mid-word

    This is smarter than a fixed-size splitter that just cuts every 500 chars.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""],
        # The order matters — tries each separator in order
    )

    chunks = splitter.split_documents(documents)

    # Filter out chunks that are too short to be useful
    # (often headers, page numbers, or blank pages)
    min_chunk_length = 50  # characters
    chunks = [c for c in chunks if len(c.page_content.strip()) > min_chunk_length]

    print(f"\n📦 Chunking complete:")
    print(f"   Input: {len(documents)} pages")
    print(f"   Output: {len(chunks)} chunks")
    print(f"   Avg chunk size: {sum(len(c.page_content) for c in chunks) // len(chunks)} chars")

    # Show a sample chunk so you can verify it looks right
    print(f"\n   Sample chunk (chunk #10):")
    if len(chunks) > 10:
        sample = chunks[10]
        print(f"   Source: {sample.metadata.get('source_doc')} p.{sample.metadata.get('page_number')}")
        print(f"   Text: {sample.page_content[:200]}...")

    return chunks


def build_vector_store(chunks: list, reset: bool = False) -> Chroma:
    """
    Create embeddings for all chunks and store them in ChromaDB.

    Embeddings are numerical representations of text meaning.
    Two pieces of text with similar meaning will have similar embeddings (vectors).
    ChromaDB stores these vectors and can find the most similar ones quickly.

    This is the most expensive step — it calls the OpenAI Embeddings API once per chunk.
    Cost: ~$0.00002 per 1000 characters. For 200 pages: ~$0.10 total.
    """
    CHROMA_DIR.mkdir(parents=True, exist_ok=True)

    # If reset flag: delete the existing collection first
    if reset:
        print("\n🗑  Resetting existing vector database...")
        try:
            client = chromadb.PersistentClient(path=str(CHROMA_DIR))
            client.delete_collection(COLLECTION_NAME)
            print("   ✓ Existing collection deleted")
        except Exception:
            print("   (No existing collection found — starting fresh)")

    print(f"\n🔢 Creating embeddings and assigning spatial metadata...")
    print(f"   Model: {EMBEDDING_MODEL}")
    print(f"   Chunks to process: {len(chunks)}")
    print(f"   Estimated cost: ~${len(chunks) * 0.00002:.4f} (embeddings only)")

    start_time = time.time()

    # --- Phase 1: Spatial Metadata (deterministic, no API calls) ---
    # Each chunk's city is known from its docs/ subfolder, so we assign
    # the city centroid directly. Reproducible and free; the LLM-based
    # extraction is only used at query time (see rag_pipeline.py).
    print("   -> Assigning city centroid coordinates...")
    tagged = 0
    for chunk in chunks:
        coords = CITY_CENTROIDS.get(chunk.metadata.get("city"))
        if coords:
            chunk.metadata["lat"] = coords[0]
            chunk.metadata["lon"] = coords[1]
            chunk.metadata["location_name"] = chunk.metadata["city"].capitalize()
            tagged += 1
    print(f"      {tagged}/{len(chunks)} chunks tagged (national policy chunks are location-free)")

    # --- Phase 2: Vector Embedding & Storage ---
    print("   -> Generating semantic embeddings and saving to ChromaDB...")
    embeddings = OpenAIEmbeddings(
        model=EMBEDDING_MODEL,
        openai_api_key=OPENAI_API_KEY
    )

    # Chroma.from_documents does three things:
    # 1. Calls the OpenAI Embeddings API for each chunk (the slow, costly part)
    # 2. Stores the vectors in ChromaDB on disk (at CHROMA_DIR)
    # 3. Returns the Chroma object you can query later
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=str(CHROMA_DIR)
    )

    elapsed = time.time() - start_time
    stored_count = vectorstore._collection.count()

    # Per-city breakdown so we can verify each city actually made it in
    try:
        metas = vectorstore._collection.get(include=["metadatas"])["metadatas"]
        from collections import Counter
        city_counts = Counter(m.get("city", "untagged") for m in metas)
        print(f"\n   Chunks per city:")
        for city, n in sorted(city_counts.items()):
            print(f"     {city}: {n}")
    except Exception as e:
        print(f"   (Could not compute per-city counts: {e})")

    print(f"✓ Vector database built successfully!")
    print(f"   Chunks stored: {stored_count}")
    print(f"   Time taken: {elapsed:.1f} seconds")
    print(f"   Database saved to: {CHROMA_DIR}")

    return vectorstore


def verify_retrieval(vectorstore: Chroma) -> None:
    """
    Quick sanity check — run a test query to make sure retrieval works.
    If this returns relevant chunks, your system is working correctly.
    """
    print("\n🔍 Verification — running a test query...")
    test_query = "What is the definition of grey belt land?"

    results = vectorstore.similarity_search_with_score(test_query, k=3)

    print(f"   Query: '{test_query}'")
    print(f"   Retrieved {len(results)} chunks:\n")

    for i, (doc, score) in enumerate(results, 1):
        print(f"   [{i}] Score: {score:.4f} (lower = more similar in L2 distance)")
        print(f"       Source: {doc.metadata.get('source_doc')} p.{doc.metadata.get('page_number')}")
        print(f"       Text: {doc.page_content[:150]}...")
        print()

    if results:
        print("✅ Retrieval working correctly. System is ready.")
    else:
        print("⚠ No results returned. Check your documents contain relevant text.")


def main():
    parser = argparse.ArgumentParser(description="Ingest planning documents into ChromaDB")
    parser.add_argument("--reset", action="store_true",
                        help="Delete existing vector DB and re-ingest from scratch")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would happen without actually doing it")
    parser.add_argument("--city", type=str, default=None,
                        help="Only ingest docs/<city>/ (adds to the existing collection "
                             "— lets you ingest one city at a time)")
    args = parser.parse_args()

    if args.reset and args.city:
        print("❌ --reset with --city would wipe ALL cities then ingest only one. "
              "Run --reset alone, or --city alone to add incrementally.")
        sys.exit(1)

    print("=" * 60)
    print("  PlanningRAG — Document Ingestion")
    print("=" * 60)

    if args.dry_run:
        print("\n⚠ DRY RUN MODE — no files will be written\n")

    # Step 1: Load PDFs
    documents = load_documents(DOCS_DIR, city_filter=args.city)

    # Step 2: Split into chunks
    chunks = chunk_documents(documents)

    if args.dry_run:
        print("\n✓ Dry run complete. No data was written.")
        print(f"  Would have embedded {len(chunks)} chunks into ChromaDB.")
        return

    # Step 3: Build vector store
    vectorstore = build_vector_store(chunks, reset=args.reset)

    # Step 4: Verify it works
    verify_retrieval(vectorstore)

    print("\n" + "=" * 60)
    print("  Ingestion complete! Next step:")
    print("  Run: uvicorn main:app --reload --port 8000")
    print("=" * 60)


if __name__ == "__main__":
    main()
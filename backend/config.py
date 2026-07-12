# config.py
# ─────────────────────────────────────────────────────────────
# ALL configuration lives here. Change values here, not in other files.
# This is good practice — one place to tune your experiment.
# ─────────────────────────────────────────────────────────────

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # reads .env file and loads variables into os.environ

# ── Paths ─────────────────────────────────────────────────────
# Path() makes paths work on Windows, Mac, and Linux equally
BASE_DIR    = Path(__file__).parent.parent  # the planning-rag/ root folder
DOCS_DIR    = BASE_DIR / "docs"             # where you put your PDFs
CHROMA_DIR  = BASE_DIR / "chroma_db"       # where ChromaDB stores the vector index
TASKS_FILE  = BASE_DIR / "frontend" / "tasks" / "tasks.json"
RESULTS_DIR = BASE_DIR / "results"
# ── OpenAI API ────────────────────────────────────────────────
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY not found. "
        "Create a .env file with: OPENAI_API_KEY=sk-..."
    )

# ── Model Settings ────────────────────────────────────────────
# The LLM used for generating answers
LLM_MODEL = "gpt-4o-mini"
# Why gpt-4o-mini? Fast, cheap (~£0.0002/call), capable enough for planning tasks.
# For higher quality (and 10x cost), change to "gpt-4o"

TEMPERATURE = 0.0
# Temperature controls randomness.
# 0.0 = fully deterministic (same input → same output every time)
# 1.0 = highly random/creative
# For research/evaluation: ALWAYS use 0.0 so results are reproducible.

MAX_TOKENS = 1500
# Maximum length of each LLM response.
# 1500 tokens ≈ ~1100 words. Enough for a detailed planning answer.
# Increase to 2000 if answers feel cut off.

# ── Embedding Settings ────────────────────────────────────────
EMBEDDING_MODEL = "text-embedding-3-small"
# Converts text into numerical vectors for semantic search.
# text-embedding-3-small: 1536 dimensions, cheap, excellent quality
# text-embedding-3-large: 3072 dimensions, 5x more expensive, marginal improvement
# For this project: small is the right choice.

# ── Chunking Settings ─────────────────────────────────────────
CHUNK_SIZE = 500
# How many characters per chunk (NOT tokens — characters).
# 500 chars ≈ 80-120 words ≈ 2-3 short paragraphs.
# Too small (< 200): chunks lose context, retrieval is less meaningful
# Too large (> 1000): chunks contain multiple topics, retrieval is less precise
# 500 is the standard sweet spot for policy documents.

CHUNK_OVERLAP = 100
# How many characters the next chunk shares with the previous one.
# This prevents sentences from being cut at chunk boundaries.
# Example: "The grey belt policy requires [chunk break] all developers to..."
# With overlap: the second chunk starts mid-previous chunk so "requires" stays connected.
# Rule of thumb: overlap = CHUNK_SIZE * 0.15 to 0.20

# ── Retrieval Settings ────────────────────────────────────────
TOP_K = 8
# How many chunks to retrieve per query.
# These become the "context" injected into the RAG prompt.
# Too few (1-2): might miss relevant paragraphs
# Too many (10+): prompt becomes huge, LLM gets confused, cost increases
# 5 is the standard. For complex multi-part tasks, try 7.

SEARCH_TYPE = "similarity"
# How ChromaDB finds relevant chunks.
# "similarity": pure cosine similarity — finds most semantically similar chunks
# "mmr": Maximum Marginal Relevance — finds diverse chunks, avoids repetition
# For planning docs where policies repeat: "mmr" can help. Try both.

# ── ChromaDB Settings ─────────────────────────────────────────
COLLECTION_NAME = "planning_docs"
# The name of your vector database collection.
# Like a table name in SQL. Keep consistent across ingest.py and main.py.

# ── Experiment Settings ───────────────────────────────────────
N_RUNS = 3
# How many times to run each task for consistency testing.
# With temperature=0, all 3 runs will be identical — that's fine.
# Change temperature to 0.3 and N_RUNS to 3 to measure output variance.
# For your dissertation: run with temperature=0, N_RUNS=1 for efficiency.

# ── Task Categories ───────────────────────────────────────────
TASK_CATEGORIES = [
    "policy_compliance",      # PC — does X comply with policy Y?
    "evidence_synthesis",     # ES — summarise / compare documents
    "site_appraisal",        # SA — assess site suitability
    "stakeholder_communication",  # SC — plain English summaries
    "strategic_analysis",    # ST — compare strategies, policy evolution
]

# ── Hallucination Types ───────────────────────────────────────
# Your original taxonomy — used in the evaluation UI
HALLUCINATION_TYPES = [
    "fabricated_clause",      # Invented policy paragraph that doesn't exist
    "outdated_policy",        # Applied an older version of the policy
    "spatial_misattribution", # Wrong geographic policy applied
    "confident_ambiguity",    # Gave a definitive answer where policy is vague
    "none",                   # No hallucination detected
]

# ── Prompts ───────────────────────────────────────────────────
# These are the exact instructions given to the LLM.
# Stored here so they're easy to find, version, and tweak.

SYSTEM_PROMPT_BASELINE = """You are an expert urban planning assistant with deep knowledge of UK planning policy, including the National Planning Policy Framework (NPPF), Planning Practice Guidance (PPG), and local planning documents.

Answer the planning task accurately and professionally. Where relevant, cite specific policy references."""

SYSTEM_PROMPT_RAG = """You are an expert urban planning assistant. Answer planning tasks using the official planning documents provided in the context below, supplemented where necessary by your expert knowledge of UK planning policy.

RULES:
1. Prioritise information from the provided context passages — cite them specifically (e.g., "NPPF paragraph 155", "Core Strategy Policy BCS17").
2. Where the context provides relevant but partial information, use it AND supplement with your planning expertise — clearly label what comes from the documents vs. your knowledge.
3. Only say documents are insufficient if the context contains NO relevant planning information whatsoever.
4. If policies conflict between documents, flag the conflict explicitly.
5. Always give a substantive, professional planning answer — never refuse to answer if you have any relevant knowledge."""

USER_PROMPT_BASELINE = """Planning Task: {task}

Please provide a thorough, professional answer as an experienced UK planning consultant would."""

USER_PROMPT_RAG = """The following are extracts from official UK planning documents relevant to this task:

--- PLANNING DOCUMENT CONTEXT ---
{context}
--- END OF CONTEXT ---

Planning Task: {task}

Using ONLY the above context, provide a thorough professional answer. Cite specific paragraphs where applicable."""
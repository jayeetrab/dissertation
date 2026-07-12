# models.py
# ─────────────────────────────────────────────────────────────
# Pydantic models define the exact shape of data flowing through the API.
# FastAPI uses these to:
#   1. Validate incoming requests (wrong types = automatic 422 error)
#   2. Serialize outgoing responses to JSON
#   3. Auto-generate the /docs API documentation
# ─────────────────────────────────────────────────────────────

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum


# ── Enums ─────────────────────────────────────────────────────
# Enums restrict a field to a fixed set of valid values.
# FastAPI validates these automatically — typos cause 422 errors, not silent bugs.

class TaskCategory(str, Enum):
    policy_compliance          = "policy_compliance"
    evidence_synthesis         = "evidence_synthesis"
    site_appraisal             = "site_appraisal"
    stakeholder_communication  = "stakeholder_communication"
    strategic_analysis         = "strategic_analysis"

class HallucinationType(str, Enum):
    fabricated_clause      = "fabricated_clause"
    outdated_policy        = "outdated_policy"
    spatial_misattribution = "spatial_misattribution"
    confident_ambiguity    = "confident_ambiguity"
    none                   = "none"

class SystemType(str, Enum):
    baseline = "baseline"
    rag      = "rag"


# ── Task Models ───────────────────────────────────────────────

class Task(BaseModel):
    """A single planning task from tasks.json"""
    id: str                         # e.g. "PC-01" or "MAN-PC-01"
    category: TaskCategory          # must be one of the 5 categories
    task: str                       # the actual question/task text
    city: Optional[str] = "bristol" # which city's local plan the task targets
    expected_source: Optional[str] = None   # which document should answer this?
    expected_paragraphs: Optional[List[str]] = []  # e.g. ["para 155", "Annex 2"]
    difficulty: Optional[str] = "medium"           # easy / medium / hard
    notes: Optional[str] = None     # any notes about the task


# ── Request Models (what the frontend sends TO the backend) ───

class RunTaskRequest(BaseModel):
    task_id: str
    run_baseline: bool = True
    run_rag: bool = True
    corpus_filter: Optional[List[str]] = None
    # Restrict retrieval to these cities (e.g. ["london", "national"]).
    # None = cross-city retrieval (the default experimental condition).
    city_filter: Optional[List[str]] = None

class RunAllTasksRequest(BaseModel):
    """Request to run all tasks (or a filtered subset)"""
    category_filter: Optional[TaskCategory] = None  # None = run all categories
    city_filter: Optional[str] = None               # None = tasks for all cities
    run_baseline: bool = True
    run_rag: bool = True

class ScoreSubmission(BaseModel):
    """Manual score submitted by the researcher for one output"""
    result_id: str              # which result is being scored
    system: SystemType          # "baseline" or "rag"

    # Quantitative scores (1-5 scale)
    accuracy: int = Field(..., ge=1, le=5,
        description="1=completely wrong, 5=fully accurate per source documents")
    completeness: int = Field(..., ge=1, le=5,
        description="1=missing most elements, 5=addresses all parts of task")
    planning_usefulness: int = Field(..., ge=1, le=5,
        description="1=useless to a planner, 5=immediately useful")

    # Grounding score (0-2 scale)
    grounding: int = Field(..., ge=0, le=2,
        description="0=no source cited, 1=vague reference, 2=specific paragraph cited")

    # Hallucination
    hallucination_present: bool = False
    hallucination_type: HallucinationType = HallucinationType.none
    hallucination_detail: Optional[str] = None  # exact quote of the hallucination

    # Free text
    scorer_notes: Optional[str] = None


class AutoScore(BaseModel):
    """
    Automated rubric score produced by the LLM-as-judge (backend/auto_score.py).
    Mirrors the manual rubric fields so the two tracks can be compared directly,
    but is kept in SEPARATE fields from the human ScoreSubmission so a manual
    validation subset stays independent (never overwritten by the judge).
    """
    system: SystemType
    accuracy: int = Field(..., ge=1, le=5)
    completeness: int = Field(..., ge=1, le=5)
    planning_usefulness: int = Field(..., ge=1, le=5)
    grounding: int = Field(..., ge=0, le=2)
    hallucination_present: bool = False
    hallucination_type: HallucinationType = HallucinationType.none
    hallucination_detail: Optional[str] = None
    judge_model: Optional[str] = None      # which model produced this score
    judge_rationale: Optional[str] = None  # one-line justification (auditable)


# ── Response Models (what the backend sends BACK to the frontend) ─

class RetrievedChunk(BaseModel):
    """A single chunk retrieved from ChromaDB"""
    content: str
    source_doc: str     # filename of the PDF
    page_number: int
    relevance_score: float  # cosine similarity score (0-1, higher = more relevant)
    city: Optional[str] = None  # which city's corpus this chunk came from

    # Spatial metadata
    lat: Optional[float] = None
    lon: Optional[float] = None
    distance_km: Optional[float] = None

class TaskResult(BaseModel):
    """The result of running one task through one or both systems"""
    result_id: str
    task_id: str
    task_text: str
    category: TaskCategory
    city: Optional[str] = "bristol"  # which city the task targets
    timestamp: str

    # Baseline output
    baseline_output: Optional[str] = None
    baseline_tokens_used: Optional[int] = None

    # RAG output
    rag_output: Optional[str] = None
    rag_tokens_used: Optional[int] = None
    retrieved_chunks: Optional[List[RetrievedChunk]] = []

    # Automated metrics (from RAGAS, filled after evaluation)
    ragas_faithfulness: Optional[float] = None      # 0-1: does answer stick to context?
    ragas_answer_relevancy: Optional[float] = None  # 0-1: does answer address question?
    ragas_context_precision: Optional[float] = None # 0-1: were right chunks retrieved?

    # Manual scores (filled after human evaluation)
    baseline_scores: Optional[ScoreSubmission] = None
    rag_scores: Optional[ScoreSubmission] = None

    # Automated LLM-as-judge rubric scores (backend/auto_score.py) — kept
    # separate from the manual scores above so a human validation subset
    # remains an independent check on the judge.
    baseline_auto_scores: Optional[AutoScore] = None
    rag_auto_scores: Optional[AutoScore] = None

class IngestStatus(BaseModel):
    """Status of the document ingestion process"""
    success: bool
    documents_loaded: int
    chunks_created: int
    chunks_stored: int
    documents_list: List[str]
    message: str

class SystemStats(BaseModel):
    """Overall stats for the dashboard"""
    total_tasks: int
    tasks_run: int
    tasks_scored: int
    tasks_auto_scored: int = 0
    avg_baseline_accuracy: Optional[float]
    avg_rag_accuracy: Optional[float]
    hallucination_rate_baseline: Optional[float]
    hallucination_rate_rag: Optional[float]
    docs_in_corpus: int
    chunks_in_db: int
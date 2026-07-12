# main.py
# ─────────────────────────────────────────────────────────────
# FastAPI application — all HTTP endpoints.
#
# Run with: uvicorn main:app --reload --port 8000
#
# API Explorer: http://localhost:8000/docs  (auto-generated!)
# ─────────────────────────────────────────────────────────────

import json
from pathlib import Path
from typing import List, Optional
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from config import TASKS_FILE, RESULTS_DIR, CHROMA_DIR, DOCS_DIR
from models import (
    Task, TaskResult, RunTaskRequest, RunAllTasksRequest,
    ScoreSubmission, IngestStatus, SystemStats
)
from rag_pipeline import run_task, check_vectorstore_ready
from evaluator import evaluate_with_ragas, export_to_csv, compute_summary_stats
from progress import batch_progress


# ── App Setup ─────────────────────────────────────────────────
app = FastAPI(
    title="PlanningRAG API",
    description="""
    Urban Planning LLM Evaluation System
    MSc Dissertation — Jayeetra Bhattacharjee, University of Bristol

    Endpoints for running planning tasks through baseline and RAG systems,
    scoring results, and exporting data for dissertation analysis.
    """,
    version="1.0.0"
)

# CORS — allows the frontend (running on localhost:5173) to call this API
# In production, replace "*" with your actual frontend domain
import os
_raw_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://localhost:3000")
_allowed_origins = [o.strip() for o in _raw_origins.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── In-memory store ───────────────────────────────────────────
# Results are stored in memory during the session.
# They're also persisted to disk as JSON for recovery.
# For a real production app, you'd use a database (SQLite, Postgres).
results_store: dict[str, TaskResult] = {}
_RESULTS_JSON = RESULTS_DIR / "results_store.json"


def save_results_to_disk():
    """Persist results to disk so they survive server restarts."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    data = {rid: result.model_dump() for rid, result in results_store.items()}
    with open(_RESULTS_JSON, "w") as f:
        json.dump(data, f, indent=2, default=str)


def load_results_from_disk():
    """Load previously saved results on server startup."""
    global results_store
    if _RESULTS_JSON.exists():
        with open(_RESULTS_JSON) as f:
            data = json.load(f)
        # Key by task_id, not the on-disk key. Historic runs saved each task
        # under both a task_id and a UUID key; loading by task_id collapses
        # those duplicates so the store self-heals to one record per task on
        # every restart. Prefer an entry that already carries manual scores.
        for result_dict in data.values():
            try:
                r = TaskResult(**result_dict)
            except Exception:
                continue  # skip malformed entries
            existing = results_store.get(r.task_id)
            if existing and (existing.baseline_scores or existing.rag_scores) \
                    and not (r.baseline_scores or r.rag_scores):
                continue
            results_store[r.task_id] = r
        print(f"✓ Loaded {len(results_store)} results from disk")


# ── Startup ───────────────────────────────────────────────────
@app.on_event("startup")
async def startup():
    """Called once when the server starts."""
    print("\n" + "=" * 50)
    print("  PlanningRAG Server Starting")
    print("=" * 50)
    load_results_from_disk()
    status = check_vectorstore_ready()
    print(f"Vector store: {status['message']}")
    print(f"API docs at:  http://localhost:8000/docs")
    print("=" * 50 + "\n")


# ══════════════════════════════════════════════════════════════
# HEALTH & STATUS ENDPOINTS
# ══════════════════════════════════════════════════════════════

@app.get("/", tags=["Status"])
def root():
    """Root endpoint — confirms API is running."""
    return {"status": "running", "app": "PlanningRAG", "version": "1.0.0"}


@app.get("/health", tags=["Status"])
def health_check():
    """Full health check including vector store status."""
    vs_status = check_vectorstore_ready()
    tasks_loaded = len(load_tasks())
    return {
        "api": "ok",
        "vectorstore": vs_status,
        "tasks_loaded": tasks_loaded,
        "results_in_memory": len(results_store),
    }


@app.get("/stats", response_model=SystemStats, tags=["Status"])
def get_stats():
    """Summary statistics for the dashboard."""
    results_list = list(results_store.values())
    computed = compute_summary_stats(results_list)
    vs_status = check_vectorstore_ready()

    # Count unique docs in the corpus (including per-city subfolders)
    docs_count = len(list(DOCS_DIR.rglob("*.pdf"))) if DOCS_DIR.exists() else 0

    return SystemStats(
        total_tasks=len(load_tasks()),
        tasks_run=computed.get("tasks_with_results", 0),
        tasks_scored=computed.get("tasks_scored", 0),
        tasks_auto_scored=computed.get("tasks_auto_scored", 0),
        avg_baseline_accuracy=computed.get("avg_baseline_accuracy"),
        avg_rag_accuracy=computed.get("avg_rag_accuracy"),
        hallucination_rate_baseline=computed.get("hallucination_rate_baseline"),
        hallucination_rate_rag=computed.get("hallucination_rate_rag"),
        docs_in_corpus=docs_count,
        chunks_in_db=vs_status.get("chunk_count", 0),
    )


# ══════════════════════════════════════════════════════════════
# TASK ENDPOINTS
# ══════════════════════════════════════════════════════════════

def load_tasks() -> List[Task]:
    """Load tasks from tasks.json."""
    if not TASKS_FILE.exists():
        return []
    with open(TASKS_FILE) as f:
        raw = json.load(f)
    return [Task(**t) for t in raw]


@app.get("/tasks", response_model=List[Task], tags=["Tasks"])
def get_tasks(category: Optional[str] = None, city: Optional[str] = None):
    """
    Get all planning tasks.
    Optionally filter by category (e.g. ?category=policy_compliance)
    and/or city (e.g. ?city=london)
    """
    tasks = load_tasks()
    if category:
        tasks = [t for t in tasks if t.category == category]
    if city:
        tasks = [t for t in tasks if (t.city or "bristol") == city.lower()]
    return tasks


@app.get("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def get_task(task_id: str):
    """Get a single task by ID (e.g. PC-01)."""
    tasks = {t.id: t for t in load_tasks()}
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return tasks[task_id]


# ══════════════════════════════════════════════════════════════
# EXPERIMENT ENDPOINTS
# ══════════════════════════════════════════════════════════════

@app.post("/run/task", response_model=TaskResult, tags=["Experiment"])
def run_single_task(req: RunTaskRequest):
    """
    Run a single task through baseline and/or RAG system.

    This is the core experiment endpoint.
    Returns both outputs for immediate comparison.

    Cost: ~£0.001-0.002 per call (gpt-4o-mini)
    Time: ~5-15 seconds
    """
    tasks = {t.id: t for t in load_tasks()}
    if req.task_id not in tasks:
        raise HTTPException(status_code=404, detail=f"Task {req.task_id} not found")

    task = tasks[req.task_id]
    print(f"\nRunning task: {task.id} — {task.task[:60]}...")

    result = run_task(
        task_id=task.id,
        task_text=task.task,
        task_category=task.category,
        run_baseline_flag=req.run_baseline,
        run_rag_flag=req.run_rag,
        corpus_filter=req.corpus_filter,
        city=task.city,
        city_filter=req.city_filter,
    )

    # Source-ablation / what-if runs (where a corpus or city filter is applied)
    # are exploratory, not the canonical experimental condition. They must not
    # overwrite the task's real record or pollute GET /results (which feeds the
    # Evaluate/Dashboard views), so they are returned to the caller without
    # being persisted. The Compare page renders the returned result directly.
    is_ablation = bool(req.corpus_filter or req.city_filter)
    if not is_ablation:
        results_store[result.task_id] = result
        save_results_to_disk()

    return result


@app.post("/run/all", tags=["Experiment"])
def run_all_tasks(req: RunAllTasksRequest, background_tasks: BackgroundTasks):
    """
    Run ALL tasks (or a category subset) in the background.

    Returns immediately with a job ID.
    Check /results to see results as they come in.

    WARNING: Runs all 40 tasks × 2 systems = 80 API calls.
    Cost: ~£2-5. Time: ~10-20 minutes.
    """
    tasks = load_tasks()
    if req.category_filter:
        tasks = [t for t in tasks if t.category == req.category_filter]
    if req.city_filter:
        tasks = [t for t in tasks if (t.city or "bristol") == req.city_filter.lower()]

    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found matching filter")

    def run_background():
        batch_progress.start(len(tasks))
        print(f"Starting batch run: {len(tasks)} tasks")
        for i, task in enumerate(tasks, 1):
            print(f"{i}/{len(tasks)} Task {task.id}")
            batch_progress.tick(task.id)
            try:
                result = run_task(
                    task_id=task.id,
                    task_text=task.task,
                    task_category=task.category,
                    run_baseline_flag=req.run_baseline,
                    run_rag_flag=req.run_rag,
                    city=task.city,
                )
                results_store[result.task_id] = result
                save_results_to_disk()
                batch_progress.done(task.id, success=True)
            except Exception as e:
                print(f"Failed: {e}")
                batch_progress.done(task.id, success=False)
        batch_progress.finish()
        print(f"Batch complete: {len(tasks)} tasks processed")

    background_tasks.add_task(run_background)

    return {
        "message": f"Started running {len(tasks)} tasks in background",
        "task_count": len(tasks),
        "check_progress": "GET /results"
    }


# ══════════════════════════════════════════════════════════════
# RESULTS ENDPOINTS
# ══════════════════════════════════════════════════════════════

@app.get("/results", response_model=List[TaskResult], tags=["Results"])
def get_results(category: Optional[str] = None, scored_only: bool = False):
    """Get all results. Optionally filter by category or scored status."""
    results = list(results_store.values())

    if category:
        results = [r for r in results if r.category == category]

    if scored_only:
        results = [r for r in results if r.baseline_scores or r.rag_scores]

    # Sort by task_id for consistent ordering
    results.sort(key=lambda r: r.task_id)
    return results


@app.post("/score/{task_id}", response_model=TaskResult, tags=["Scoring"])
def submit_score(task_id: str, score: ScoreSubmission):
    if task_id not in results_store:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    result = results_store[task_id]
    if score.system == "baseline":
        result.baseline_scores = score
    else:
        result.rag_scores = score
    results_store[task_id] = result
    save_results_to_disk()
    return result


@app.delete("/results", tags=["Results"])
def clear_results():
    """Clear all results from memory and disk. Use with caution!"""
    results_store.clear()
    if _RESULTS_JSON.exists():
        _RESULTS_JSON.unlink()
    return {"message": "All results cleared"}


@app.get("/run/progress", tags=["Experiment"])
def get_run_progress():
    """Poll this while /run/all is running to get live progress."""
    return batch_progress.to_dict()

@app.get("/validation", tags=["Evaluation"])
def get_validation():
    """Inter-model agreement summary written by judge_agreement.py, or null if not run."""
    p = RESULTS_DIR / "judge_agreement.json"
    return json.loads(p.read_text()) if p.exists() else None


@app.get("/model-comparison", tags=["Evaluation"])
def get_model_comparison():
    """Citation errors by base model: gpt-4o-mini (from citation_check.csv) vs the
    alternate generator run by model_comparison.py. Null if the alt run is missing."""
    import csv
    p = RESULTS_DIR / "model_comparison_gpt-4.1.json"
    if not p.exists():
        return None
    alt = json.loads(p.read_text())
    rows = list(csv.DictReader(open(RESULTS_DIR / "citation_check.csv")))

    def agg(system):
        seen, fab, mis, cited = set(), 0, 0, 0
        for r in rows:
            if r["system"] == system and r["task_id"] not in seen:
                seen.add(r["task_id"])
                fab += int(r["codes_fabricated"]); mis += int(r["codes_misattributed"]); cited += int(r["codes_cited"])
        return {"cited": cited, "fabricated": fab, "misattributed": mis}

    pick = lambda d: {"cited": d["cited"], "fabricated": d["fabricated"], "misattributed": d["misattributed"]}
    return {"models": [
        {"model": "gpt-4o-mini", "baseline": agg("baseline"), "rag": agg("rag")},
        {"model": alt["model"], "baseline": pick(alt["baseline"]), "rag": pick(alt["rag"])},
    ]}


# ══════════════════════════════════════════════════════════════
# EVALUATION & EXPORT ENDPOINTS
# ══════════════════════════════════════════════════════════════

@app.post("/evaluate/ragas", tags=["Evaluation"])
def run_ragas_evaluation():
    """
    Run RAGAS automated evaluation on all RAG results.
    Writes faithfulness / answer_relevancy back into the store BY RESULT_ID.
    """
    results = list(results_store.values())
    if not results:
        raise HTTPException(status_code=400, detail="No results to evaluate")

    # evaluate_with_ragas now returns {result_id: TaskResult}
    updated_map = evaluate_with_ragas(results)

    # Write back by the store's REAL key (result_id / UUID) — fixes overwrite bug
    for result_id, result in updated_map.items():
        results_store[result_id] = result
    save_results_to_disk()

    scored = len([r for r in updated_map.values() if r.ragas_faithfulness is not None])
    return {"evaluated": scored, "message": "RAGAS evaluation complete"}


@app.get("/export/csv", tags=["Export"])
def export_csv():
    """
    Export all results to a CSV file and return it for download.
    This is the file you import into Excel / Python for your dissertation analysis.
    """
    results = list(results_store.values())
    if not results:
        raise HTTPException(status_code=400, detail="No results to export")

    filepath = export_to_csv(results)

    return FileResponse(
        path=str(filepath),
        media_type="text/csv",
        filename=filepath.name
    )


@app.get("/export/json", tags=["Export"])
def export_json():
    """Export all results as JSON (useful for backup / further processing)."""
    results = [r.model_dump() for r in results_store.values()]
    if not results:
        raise HTTPException(status_code=400, detail="No results to export")

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    from datetime import datetime
    filepath = RESULTS_DIR / f"results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filepath, "w") as f:
        json.dump(results, f, indent=2, default=str)

    return FileResponse(
        path=str(filepath),
        media_type="application/json",
        filename=filepath.name
    )
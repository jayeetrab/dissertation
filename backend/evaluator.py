# evaluator.py — RAGAS fix (version-aware) + correct result-store keying
# ═══════════════════════════════════════════════════════════════════════
# TWO bugs were causing "RAGAS does nothing":
#
#  BUG 1 — API version mismatch. The old code used RAGAS 0.1.x style
#          (module-level `faithfulness` singletons + `metric.llm = llm`
#          + Dataset.from_dict). RAGAS 0.2.x removed that API, so on a
#          fresh install the call silently fails or scores nothing.
#          FIX: detect the installed version and call the right API.
#
#  BUG 2 — write-back keying. The /evaluate/ragas endpoint wrote results
#          back with results_store[result.task_id], but the store is keyed
#          by result_id (UUID). With 240 outputs sharing task_ids across
#          baseline/RAG and across cities, scores collided/overwrote.
#          FIX: return a {result_id: result} map and write back by result_id.
# ═══════════════════════════════════════════════════════════════════════

import csv
import statistics
from pathlib import Path
from datetime import datetime
from typing import List, Optional, Dict

from config import RESULTS_DIR, OPENAI_API_KEY
from models import TaskResult


def _ragas_version() -> tuple[int, int]:
    try:
        import ragas
        v = getattr(ragas, "__version__", "0.0.0").split(".")
        return int(v[0]), int(v[1])
    except Exception:
        return 0, 0


def _new_api(evaluable: List[TaskResult]) -> List[TaskResult]:
    """RAGAS 0.2.x — EvaluationDataset + SingleTurnSample + class metrics."""
    from ragas import evaluate as ragas_evaluate
    from ragas.dataset_schema import SingleTurnSample, EvaluationDataset
    from ragas.metrics import Faithfulness, AnswerRelevancy
    from ragas.llms import LangchainLLMWrapper
    from ragas.embeddings import LangchainEmbeddingsWrapper
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings

    llm = LangchainLLMWrapper(ChatOpenAI(
        model="gpt-4o-mini", temperature=0, openai_api_key=OPENAI_API_KEY))
    emb = LangchainEmbeddingsWrapper(OpenAIEmbeddings(
        model="text-embedding-3-small", openai_api_key=OPENAI_API_KEY))

    metrics = [Faithfulness(llm=llm), AnswerRelevancy(llm=llm, embeddings=emb)]
    samples = [
        SingleTurnSample(
            user_input=r.task_text,
            response=r.rag_output,
            retrieved_contexts=[
                f"[{c.source_doc} p.{c.page_number}] {c.content}"
                for c in r.retrieved_chunks],
        ) for r in evaluable
    ]
    df = ragas_evaluate(dataset=EvaluationDataset(samples=samples),
                        metrics=metrics).to_pandas()
    cf = next((c for c in df.columns if "faith" in c.lower()), None)
    cr = next((c for c in df.columns if "relev" in c.lower()), None)
    for i, r in enumerate(evaluable):
        if i < len(df):
            row = df.iloc[i]
            r.ragas_faithfulness = round(float(row[cf] or 0), 4) if cf else None
            r.ragas_answer_relevancy = round(float(row[cr] or 0), 4) if cr else None
            r.ragas_context_precision = None
    return evaluable


def _old_api(evaluable: List[TaskResult]) -> List[TaskResult]:
    """RAGAS 0.1.x — HuggingFace Dataset + module singletons."""
    from ragas import evaluate as ragas_evaluate
    from ragas.metrics import faithfulness, answer_relevancy
    from ragas.llms import LangchainLLMWrapper
    from langchain_openai import ChatOpenAI
    from datasets import Dataset

    llm = LangchainLLMWrapper(ChatOpenAI(
        model="gpt-4o-mini", temperature=0, openai_api_key=OPENAI_API_KEY))
    faithfulness.llm = llm
    answer_relevancy.llm = llm

    ds = Dataset.from_dict({
        "question": [r.task_text for r in evaluable],
        "answer":   [r.rag_output for r in evaluable],
        "contexts": [[f"[{c.source_doc} p.{c.page_number}] {c.content}"
                      for c in r.retrieved_chunks] for r in evaluable],
    })
    df = ragas_evaluate(dataset=ds, metrics=[faithfulness, answer_relevancy],
                        raise_exceptions=False).to_pandas()
    for i, r in enumerate(evaluable):
        if i < len(df):
            row = df.iloc[i]
            r.ragas_faithfulness = round(float(row.get("faithfulness", 0) or 0), 4)
            r.ragas_answer_relevancy = round(float(row.get("answer_relevancy", 0) or 0), 4)
            r.ragas_context_precision = None
    return evaluable


def evaluate_with_ragas(results: List[TaskResult]) -> Dict[str, TaskResult]:
    """
    Returns a {result_id: TaskResult} map so the caller can write back by the
    CORRECT key. (This is the fix for BUG 2 — see endpoint snippet below.)
    """
    major, minor = _ragas_version()
    if (major, minor) == (0, 0):
        print("RAGAS not installed. Run: pip install ragas datasets langchain-openai")
        return {r.result_id: r for r in results}

    evaluable = [
        r for r in results
        if r.rag_output and r.retrieved_chunks
        and not r.rag_output.startswith("[ERROR")
        and "__ablation__" not in r.task_id
    ]
    if not evaluable:
        print("No evaluable RAG results. Run tasks first.")
        return {r.result_id: r for r in results}

    print(f"\nRAGAS v{major}.{minor} — evaluating {len(evaluable)} RAG outputs ...")
    try:
        updated = _new_api(evaluable) if (major, minor) >= (0, 2) else _old_api(evaluable)
        fv = [r.ragas_faithfulness for r in updated if r.ragas_faithfulness is not None]
        rv = [r.ragas_answer_relevancy for r in updated if r.ragas_answer_relevancy is not None]
        print(f"RAGAS complete — {len(updated)} scored")
        if fv: print(f"  mean faithfulness:     {statistics.mean(fv):.3f}")
        if rv: print(f"  mean answer relevancy: {statistics.mean(rv):.3f}")
    except Exception as e:
        print(f"RAGAS failed: {e}")
        print("  Check OPENAI_API_KEY, and: pip install --upgrade ragas langchain-openai")

    # Return keyed by result_id (UUID) — the store's real key
    return {r.result_id: r for r in results}

def compute_summary_stats(results: List[TaskResult]) -> dict:
    tasks_with_results = len([r for r in results if r.baseline_output or r.rag_output])
    tasks_scored = len([r for r in results if r.baseline_scores or r.rag_scores])
    tasks_auto_scored = len([r for r in results if r.baseline_auto_scores or r.rag_auto_scores])

    # Prefer the human score for a system, but fall back to the automated
    # LLM-judge score so the dashboard reflects the primary (automated)
    # evaluation before the manual validation subset has been scored.
    def _score(r, system):
        return getattr(r, f"{system}_scores") or getattr(r, f"{system}_auto_scores")

    def _acc(r, system):
        s = _score(r, system)
        return s.accuracy if s and s.accuracy else None

    def _halluc(r, system):
        s = _score(r, system)
        return (1 if s.hallucination_present else 0) if s else None

    baseline_acc = [a for r in results if (a := _acc(r, "baseline")) is not None]
    rag_acc = [a for r in results if (a := _acc(r, "rag")) is not None]
    base_halluc = [h for r in results if (h := _halluc(r, "baseline")) is not None]
    rag_halluc = [h for r in results if (h := _halluc(r, "rag")) is not None]

    return {
        "tasks_with_results": tasks_with_results,
        "tasks_scored": tasks_scored,
        "tasks_auto_scored": tasks_auto_scored,
        "avg_baseline_accuracy": round(sum(baseline_acc)/len(baseline_acc), 2) if baseline_acc else 0.0,
        "avg_rag_accuracy": round(sum(rag_acc)/len(rag_acc), 2) if rag_acc else 0.0,
        "hallucination_rate_baseline": round(sum(base_halluc)/len(base_halluc), 2) if base_halluc else 0.0,
        "hallucination_rate_rag": round(sum(rag_halluc)/len(rag_halluc), 2) if rag_halluc else 0.0,
    }

def export_to_csv(results: List[TaskResult]) -> Path:
    import csv
    from datetime import datetime
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    filepath = RESULTS_DIR / f"results_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["result_id", "task_id", "city", "category", "baseline_output", "rag_output", "baseline_accuracy", "rag_accuracy", "baseline_hallucination", "rag_hallucination", "ragas_faithfulness", "ragas_answer_relevancy"])
        for r in results:
            writer.writerow([
                r.result_id, r.task_id, r.city, r.category,
                r.baseline_output,
                r.rag_output,
                r.baseline_scores.accuracy if r.baseline_scores else "",
                r.rag_scores.accuracy if r.rag_scores else "",
                r.baseline_scores.hallucination_present if r.baseline_scores else "",
                r.rag_scores.hallucination_present if r.rag_scores else "",
                r.ragas_faithfulness,
                r.ragas_answer_relevancy
            ])
    return filepath
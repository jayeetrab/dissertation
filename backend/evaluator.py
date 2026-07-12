# evaluator.py — FIXED
# Root cause of RAGAS being broken: API changed completely between 0.1.x and 0.2.x
# This file auto-detects the version and uses the right API.
# If RAGAS is missing entirely, it skips gracefully with clear messages.

import csv
import statistics
from pathlib import Path
from datetime import datetime
from typing import List, Optional

from config import RESULTS_DIR, OPENAI_API_KEY
from models import TaskResult


def _ragas_version() -> tuple[int, int]:
    """Return (major, minor) of installed ragas, or (0,0) if not found."""
    try:
        import ragas
        v = getattr(ragas, '__version__', '0.0.0')
        parts = v.split('.')
        return int(parts[0]), int(parts[1])
    except Exception:
        return 0, 0


def _evaluate_new_api(evaluable: list) -> list:
    """RAGAS 0.2.x: EvaluationDataset + SingleTurnSample + class-based metrics."""
    from ragas import evaluate as ragas_evaluate
    from ragas.dataset_schema import SingleTurnSample, EvaluationDataset
    from ragas.metrics import Faithfulness, AnswerRelevancy
    from ragas.llms import LangchainLLMWrapper
    from langchain_openai import ChatOpenAI

    llm = LangchainLLMWrapper(
        ChatOpenAI(model="gpt-4o-mini", temperature=0,
                   openai_api_key=OPENAI_API_KEY))

    metrics  = [Faithfulness(llm=llm), AnswerRelevancy(llm=llm)]
    samples  = [
        SingleTurnSample(
            user_input=r.task_text,
            response=r.rag_output,
            retrieved_contexts=[
                f"[{c.source_doc} p.{c.page_number}] {c.content}"
                for c in r.retrieved_chunks],
        ) for r in evaluable
    ]
    dataset = EvaluationDataset(samples=samples)
    result  = ragas_evaluate(dataset=dataset, metrics=metrics)
    df      = result.to_pandas()

    # Column names vary — find them by substring
    col_f = next((c for c in df.columns if 'faith'  in c.lower()), None)
    col_r = next((c for c in df.columns if 'relev'  in c.lower()), None)

    for i, r in enumerate(evaluable):
        if i < len(df):
            row = df.iloc[i]
            r.ragas_faithfulness      = round(float(row[col_f] or 0), 4) if col_f else None
            r.ragas_answer_relevancy  = round(float(row[col_r] or 0), 4) if col_r else None
            r.ragas_context_precision = None   # needs ground_truth; skip
    return evaluable


def _evaluate_old_api(evaluable: list) -> list:
    """RAGAS 0.1.x: HuggingFace Dataset + module-level singletons."""
    from ragas import evaluate as ragas_evaluate
    from ragas.metrics import faithfulness, answer_relevancy
    from ragas.llms import LangchainLLMWrapper
    from langchain_openai import ChatOpenAI
    from datasets import Dataset

    llm = LangchainLLMWrapper(
        ChatOpenAI(model="gpt-4o-mini", temperature=0,
                   openai_api_key=OPENAI_API_KEY))

    faithfulness.llm     = llm
    answer_relevancy.llm = llm

    dataset = Dataset.from_dict({
        "question": [r.task_text  for r in evaluable],
        "answer":   [r.rag_output for r in evaluable],
        "contexts": [
            [f"[{c.source_doc} p.{c.page_number}] {c.content}"
             for c in r.retrieved_chunks]
            for r in evaluable],
    })
    scores = ragas_evaluate(
        dataset=dataset,
        metrics=[faithfulness, answer_relevancy],
        raise_exceptions=False,
    )
    df = scores.to_pandas()

    for i, r in enumerate(evaluable):
        if i < len(df):
            row = df.iloc[i]
            r.ragas_faithfulness     = round(float(row.get("faithfulness",    0) or 0), 4)
            r.ragas_answer_relevancy = round(float(row.get("answer_relevancy", 0) or 0), 4)
            r.ragas_context_precision = None
    return evaluable


def evaluate_with_ragas(results: List[TaskResult]) -> List[TaskResult]:
    """
    Main entry point. Detects RAGAS version → calls correct API.
    The previous code was broken because RAGAS 0.2.x changed:
      - Metrics are now classes (Faithfulness()) not singletons (faithfulness)
      - Accepts EvaluationDataset not HuggingFace Dataset
      - Column names in output DataFrame changed
    This function handles both versions automatically.
    """
    major, minor = _ragas_version()

    if major == 0 and minor == 0:
        print("RAGAS not installed. Run: pip install ragas datasets")
        return results

    evaluable = [
        r for r in results
        if r.rag_output
        and r.retrieved_chunks
        and not r.rag_output.startswith("[ERROR")
        and "__ablation__" not in r.task_id
    ]

    if not evaluable:
        print("No evaluable RAG results found. Run tasks first.")
        return results

    print(f"\nRAGAS v{major}.{minor} — evaluating {len(evaluable)} results ...")

    try:
        if major == 0 and minor >= 2:
            print("  Using RAGAS 0.2.x API")
            updated = _evaluate_new_api(evaluable)
        else:
            print("  Using RAGAS 0.1.x API")
            updated = _evaluate_old_api(evaluable)

        # Merge scores back by task_id
        scored_map = {r.task_id: r for r in updated}
        for r in results:
            if r.task_id in scored_map:
                u = scored_map[r.task_id]
                r.ragas_faithfulness      = u.ragas_faithfulness
                r.ragas_answer_relevancy  = u.ragas_answer_relevancy
                r.ragas_context_precision = u.ragas_context_precision

        # Print summary
        fv = [r.ragas_faithfulness     for r in updated if r.ragas_faithfulness is not None]
        rv = [r.ragas_answer_relevancy for r in updated if r.ragas_answer_relevancy is not None]
        print(f"RAGAS complete — {len(updated)} results scored")
        if fv: print(f"  Avg faithfulness:     {statistics.mean(fv):.3f}")
        if rv: print(f"  Avg answer relevancy: {statistics.mean(rv):.3f}")

    except Exception as e:
        print(f"RAGAS failed: {e}")
        print("  Check OPENAI_API_KEY in .env and try: pip install --upgrade ragas")
        print("  Manual scores are unaffected.")

    return results


def export_to_csv(results: List[TaskResult],
                  filename: Optional[str] = None) -> Path:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    if filename is None:
        filename = f"results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    filepath = RESULTS_DIR / filename

    fieldnames = [
        "task_id", "category", "city", "system", "timestamp",
        "output_text", "tokens_used",
        "num_chunks_retrieved", "sources_retrieved",
        "avg_relevance_score", "corpus_filter",
        "pct_chunks_task_city", "pct_chunks_national", "pct_chunks_other_city",
        "ragas_faithfulness", "ragas_answer_relevancy",
        "ragas_context_precision",
        "accuracy_1_5", "completeness_1_5",
        "planning_usefulness_1_5", "grounding_0_2",
        "hallucination_present", "hallucination_type",
        "hallucination_detail", "scorer_notes",
    ]

    rows = []
    for result in results:
        corpus_str = ("|".join(result.corpus_filter)
                      if getattr(result, 'corpus_filter', None) else "all")

        task_city = getattr(result, 'city', None) or "bristol"

        if result.baseline_output:
            bs = result.baseline_scores
            rows.append({"task_id": result.task_id, "category": result.category,
                "city": task_city,
                "system": "baseline", "timestamp": result.timestamp,
                "output_text": result.baseline_output,
                "tokens_used": result.baseline_tokens_used or "",
                "num_chunks_retrieved": 0, "sources_retrieved": "",
                "avg_relevance_score": "", "corpus_filter": corpus_str,
                "ragas_faithfulness": "", "ragas_answer_relevancy": "",
                "ragas_context_precision": "",
                "accuracy_1_5":            bs.accuracy             if bs else "",
                "completeness_1_5":        bs.completeness         if bs else "",
                "planning_usefulness_1_5": bs.planning_usefulness  if bs else "",
                "grounding_0_2":           bs.grounding            if bs else "",
                "hallucination_present":   bs.hallucination_present if bs else "",
                "hallucination_type":      bs.hallucination_type    if bs else "",
                "hallucination_detail":    bs.hallucination_detail  if bs else "",
                "scorer_notes":            bs.scorer_notes          if bs else ""})

        if result.rag_output:
            rs     = result.rag_scores
            chunks = result.retrieved_chunks or []
            avg_rel = (round(statistics.mean(c.relevance_score for c in chunks), 4)
                       if chunks else "")
            sources = " | ".join(f"{c.source_doc} p.{c.page_number}" for c in chunks)

            # City-mix of retrieved chunks: the spatial misattribution signal.
            # Chunks from the task's own city or national policy are fine;
            # chunks from ANOTHER city's local plan are retrieval contamination.
            pct_own, pct_nat, pct_other = "", "", ""
            tagged = [c for c in chunks if getattr(c, 'city', None)]
            if tagged:
                n = len(tagged)
                own   = sum(1 for c in tagged if c.city == task_city)
                nat   = sum(1 for c in tagged if c.city == "national")
                pct_own   = round(own / n, 3)
                pct_nat   = round(nat / n, 3)
                pct_other = round((n - own - nat) / n, 3)

            rows.append({"task_id": result.task_id, "category": result.category,
                "city": task_city,
                "system": "rag", "timestamp": result.timestamp,
                "pct_chunks_task_city": pct_own,
                "pct_chunks_national": pct_nat,
                "pct_chunks_other_city": pct_other,
                "output_text": result.rag_output,
                "tokens_used": result.rag_tokens_used or "",
                "num_chunks_retrieved": len(chunks), "sources_retrieved": sources,
                "avg_relevance_score": avg_rel, "corpus_filter": corpus_str,
                "ragas_faithfulness":      result.ragas_faithfulness      or "",
                "ragas_answer_relevancy":  result.ragas_answer_relevancy  or "",
                "ragas_context_precision": result.ragas_context_precision or "",
                "accuracy_1_5":            rs.accuracy             if rs else "",
                "completeness_1_5":        rs.completeness         if rs else "",
                "planning_usefulness_1_5": rs.planning_usefulness  if rs else "",
                "grounding_0_2":           rs.grounding            if rs else "",
                "hallucination_present":   rs.hallucination_present if rs else "",
                "hallucination_type":      rs.hallucination_type    if rs else "",
                "hallucination_detail":    rs.hallucination_detail  if rs else "",
                "scorer_notes":            rs.scorer_notes          if rs else ""})

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"CSV exported: {filepath}  ({len(rows)} rows)")
    return filepath


def compute_summary_stats(results: List[TaskResult]) -> dict:
    b_acc, r_acc   = [], []
    b_hlc, r_hlc   = 0, 0
    b_scored, r_scored = 0, 0
    for r in results:
        if "__ablation__" in r.task_id:
            continue
        if r.baseline_scores:
            b_acc.append(r.baseline_scores.accuracy)
            if r.baseline_scores.hallucination_present:
                b_hlc += 1
            b_scored += 1
        if r.rag_scores:
            r_acc.append(r.rag_scores.accuracy)
            if r.rag_scores.hallucination_present:
                r_hlc += 1
            r_scored += 1
    return {
        "tasks_with_results": len([r for r in results
            if (r.baseline_output or r.rag_output)
            and "__ablation__" not in r.task_id]),
        "tasks_scored": len([r for r in results
            if (r.baseline_scores or r.rag_scores)
            and "__ablation__" not in r.task_id]),
        "avg_baseline_accuracy": round(statistics.mean(b_acc), 2) if b_acc else None,
        "avg_rag_accuracy":      round(statistics.mean(r_acc), 2) if r_acc else None,
        "hallucination_rate_baseline": round(b_hlc/b_scored, 3) if b_scored else None,
        "hallucination_rate_rag":      round(r_hlc/r_scored, 3) if r_scored else None,
    }
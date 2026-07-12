# auto_score.py
# ─────────────────────────────────────────────────────────────
# LLM-as-judge automated rubric scoring.
#
# Fills baseline_auto_scores / rag_auto_scores on every result record using
# the SAME rubric a human scorer would apply on the Evaluate page (accuracy,
# completeness, planning usefulness, grounding, hallucination). This is the
# automated counterpart to manual scoring: it lets the full library be scored
# without ~9h of human effort, while a small human-scored subset is retained
# to validate the judge (inter-rater agreement, reported in the methodology).
#
# Design choices that keep it defensible:
#   - Judge model is gpt-4o (stronger and distinct from the gpt-4o-mini
#     system-under-test), reducing same-model self-preference bias.
#   - temperature=0 for reproducibility.
#   - For RAG answers the judge sees the ACTUAL retrieved chunks, so accuracy
#     and grounding are assessed against the real evidence, not the judge's
#     own recall.
#   - Scores are written to SEPARATE fields; manual scores are never touched.
#
# Usage:
#   python auto_score.py                 (score every unscored output)
#   python auto_score.py --overwrite     (re-score everything)
#   python auto_score.py --limit 5       (smoke-test on the first 5 tasks)
# ─────────────────────────────────────────────────────────────

import json
import argparse
from typing import Optional

from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

from config import OPENAI_API_KEY, RESULTS_DIR
from models import AutoScore

STORE = RESULTS_DIR / "results_store.json"
JUDGE_MODEL = "gpt-4o"

RUBRIC = """You are a meticulous senior UK town-planning examiner. Score an AI
assistant's answer to a planning task, strictly and objectively.

Scoring rubric:
- accuracy (1-5): factual correctness of the planning content. 1 = wrong or
  fabricated; 5 = fully correct and supported. If the answer cites policy codes
  or paragraphs that are NOT in the provided source context (or do not exist),
  treat that as a serious accuracy failure.
- completeness (1-5): does it address every part the task asks for? 1 = misses
  most; 5 = covers all required elements.
- planning_usefulness (1-5): would a busy planning officer find it directly
  usable? 1 = useless; 5 = immediately actionable.
- grounding (0-2): 0 = asserts with no source; 1 = vague/general reference;
  2 = specific, checkable citation (named policy code or NPPF paragraph).
- hallucination_present (bool) and hallucination_type (one of: none,
  fabricated_clause, outdated_policy, spatial_misattribution,
  confident_ambiguity). Mark present=true ONLY for a specific claim that is
  invented or wrong: a policy code/clause that does not exist
  (fabricated_clause), a superseded pre-December-2024 rule stated as current
  (outdated_policy), a policy attributed to the wrong city
  (spatial_misattribution), or a confident definitive answer where policy is
  actually silent or ambiguous (confident_ambiguity). A citation that is
  plausibly real but simply not present in the provided source context is NOT
  a hallucination — reflect that only through a lower grounding score. Put the
  exact offending quote in hallucination_detail.
Be conservative: when in doubt, hallucination_present=false."""


class JudgeVerdict(BaseModel):
    """The fields the judge model fills for one output."""
    accuracy: int = Field(..., ge=1, le=5)
    completeness: int = Field(..., ge=1, le=5)
    planning_usefulness: int = Field(..., ge=1, le=5)
    grounding: int = Field(..., ge=0, le=2)
    hallucination_present: bool = False
    hallucination_type: str = "none"
    hallucination_detail: Optional[str] = None
    rationale: str = Field("", description="One sentence justifying the scores.")


def _context_block(chunks) -> str:
    if not chunks:
        return "(No retrieved context — this system answers from model knowledge alone.)"
    lines = []
    for i, c in enumerate(chunks, 1):
        lines.append(f"[{i}] {c.get('source_doc')} p.{c.get('page_number')} "
                     f"(city: {c.get('city')}):\n{(c.get('content') or '')[:600]}")
    return "\n\n".join(lines)


def _score_output(judge, task_text, system, output, chunks) -> Optional[AutoScore]:
    if not output:
        return None
    prompt = (
        f"{RUBRIC}\n\n"
        f"=== TASK ===\n{task_text}\n\n"
        f"=== SYSTEM UNDER TEST ===\n{system}\n\n"
        f"=== SOURCE CONTEXT PROVIDED TO THE SYSTEM ===\n{_context_block(chunks)}\n\n"
        f"=== ANSWER TO SCORE ===\n{output}\n\n"
        f"Return the rubric scores for this answer."
    )
    v: JudgeVerdict = judge.invoke(prompt)
    htype = v.hallucination_type if v.hallucination_type in {
        "none", "fabricated_clause", "outdated_policy",
        "spatial_misattribution", "confident_ambiguity"} else "none"
    return AutoScore(
        system=system,
        accuracy=v.accuracy,
        completeness=v.completeness,
        planning_usefulness=v.planning_usefulness,
        grounding=v.grounding,
        hallucination_present=v.hallucination_present,
        hallucination_type=htype,
        hallucination_detail=v.hallucination_detail,
        judge_model=JUDGE_MODEL,
        judge_rationale=v.rationale,
    )


_JUDGE = None


def get_judge():
    """Lazily build and cache the structured-output judge (used by the API)."""
    global _JUDGE
    if _JUDGE is None:
        _JUDGE = ChatOpenAI(model=JUDGE_MODEL, temperature=0,
                            openai_api_key=OPENAI_API_KEY).with_structured_output(JudgeVerdict)
    return _JUDGE


def score_output(task_text, system, output, chunks) -> Optional[AutoScore]:
    """Public entry point: score one output with the LLM-as-judge.

    Reused by the FastAPI endpoint so evaluation can be triggered from the UI.
    """
    return _score_output(get_judge(), task_text, system, output, chunks)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--overwrite", action="store_true",
                    help="re-score outputs that already have auto scores")
    ap.add_argument("--limit", type=int, default=None,
                    help="only process the first N task records (smoke test)")
    args = ap.parse_args()

    store = json.load(open(STORE))
    judge = ChatOpenAI(model=JUDGE_MODEL, temperature=0,
                       openai_api_key=OPENAI_API_KEY).with_structured_output(JudgeVerdict)

    items = list(store.items())
    if args.limit:
        items = items[:args.limit]

    scored = 0
    for i, (key, rec) in enumerate(items, 1):
        for system, out_field, score_field in [
            ("baseline", "baseline_output", "baseline_auto_scores"),
            ("rag", "rag_output", "rag_auto_scores"),
        ]:
            if not rec.get(out_field):
                continue
            if rec.get(score_field) and not args.overwrite:
                continue
            try:
                auto = _score_output(judge, rec["task_text"], system,
                                     rec[out_field], rec.get("retrieved_chunks"))
                if auto:
                    rec[score_field] = auto.model_dump()
                    scored += 1
            except Exception as e:
                print(f"  ! {rec.get('task_id')} {system}: {e}")
        print(f"[{i}/{len(items)}] {rec.get('task_id')} scored")
        json.dump(store, open(STORE, "w"), indent=2, default=str)  # incremental, crash-safe

    print(f"\nDone. {scored} outputs auto-scored with {JUDGE_MODEL}.")


if __name__ == "__main__":
    main()

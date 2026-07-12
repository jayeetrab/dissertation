# judge_agreement.py
# ─────────────────────────────────────────────────────────────
# Inter-model reliability check for the automated rubric.
#
# A second judge (gpt-4.1), different from the primary judge (gpt-4o) and from
# the gpt-4o-mini system under test, re-scores a stratified sample of outputs.
# We then measure agreement between the two judges. This tests whether the
# rubric scores are stable across models, i.e. consistency. It does NOT test
# correctness: two models can agree and both be wrong, so this complements but
# does not replace human validation.
#
# Sample: 2 tasks per breadth city (seed 42), both systems -> 40 outputs.
#
# Usage: python judge_agreement.py
# ─────────────────────────────────────────────────────────────

import json
import random
import argparse
import statistics as st

from scipy import stats
from langchain_openai import ChatOpenAI

from config import OPENAI_API_KEY, TASKS_FILE, RESULTS_DIR
from auto_score import JudgeVerdict, _score_output
from spatial import CITY_CENTROIDS

SECOND_MODEL = "gpt-4.1"
METRICS = ["accuracy", "completeness", "planning_usefulness", "grounding"]


def sample_task_ids(all_tasks=False):
    tasks = json.load(open(TASKS_FILE))
    if all_tasks:
        return [t["id"] for t in tasks]
    by_city = {}
    for t in tasks:
        c = t.get("city")
        if c and c != "bristol" and c in CITY_CENTROIDS:
            by_city.setdefault(c, []).append(t["id"])
    rng = random.Random(42)
    picked = []
    for c in sorted(by_city):
        picked += rng.sample(sorted(by_city[c]), 2)
    return picked


def cohen_kappa(a, b):
    n = len(a)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pa1 = sum(a) / n
    pb1 = sum(b) / n
    pe = pa1 * pb1 + (1 - pa1) * (1 - pb1)
    return (po - pe) / (1 - pe) if pe != 1 else 1.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="score all 120 tasks, not the sample")
    args = ap.parse_args()

    store = json.load(open(RESULTS_DIR / "results_store.json"))
    judge2 = ChatOpenAI(model=SECOND_MODEL, temperature=0,
                        openai_api_key=OPENAI_API_KEY).with_structured_output(JudgeVerdict)

    ids = sample_task_ids(all_tasks=args.all)
    pairs = {m: ([], []) for m in METRICS}   # metric -> (gpt4o_vals, gpt41_vals)
    halluc = ([], [])
    # accuracy by system for each judge, to check both reproduce RAG > baseline
    direction = {"gpt-4o": {"baseline": [], "rag": []},
                 SECOND_MODEL: {"baseline": [], "rag": []}}

    for i, tid in enumerate(ids, 1):
        rec = store.get(tid)
        if not rec:
            continue
        for system, out_f, score_f, chunks in [
            ("baseline", "baseline_output", "baseline_auto_scores", None),
            ("rag", "rag_output", "rag_auto_scores", rec.get("retrieved_chunks")),
        ]:
            primary = rec.get(score_f)
            if not rec.get(out_f) or not primary:
                continue
            second = _score_output(judge2, rec["task_text"], system, rec[out_f], chunks)
            for m in METRICS:
                pairs[m][0].append(primary[m])
                pairs[m][1].append(getattr(second, m))
            halluc[0].append(1 if primary["hallucination_present"] else 0)
            halluc[1].append(1 if second.hallucination_present else 0)
            direction["gpt-4o"][system].append(primary["accuracy"])
            direction[SECOND_MODEL][system].append(second.accuracy)
        print(f"[{i}/{len(ids)}] {tid} scored by {SECOND_MODEL}")

    n = len(halluc[0])
    lines = [f"# Inter-model agreement: gpt-4o vs {SECOND_MODEL}\n",
             f"Stratified sample: 2 tasks per breadth city (seed 42), both systems "
             f"({n} outputs). Agreement measures consistency across judge models, "
             f"not correctness.\n",
             "| Rubric metric | Exact agreement | Mean abs. diff | Spearman r |",
             "|---|---|---|---|"]
    for m in METRICS:
        a, b = pairs[m]
        exact = sum(1 for x, y in zip(a, b) if x == y) / len(a)
        mad = st.mean(abs(x - y) for x, y in zip(a, b))
        rho = stats.spearmanr(a, b).correlation
        lines.append(f"| {m.replace('_', ' ')} | {exact:.0%} | {mad:.2f} | "
                     f"{rho:.2f} |" if rho == rho else
                     f"| {m.replace('_', ' ')} | {exact:.0%} | {mad:.2f} | n/a |")
    hk = cohen_kappa(halluc[0], halluc[1])
    hagree = sum(1 for x, y in zip(*halluc) if x == y) / n
    lines.append(f"\nHallucination flag: {hagree:.0%} agreement, Cohen's kappa = {hk:.2f} "
                 f"(n = {n}).\n")
    lines.append("Direction check (mean accuracy on the sample):\n")
    lines.append("| Judge | Baseline | RAG | Delta | paired p |")
    lines.append("|---|---|---|---|---|")
    for judge in ("gpt-4o", SECOND_MODEL):
        bl, rl = direction[judge]["baseline"], direction[judge]["rag"]
        b, r = st.mean(bl), st.mean(rl)
        p = stats.ttest_rel(rl, bl).pvalue if len(bl) > 1 else float("nan")
        lines.append(f"| {judge} | {b:.2f} | {r:.2f} | {r-b:+.2f} | {p:.2e} |")

    out = RESULTS_DIR / "judge_agreement.md"
    out.write_text("\n".join(lines) + "\n")

    # JSON summary for the web UI
    summary = {
        "judge_a": "gpt-4o", "judge_b": SECOND_MODEL, "n_outputs": n,
        "scope": "all 120 tasks" if len(ids) > 40 else "sample (2/breadth city, seed 42)",
        "metrics": [
            {"metric": m.replace("_", " "),
             "exact_agreement": round(sum(1 for x, y in zip(*pairs[m]) if x == y) / len(pairs[m][0]), 3),
             "mean_abs_diff": round(st.mean(abs(x - y) for x, y in zip(*pairs[m])), 2),
             "spearman": round(stats.spearmanr(*pairs[m]).correlation, 2)}
            for m in METRICS],
        "hallucination": {"agreement": round(hagree, 3), "kappa": round(hk, 2)},
        "direction": [
            {"judge": j,
             "baseline": round(st.mean(direction[j]["baseline"]), 2),
             "rag": round(st.mean(direction[j]["rag"]), 2),
             "delta": round(st.mean(direction[j]["rag"]) - st.mean(direction[j]["baseline"]), 2),
             "p": round(stats.ttest_rel(direction[j]["rag"], direction[j]["baseline"]).pvalue, 5)}
            for j in ("gpt-4o", SECOND_MODEL)],
    }
    (RESULTS_DIR / "judge_agreement.json").write_text(json.dumps(summary, indent=2))
    print("\n" + "\n".join(lines))
    print(f"\nWritten to {out} and judge_agreement.json")


if __name__ == "__main__":
    main()

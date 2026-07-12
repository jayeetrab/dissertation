# model_comparison.py
# ─────────────────────────────────────────────────────────────
# Does RAG still help when the base model is stronger?
#
# Re-runs baseline vs RAG with a different GENERATOR model (default gpt-4.1)
# on a focused sample, and scores each output with the deterministic citation
# instrument (fabricated / misattributed policy codes). No LLM judge is used,
# so the comparison is judge-independent.
#
# Sample: PC-01 and ST-02 for each breadth city (20 tasks). Both explicitly
# ask for specific local policy codes, so they are where fabrication shows.
#
# Usage: python model_comparison.py [model]   (default gpt-4.1)
# ─────────────────────────────────────────────────────────────

import sys
import json

from langchain_openai import ChatOpenAI

import rag_pipeline
from config import OPENAI_API_KEY, TASKS_FILE, RESULTS_DIR, TEMPERATURE, MAX_TOKENS
from citation_check import extract_citations, classify
from spatial import CITY_CENTROIDS

ALL = "--all" in sys.argv
args = [a for a in sys.argv[1:] if not a.startswith("-")]
MODEL = args[0] if args else "gpt-4.1"


def sample_tasks():
    tasks = json.load(open(TASKS_FILE))
    if ALL:
        return tasks
    keep = []
    for t in tasks:
        c = t.get("city")
        if c in CITY_CENTROIDS and c != "bristol" and t["id"].split("-", 1)[-1] in ("PC-01", "ST-02"):
            keep.append(t)
    return sorted(keep, key=lambda t: t["id"])


def score(text, city, index, known_families):
    codes, _ = extract_citations(text, known_families)
    fab = mis = ok = 0
    for c in codes:
        verdict, _ = classify(c, city, index)
        if verdict == "fabricated":
            fab += 1
        elif verdict == "misattributed":
            mis += 1
        else:
            ok += 1
    return ok, fab, mis


def main():
    # Inject the stronger generator into the cached pipeline
    rag_pipeline._llm = ChatOpenAI(model=MODEL, temperature=TEMPERATURE,
                                   max_tokens=MAX_TOKENS, openai_api_key=OPENAI_API_KEY)
    index = json.load(open(RESULTS_DIR / "policy_index.json"))
    known_families = {__import__("re").sub(r"\d.*", "", c)
                      for v in index.values() for c in v.get("policy_codes", [])}

    agg = {"baseline": [0, 0, 0, 0, 0], "rag": [0, 0, 0, 0, 0]}  # ok, fab, mis, outputs_with_fab, outputs_with_mis
    tasks = sample_tasks()
    for i, t in enumerate(tasks, 1):
        city = t["city"]
        b_out, _ = rag_pipeline.run_baseline(t["task"])
        r_out, _, _ = rag_pipeline.run_rag(t["task"])
        for system, out in [("baseline", b_out), ("rag", r_out)]:
            ok, fab, mis = score(out, city, index, known_families)
            a = agg[system]
            a[0] += ok; a[1] += fab; a[2] += mis
            a[3] += fab > 0; a[4] += mis > 0
        print(f"[{i}/{len(tasks)}] {t['id']}: baseline fab/mis, rag fab/mis printed at end")

    n = len(tasks)
    scope = f"all {n} tasks" if ALL else f"{n} tasks (PC-01 + ST-02 per breadth city)"
    lines = [f"# Base-model comparison: does RAG still help {MODEL}?\n",
             f"Generator = {MODEL}. {scope}, scored by the deterministic citation "
             f"instrument. No LLM judge.\n",
             "| System | Codes cited | Fabricated | Misattributed | Outputs w/ fabrication | Outputs w/ misattribution |",
             "|---|---|---|---|---|---|"]
    rows = {}
    for system in ("baseline", "rag"):
        ok, fab, mis, ofab, omis = agg[system]
        lines.append(f"| {system} | {ok+fab+mis} | {fab} | {mis} | "
                     f"{ofab}/{n} ({ofab/n:.0%}) | {omis}/{n} ({omis/n:.0%}) |")
        rows[system] = {"cited": ok+fab+mis, "fabricated": fab, "misattributed": mis,
                        "outputs_fabrication": ofab, "outputs_misattribution": omis}

    tag = MODEL.replace("/", "-")
    (RESULTS_DIR / f"model_comparison_{tag}.md").write_text("\n".join(lines) + "\n")
    (RESULTS_DIR / f"model_comparison_{tag}.json").write_text(
        json.dumps({"model": MODEL, "n": n, "scope": scope, **rows}, indent=2))
    print("\n" + "\n".join(lines))
    print(f"\nWritten to model_comparison_{tag}.md and .json")


if __name__ == "__main__":
    main()

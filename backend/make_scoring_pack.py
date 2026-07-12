# make_scoring_pack.py
# ─────────────────────────────────────────────────────────────
# Generates markdown "scoring packs" to make manual evaluation fast.
#
# Each pack entry shows: the task, the system output, the retrieved
# chunks (with source PDF + page so claims can be verified in seconds),
# and the rubric. Scores are entered in the frontend Evaluate page as
# usual — the pack is the reading aid, not the data store.
#
# Two packs:
#   python make_scoring_pack.py --bristol      (all Bristol outputs)
#   python make_scoring_pack.py --multicity    (stratified sample:
#         N tasks per city x both systems, deterministic seed)
# ─────────────────────────────────────────────────────────────

import json
import random
import argparse
from collections import defaultdict
from pathlib import Path

from config import RESULTS_DIR, TASKS_FILE, BASE_DIR

RUBRIC = """
| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |
"""


def write_entry(f, r: dict, system: str, task: dict):
    out = r.get(f"{system}_output")
    if not out:
        return False
    f.write(f"\n---\n\n## {r['task_id']} — {system.upper()}\n\n")
    f.write(f"**City:** {task.get('city','bristol')} | **Category:** {r['category']} "
            f"| **Difficulty:** {task.get('difficulty','?')}\n\n")
    f.write(f"**Task:** {r['task_text']}\n\n")
    exp = task.get("expected_paragraphs") or []
    if exp:
        f.write(f"**Expected policies (check these in the source PDF):** "
                f"{', '.join(exp)} — source: `{task.get('expected_source','?')}`\n\n")
    f.write(f"### Output ({system})\n\n{out}\n\n")
    if system == "rag":
        chunks = r.get("retrieved_chunks") or []
        f.write(f"### Retrieved context ({len(chunks)} chunks — verify citations against these)\n\n")
        for i, c in enumerate(chunks, 1):
            f.write(f"**[{i}] {c['source_doc']} p.{c['page_number']}"
                    f" (city: {c.get('city','?')}, score {c['relevance_score']})**\n"
                    f"> {c['content'][:400]}\n\n")
    f.write(f"### Rubric (enter in the Evaluate page for `{r['task_id']}` / {system})\n")
    f.write(RUBRIC)
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bristol", action="store_true")
    parser.add_argument("--multicity", action="store_true")
    parser.add_argument("--per-city", type=int, default=2,
                        help="tasks sampled per city for the multicity pack")
    parser.add_argument("--seed", type=int, default=42,
                        help="RNG seed — keep fixed and report it in the methodology")
    args = parser.parse_args()

    with open(RESULTS_DIR / "results_store.json") as f:
        results = {k: v for k, v in json.load(f).items()
                   if "__ablation__" not in v.get("task_id", "")}
    with open(TASKS_FILE) as f:
        tasks = {t["id"]: t for t in json.load(f)}

    by_task = {r["task_id"]: r for r in results.values()}

    packs_dir = BASE_DIR / "docs"

    if args.bristol:
        ids = sorted(tid for tid, r in by_task.items()
                     if tasks.get(tid, {}).get("city", "bristol") == "bristol")
        path = packs_dir / "scoring_pack_bristol.md"
        n = 0
        with open(path, "w") as f:
            f.write("# Scoring Pack — Bristol (deep case study, all outputs)\n")
            for tid in ids:
                r = by_task[tid]
                for system in ("baseline", "rag"):
                    n += write_entry(f, r, system, tasks.get(tid, {}))
        print(f"Bristol pack: {n} outputs -> {path}")

    if args.multicity:
        rng = random.Random(args.seed)
        by_city = defaultdict(list)
        for tid, r in by_task.items():
            city = tasks.get(tid, {}).get("city", "bristol")
            if city != "bristol":
                by_city[city].append(tid)
        path = packs_dir / "scoring_pack_multicity.md"
        n = 0
        with open(path, "w") as f:
            f.write(f"# Scoring Pack — Multi-city stratified sample "
                    f"({args.per_city}/city, seed={args.seed})\n")
            for city in sorted(by_city):
                # spread across categories: sort by category then sample evenly
                ids = sorted(by_city[city])
                cats = defaultdict(list)
                for tid in ids:
                    cats[by_task[tid]["category"]].append(tid)
                chosen = []
                cat_cycle = sorted(cats)
                rng.shuffle(cat_cycle)
                while len(chosen) < args.per_city and any(cats.values()):
                    for cat in cat_cycle:
                        if cats[cat] and len(chosen) < args.per_city:
                            chosen.append(cats[cat].pop(rng.randrange(len(cats[cat]))))
                for tid in chosen:
                    r = by_task[tid]
                    for system in ("baseline", "rag"):
                        n += write_entry(f, r, system, tasks.get(tid, {}))
        print(f"Multi-city pack: {n} outputs -> {path}")

    if not (args.bristol or args.multicity):
        parser.print_help()


if __name__ == "__main__":
    main()

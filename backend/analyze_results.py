# analyze_results.py
# ─────────────────────────────────────────────────────────────
# Produces the Chapter 4 tables and figures from the results store,
# the citation check, and the RAGAS scores.
#
# Outputs:
#   results/analysis_summary.md   (all tables, markdown)
#   results/figures/*.png         (dissertation-ready figures, 300 dpi)
#
# Usage: python analyze_results.py
# ─────────────────────────────────────────────────────────────

import json
import csv
import math
import statistics
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from config import RESULTS_DIR, TASKS_FILE

FIG_DIR = RESULTS_DIR / "figures"

PLAN_YEAR = {  # adoption year of each city's primary plan (docs/corpus_sources.md)
    "sheffield": 2009, "london": 2021, "leeds": 2019, "newcastle": 2015,
    "birmingham": 2017, "plymouth": 2019, "nottingham": 2020, "liverpool": 2022,
    "southampton": 2015, "leicester": 2026, "bristol": 2014,
}


def val(x):
    return x is not None and not (isinstance(x, float) and math.isnan(x))


def main():
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(RESULTS_DIR / "results_store.json") as f:
        results = list(json.load(f).values())
    with open(RESULTS_DIR / "citation_check.csv") as f:
        citations = list(csv.DictReader(f))
    with open(TASKS_FILE) as f:
        tasks = {t["id"]: t for t in json.load(f)}

    lines = ["# Results Analysis Summary",
             f"\n*Auto-generated from {len(results)} task results "
             f"(120 tasks x baseline+RAG). Figures in results/figures/.*\n"]

    # ── T1: RAGAS by city ─────────────────────────────────────
    by_city = defaultdict(lambda: {"f": [], "r": []})
    for r in results:
        if val(r.get("ragas_faithfulness")):
            by_city[r["city"]]["f"].append(r["ragas_faithfulness"])
        if val(r.get("ragas_answer_relevancy")):
            by_city[r["city"]]["r"].append(r["ragas_answer_relevancy"])

    lines.append("\n## Table 1 — RAGAS metrics by city (RAG system)\n")
    lines.append("| City | n | Faithfulness | Answer relevancy |")
    lines.append("|---|---|---|---|")
    for city in sorted(by_city):
        v = by_city[city]
        lines.append(f"| {city} | {len(v['f'])} | "
                     f"{statistics.mean(v['f']):.3f} | {statistics.mean(v['r']):.3f} |")
    allf = [x for v in by_city.values() for x in v["f"]]
    allr = [x for v in by_city.values() for x in v["r"]]
    lines.append(f"| **all** | {len(allf)} | **{statistics.mean(allf):.3f}** "
                 f"| **{statistics.mean(allr):.3f}** |")

    # ── T2: RAGAS by category ─────────────────────────────────
    by_cat = defaultdict(list)
    for r in results:
        if val(r.get("ragas_faithfulness")):
            by_cat[r["category"]].append(r["ragas_faithfulness"])
    lines.append("\n## Table 2 — RAGAS faithfulness by task category\n")
    lines.append("| Category | n | Faithfulness |")
    lines.append("|---|---|---|")
    for cat in sorted(by_cat):
        lines.append(f"| {cat} | {len(by_cat[cat])} | {statistics.mean(by_cat[cat]):.3f} |")

    # ── T3: citation check summary ────────────────────────────
    sums = defaultdict(lambda: defaultdict(int))
    for row in citations:
        s = sums[row["system"]]
        s["outputs"] += 1
        s["cited"] += int(row["codes_cited"])
        s["fab"] += int(row["codes_fabricated"])
        s["mis"] += int(row["codes_misattributed"])
        s["fab_outputs"] += int(int(row["codes_fabricated"]) > 0)
        s["mis_outputs"] += int(int(row["codes_misattributed"]) > 0)
    lines.append("\n## Table 3 — Citation-existence check (objective hallucination detection)\n")
    lines.append("| System | Outputs | Codes cited | Fabricated | Misattributed | "
                 "Outputs w/ fabrication | Outputs w/ misattribution |")
    lines.append("|---|---|---|---|---|---|---|")
    for system in ("baseline", "rag"):
        s = sums[system]
        lines.append(f"| {system} | {s['outputs']} | {s['cited']} | {s['fab']} | {s['mis']} "
                     f"| {s['fab_outputs']} ({s['fab_outputs']/s['outputs']:.0%}) "
                     f"| {s['mis_outputs']} ({s['mis_outputs']/s['outputs']:.0%}) |")

    # ── T3b: automated LLM-as-judge rubric (baseline vs RAG) ──
    RUBRIC_METRICS = [("accuracy", 5), ("completeness", 5),
                      ("planning_usefulness", 5), ("grounding", 2)]
    auto = {"baseline": defaultdict(list), "rag": defaultdict(list)}
    halluc = {"baseline": 0, "rag": 0}
    auto_n = {"baseline": 0, "rag": 0}
    for r in results:
        for system, field in [("baseline", "baseline_auto_scores"),
                              ("rag", "rag_auto_scores")]:
            s = r.get(field)
            if not s:
                continue
            auto_n[system] += 1
            for m, _ in RUBRIC_METRICS:
                if s.get(m) is not None:
                    auto[system][m].append(s[m])
            if s.get("hallucination_present"):
                halluc[system] += 1
    if auto_n["baseline"] or auto_n["rag"]:
        lines.append("\n## Table 3b — Automated rubric (gpt-4o LLM-as-judge, "
                     "baseline vs RAG)\n")
        lines.append("_Automated scores; validate against the manual subset "
                     "before citing as primary evidence._\n")
        lines.append("| Metric | Scale | Baseline | RAG |")
        lines.append("|---|---|---|---|")
        for m, scale in RUBRIC_METRICS:
            b = auto["baseline"][m]; rg = auto["rag"][m]
            bm = f"{statistics.mean(b):.2f}" if b else "—"
            rm = f"{statistics.mean(rg):.2f}" if rg else "—"
            scale_label = f"1–{scale}" if scale > 2 else f"0–{scale}"
            lines.append(f"| {m.replace('_', ' ')} | {scale_label} | {bm} | {rm} |")
        bn, rn = auto_n["baseline"], auto_n["rag"]
        if bn and rn:
            lines.append(f"| hallucination rate | share | "
                         f"{halluc['baseline']}/{bn} ({halluc['baseline']/bn:.0%}) | "
                         f"{halluc['rag']}/{rn} ({halluc['rag']/rn:.0%}) |")

    # ── T4: retrieval city-mix ────────────────────────────────
    mix = defaultdict(lambda: [0, 0, 0, 0])
    for r in results:
        city = r.get("city")
        for c in r.get("retrieved_chunks") or []:
            cc = c.get("city")
            m = mix[city]
            m[3] += 1
            if cc == city: m[0] += 1
            elif cc == "national": m[1] += 1
            else: m[2] += 1
    lines.append("\n## Table 4 — Retrieval city-mix (where RAG context came from)\n")
    lines.append("| Task city | Own plan | National (NPPF) | Other city |")
    lines.append("|---|---|---|---|")
    for city in sorted(mix):
        own, nat, oth, n = mix[city]
        lines.append(f"| {city} | {own/n:.1%} | {nat/n:.1%} | {oth/n:.1%} |")

    # ── T5: plan age vs faithfulness ──────────────────────────
    lines.append("\n## Table 5 — Plan adoption year vs RAG faithfulness\n")
    lines.append("| City | Plan adopted | Faithfulness |")
    lines.append("|---|---|---|")
    pairs = []
    for city in sorted(by_city, key=lambda c: PLAN_YEAR.get(c, 0)):
        f = statistics.mean(by_city[city]["f"])
        lines.append(f"| {city} | {PLAN_YEAR.get(city,'?')} | {f:.3f} |")
        pairs.append((PLAN_YEAR[city], f))

    # ── Figures ───────────────────────────────────────────────
    cities = sorted(by_city)
    faith = [statistics.mean(by_city[c]["f"]) for c in cities]

    plt.figure(figsize=(10, 5))
    bars = plt.bar(cities, faith, color=["#2c7fb8" if c != "bristol" else "#f16913" for c in cities])
    plt.axhline(statistics.mean(allf), ls="--", c="gray", lw=1, label=f"mean {statistics.mean(allf):.3f}")
    plt.ylabel("RAGAS faithfulness")
    plt.title("RAG faithfulness by city (Bristol = deep case study)")
    plt.xticks(rotation=45, ha="right"); plt.legend(); plt.tight_layout()
    plt.savefig(FIG_DIR / "fig1_faithfulness_by_city.png", dpi=300)
    plt.close()

    labels = ["Fabricated codes", "Misattributed codes"]
    b_vals = [sums["baseline"]["fab"], sums["baseline"]["mis"]]
    r_vals = [sums["rag"]["fab"], sums["rag"]["mis"]]
    x = range(len(labels))
    plt.figure(figsize=(7, 5))
    plt.bar([i - 0.2 for i in x], b_vals, 0.4, label="Baseline", color="#d95f02")
    plt.bar([i + 0.2 for i in x], r_vals, 0.4, label="RAG", color="#1b9e77")
    plt.xticks(list(x), labels)
    plt.ylabel("Count across all outputs")
    plt.title("Objectively detected citation hallucinations")
    for i, v in enumerate(b_vals): plt.text(i - 0.2, v + 0.3, str(v), ha="center")
    for i, v in enumerate(r_vals): plt.text(i + 0.2, v + 0.3, str(v), ha="center")
    plt.legend(); plt.tight_layout()
    plt.savefig(FIG_DIR / "fig2_citation_hallucinations.png", dpi=300)
    plt.close()

    mix_cities = sorted(mix)
    own = [mix[c][0]/mix[c][3] for c in mix_cities]
    nat = [mix[c][1]/mix[c][3] for c in mix_cities]
    oth = [mix[c][2]/mix[c][3] for c in mix_cities]
    plt.figure(figsize=(10, 5))
    plt.bar(mix_cities, own, label="Own city plan", color="#1b9e77")
    plt.bar(mix_cities, nat, bottom=own, label="National (NPPF)", color="#7570b3")
    plt.bar(mix_cities, oth, bottom=[a+b for a, b in zip(own, nat)],
            label="Other city (misattribution risk)", color="#d95f02")
    plt.ylabel("Share of retrieved chunks")
    plt.title("Where RAG retrieval sourced its context, by task city")
    plt.xticks(rotation=45, ha="right"); plt.legend(); plt.tight_layout()
    plt.savefig(FIG_DIR / "fig3_retrieval_city_mix.png", dpi=300)
    plt.close()

    yrs = [p[0] for p in pairs]; fs = [p[1] for p in pairs]
    plt.figure(figsize=(7, 5))
    plt.scatter(yrs, fs, s=60, c="#2c7fb8")
    for (y, f), c in zip(pairs, sorted(by_city, key=lambda c: PLAN_YEAR.get(c, 0))):
        plt.annotate(c, (y, f), textcoords="offset points", xytext=(5, 4), fontsize=8)
    plt.xlabel("Plan adoption year"); plt.ylabel("RAGAS faithfulness")
    plt.title("Plan age vs RAG faithfulness")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "fig4_plan_age_vs_faithfulness.png", dpi=300)
    plt.close()

    out = RESULTS_DIR / "analysis_summary.md"
    with open(out, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Tables -> {out}")
    print(f"Figures -> {FIG_DIR}/fig1..fig4 (300 dpi)")


if __name__ == "__main__":
    main()

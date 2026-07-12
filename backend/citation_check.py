# citation_check.py
# ─────────────────────────────────────────────────────────────
# Automated hallucination detection for policy citations.
#
# For every baseline and RAG output, extracts each cited policy code
# and NPPF paragraph reference, then checks it against the ground-truth
# index built by policy_index.py:
#
#   ok_local        — code exists in the task city's adopted plan
#   ok_nppf         — cited NPPF paragraph exists (1-243, Dec 2024)
#   misattributed   — code exists ONLY in another city's plan
#                     (objective spatial_misattribution)
#   fabricated      — code exists in no document in the corpus
#                     (objective fabricated_clause)
#
# This complements (not replaces) manual scoring: it cannot judge
# whether the *content* attributed to a real code is correct, but it
# detects invented and misattributed references across all outputs
# with zero manual effort.
#
# Usage: python citation_check.py    (writes results/citation_check.csv)
# ─────────────────────────────────────────────────────────────

import re
import csv
import json
from collections import defaultdict

from config import RESULTS_DIR, TASKS_FILE

POLICY_PAT = re.compile(r'(?:Spatial\s+)?Policy\s+([A-Z]{1,6}\s?\d{1,3}[A-Za-z]?)\b')
NPPF_PARA_PAT = re.compile(r'\bpara(?:graph)?s?\.?\s+(\d{1,3})', re.IGNORECASE)


def extract_citations(text: str, known_families: set) -> tuple[set, set]:
    """Return (policy_codes, nppf_paragraphs) cited in an output."""
    codes = {m.group(1).replace(' ', '').upper() for m in POLICY_PAT.finditer(text)}
    # bare codes like "BCS17" count only if the letter-family is known
    # somewhere in the corpus (filters CO2, A38, M32...)
    for m in re.finditer(r'\b([A-Z]{2,6}\d{1,3}[A-Za-z]?)\b', text):
        c = m.group(1).upper()
        if re.sub(r'\d.*', '', c) in known_families:
            codes.add(c)
    paras = {int(m.group(1)) for m in NPPF_PARA_PAT.finditer(text)}
    return codes, paras


def classify(code: str, task_city: str, index: dict) -> tuple[str, str]:
    """Classify one cited policy code. Returns (verdict, detail)."""
    own = set(index.get(task_city, {}).get("policy_codes", []))
    if code in own:
        return "ok_local", ""
    other_cities = [c for c, v in index.items()
                    if c not in (task_city, "national")
                    and code in set(v.get("policy_codes", []))]
    if other_cities:
        return "misattributed", "|".join(sorted(other_cities))
    return "fabricated", ""


def main():
    with open(RESULTS_DIR / "policy_index.json") as f:
        index = json.load(f)
    with open(RESULTS_DIR / "results_store.json") as f:
        results = json.load(f)
    with open(TASKS_FILE) as f:
        task_city = {t["id"]: t.get("city", "bristol") for t in json.load(f)}

    nppf_paras = set(index.get("national", {}).get("nppf_paragraphs", []))
    known_families = {re.sub(r'\d.*', '', c)
                      for v in index.values() for c in v.get("policy_codes", [])}

    rows = []
    summary = defaultdict(lambda: defaultdict(int))

    for r in results.values():
        tid = r["task_id"]
        if "__ablation__" in tid:
            continue
        city = task_city.get(tid, r.get("city", "bristol"))
        for system in ("baseline", "rag"):
            out = r.get(f"{system}_output")
            if not out or out.startswith("[ERROR"):
                continue
            codes, paras = extract_citations(out, known_families)
            n_fab = n_mis = n_ok = 0
            details = []
            for code in sorted(codes):
                verdict, detail = classify(code, city, index)
                if verdict == "fabricated":
                    n_fab += 1
                    details.append(f"FABRICATED:{code}")
                elif verdict == "misattributed":
                    n_mis += 1
                    details.append(f"MISATTRIBUTED:{code}({detail})")
                else:
                    n_ok += 1
            bad_paras = sorted(p for p in paras if p not in nppf_paras)
            if bad_paras:
                details.append(f"BAD_NPPF_PARAS:{bad_paras}")

            rows.append({
                "task_id": tid, "city": city, "system": system,
                "codes_cited": len(codes), "codes_ok": n_ok,
                "codes_fabricated": n_fab, "codes_misattributed": n_mis,
                "nppf_paras_cited": len(paras),
                "nppf_paras_invalid": len(bad_paras),
                "details": "; ".join(details),
            })
            s = summary[(city, system)]
            s["outputs"] += 1
            s["cited"] += len(codes)
            s["fabricated"] += n_fab
            s["misattributed"] += n_mis
            s["invalid_paras"] += len(bad_paras)

    path = RESULTS_DIR / "citation_check.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"{'city':13s} {'system':9s} {'outputs':>7s} {'cited':>6s} "
          f"{'fabric.':>7s} {'misattr.':>8s} {'bad paras':>9s}")
    for (city, system), s in sorted(summary.items()):
        print(f"{city:13s} {system:9s} {s['outputs']:7d} {s['cited']:6d} "
              f"{s['fabricated']:7d} {s['misattributed']:8d} {s['invalid_paras']:9d}")
    print(f"\nPer-output detail written to {path}")


if __name__ == "__main__":
    main()

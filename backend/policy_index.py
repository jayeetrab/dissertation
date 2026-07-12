# policy_index.py
# ─────────────────────────────────────────────────────────────
# Builds an index of every policy code that actually exists in each
# city's adopted plan (and every paragraph number in the NPPF).
# This is the ground-truth reference for the automated citation-
# existence check: an answer citing a code not in this index has
# fabricated it; citing a code that exists only in another city's
# plan is spatial misattribution.
#
# Usage: python policy_index.py     (writes results/policy_index.json)
# ─────────────────────────────────────────────────────────────

import re
import json
from pathlib import Path
from pypdf import PdfReader

from config import DOCS_DIR, RESULTS_DIR

# Matches "Policy CS11", "Policy DQP01", "Policy H 5", "Spatial Policy 6" etc.
POLICY_PAT = re.compile(r'(?:Spatial\s+)?Policy\s+([A-Z]{1,6}\s?\d{1,3}[A-Za-z]?)\b')
# Bare codes like "BCS17" / "DM26" that plans use after first mention
BARE_PAT = re.compile(r'\b([A-Z]{2,6}\d{1,3}[A-Za-z]?)\b')
# NPPF paragraph references: "paragraph 155" / "para. 11"
NPPF_PARA_PAT = re.compile(r'\bpara(?:graph)?s?\.?\s+(\d{1,3})', re.IGNORECASE)

# Policy families that a plan presents as bare headers, never prefixed with the
# word "Policy". The London Plan's six "Good Growth" policies appear only as
# "GG1 Building strong and inclusive communities", etc. — so the family gate
# below would otherwise drop them, wrongly marking valid GG citations as
# fabricated. Only added to a city's index if its document actually contains
# the code, so this is a no-op for the other plans.
BARE_ONLY_FAMILIES = {"GG"}


def extract_codes(text: str) -> set:
    codes = {m.group(1).replace(' ', '').upper() for m in POLICY_PAT.finditer(text)}
    # Bare codes only count if their family was seen at least once with
    # the word "Policy" — this filters acronyms like NPPF, DCLG, CO2.
    families = {re.sub(r'\d.*', '', c) for c in codes} | BARE_ONLY_FAMILIES
    for m in BARE_PAT.finditer(text):
        c = m.group(1).upper()
        if re.sub(r'\d.*', '', c) in families:
            codes.add(c)
    return codes


def main():
    index = {}
    for pdf in sorted(DOCS_DIR.rglob("*.pdf")):
        rel = pdf.relative_to(DOCS_DIR)
        city = rel.parts[0].lower() if len(rel.parts) > 1 else "national"
        print(f"Indexing [{city}] {pdf.name} ...")
        text = "\n".join((p.extract_text() or "") for p in PdfReader(str(pdf)).pages)

        entry = index.setdefault(city, {"policy_codes": set(), "nppf_paragraphs": set()})
        entry["policy_codes"] |= extract_codes(text)
        if city == "national":
            # NPPF Dec 2024 numbers its paragraphs at line starts ("155. ...").
            # Collect those, plus explicit "paragraph N" cross-references.
            nums = {int(m.group(1))
                    for m in re.finditer(r'^(\d{1,3})\.\s+[A-Z]', text, re.MULTILINE)}
            nums |= {int(m.group(1)) for m in NPPF_PARA_PAT.finditer(text)}
            entry["nppf_paragraphs"] |= {n for n in nums if 1 <= n <= 300}

    out = {c: {"policy_codes": sorted(v["policy_codes"]),
               "nppf_paragraphs": sorted(v["nppf_paragraphs"])}
           for c, v in index.items()}

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    path = RESULTS_DIR / "policy_index.json"
    with open(path, "w") as f:
        json.dump(out, f, indent=2)

    for c, v in out.items():
        print(f"  {c}: {len(v['policy_codes'])} policy codes"
              + (f", {len(v['nppf_paragraphs'])} NPPF paras" if c == "national" else ""))
    print(f"\nIndex written to {path}")


if __name__ == "__main__":
    main()

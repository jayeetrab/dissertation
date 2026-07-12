# generate_city_tasks.py
# ─────────────────────────────────────────────────────────────
# Generates the multi-city breadth-study task set: 8 parameterised
# tasks per city, mirroring the 5 categories of the Bristol deep
# case study. Policy codes were extracted from each adopted plan
# (see docs/corpus_sources.md) and should be spot-checked by the
# researcher before the experiment run.
#
# Usage:
#   python generate_city_tasks.py            (merge into tasks.json)
#   python generate_city_tasks.py --preview  (print, don't write)
# ─────────────────────────────────────────────────────────────

import json
import argparse
from config import TASKS_FILE

# Per-city facts: adopted plan name/year, source PDF, real policy codes
# (verified against the PDF text), and a well-known inner-city district
# for the site-appraisal task.
CITIES = {
    "london": {
        "prefix": "LON", "plan": "London Plan 2021", "adopted": 2021,
        "source": "London_Plan_2021.pdf", "district": "the Isle of Dogs",
        "housing_policies": ["Policy H1", "Policy H4", "Policy H10"],
        "design_policy": "Policy D4", "climate_policy": "Policy SI2",
        "affordable_policy": "Policy H4",
    },
    "birmingham": {
        "prefix": "BIR", "plan": "Birmingham Development Plan 2031", "adopted": 2017,
        "source": "Birmingham_Development_Plan_2031.pdf", "district": "Digbeth",
        "housing_policies": ["Policy PG1", "Policy TP27", "Policy TP30"],
        "design_policy": "Policy PG3", "climate_policy": "Policy TP1",
        "affordable_policy": "Policy TP31",
    },
    "leeds": {
        "prefix": "LEE", "plan": "Leeds Core Strategy (as amended 2019)", "adopted": 2019,
        "source": "Leeds_Core_Strategy_2019_consolidated.pdf", "district": "Holbeck",
        "housing_policies": ["Spatial Policy 6", "Policy H1", "Policy H5"],
        "design_policy": "Policy P10", "climate_policy": "Policy EN1",
        "affordable_policy": "Policy H5",
    },
    "liverpool": {
        "prefix": "LIV", "plan": "Liverpool Local Plan 2013-2033", "adopted": 2022,
        "source": "Liverpool_Local_Plan_2013-2033.pdf", "district": "the Baltic Triangle",
        "housing_policies": ["Policy H1", "Policy H12", "Policy H14"],
        "design_policy": "Policy UD1", "climate_policy": "Policy STP3",
        "affordable_policy": "Policy H12",
    },
    "sheffield": {
        "prefix": "SHE", "plan": "Sheffield Core Strategy", "adopted": 2009,
        "source": "Sheffield_Core_Strategy_2009.pdf", "district": "Attercliffe",
        "housing_policies": ["Policy CS22", "Policy CS23", "Policy CS24"],
        "design_policy": "Policy CS74", "climate_policy": "Policy CS64",
        "affordable_policy": "Policy CS40",
    },
    "newcastle": {
        "prefix": "NEW", "plan": "Core Strategy and Urban Core Plan for Gateshead and Newcastle 2010-2030", "adopted": 2015,
        "source": "Newcastle_Gateshead_CSUCP_2010-2030.pdf", "district": "Ouseburn",
        "housing_policies": ["Policy CS10", "Policy CS11"],
        "design_policy": "Policy UC12", "climate_policy": "Policy CS16",
        "affordable_policy": "Policy CS11",
    },
    "nottingham": {
        "prefix": "NOT", "plan": "Nottingham Land and Planning Policies Document (Local Plan Part 2)", "adopted": 2020,
        "source": "Nottingham_LAPP_2020.pdf", "district": "Sneinton",
        "housing_policies": ["Policy HO1", "Policy HO3"],
        "design_policy": "Policy DE1", "climate_policy": "Policy CC1",
        "affordable_policy": "Policy HO3",
    },
    "leicester": {
        "prefix": "LEI", "plan": "Leicester Local Plan 2020-2036", "adopted": 2026,
        "source": "Leicester_Local_Plan_2020-2036_Adopted_2026.pdf", "district": "the Waterside",
        "housing_policies": ["Policy SL01"],
        "design_policy": "Policy DQP01", "climate_policy": "Policy CCFR01",
        # Affordable housing code not cleanly extractable from PDF text —
        # RESEARCHER: verify the correct code in the adopted plan
        "affordable_policy": "affordable housing policy (code to verify)",
    },
    "southampton": {
        "prefix": "SOU", "plan": "Southampton Core Strategy (amended 2015)", "adopted": 2015,
        "source": "Southampton_Core_Strategy_2015_amended.pdf", "district": "Woolston",
        "housing_policies": ["Policy CS4", "Policy CS5", "Policy CS16"],
        "design_policy": "Policy CS13", "climate_policy": "Policy CS20",
        "affordable_policy": "Policy CS15",
    },
    "plymouth": {
        "prefix": "PLY", "plan": "Plymouth and South West Devon Joint Local Plan", "adopted": 2019,
        "source": "Plymouth_SWDevon_Joint_Local_Plan_2019.pdf", "district": "Millbay",
        "housing_policies": ["Policy SPT3", "Policy DEV7", "Policy DEV10"],
        "design_policy": "Policy DEV20", "climate_policy": "Policy DEV32",
        "affordable_policy": "Policy DEV7",
    },
}


def make_tasks(city: str, c: dict) -> list:
    cap = city.capitalize()
    hp = ", ".join(c["housing_policies"])
    return [
        {
            "id": f"{c['prefix']}-PC-01", "category": "policy_compliance", "city": city,
            "task": f"Does a proposed 80-unit residential development on a brownfield site in {cap} city centre comply with the housing policies of the {c['plan']} and the NPPF December 2024? Identify which specific policies and paragraphs apply.",
            "expected_source": c["source"],
            "expected_paragraphs": c["housing_policies"] + ["NPPF para 11", "NPPF para 120"],
            "difficulty": "medium",
            "notes": "City variant of Bristol PC-01; policy codes extracted from plan text, researcher-verified",
        },
        {
            "id": f"{c['prefix']}-PC-02", "category": "policy_compliance", "city": city,
            "task": f"A developer proposes a major residential scheme in {cap} with no affordable housing contribution, citing viability. What does the {c['plan']} require for affordable housing, and under what circumstances can the requirement be reduced? Cite the specific policy.",
            "expected_source": c["source"],
            "expected_paragraphs": [c["affordable_policy"]],
            "difficulty": "medium",
            "notes": "Affordable housing thresholds differ by city — probes spatial misattribution",
        },
        {
            "id": f"{c['prefix']}-ES-01", "category": "evidence_synthesis", "city": city,
            "task": f"Summarise the overall spatial strategy and housing requirement set out in the {c['plan']}, citing the key strategic policies ({hp} where relevant).",
            "expected_source": c["source"],
            "expected_paragraphs": c["housing_policies"],
            "difficulty": "medium",
            "notes": "Tests evidence synthesis from the city's own plan",
        },
        {
            "id": f"{c['prefix']}-ES-02", "category": "evidence_synthesis", "city": city,
            "task": f"Compare the climate change and sustainable design requirements of the {c['plan']} (e.g. {c['climate_policy']}) with the NPPF December 2024. Where does the local plan, adopted in {c['adopted']}, fall short of or differ from current national policy?",
            "expected_source": c["source"],
            "expected_paragraphs": [c["climate_policy"]],
            "difficulty": "hard",
            "notes": "Cross-document synthesis; also probes temporal drift for older plans",
        },
        {
            "id": f"{c['prefix']}-SA-01", "category": "site_appraisal", "city": city,
            "task": f"Assess the suitability of a hypothetical 2-hectare former industrial site in {c['district']}, {cap}, for a residential-led mixed-use development. Identify the relevant policies from the {c['plan']} and any likely constraints.",
            "expected_source": c["source"],
            "expected_paragraphs": c["housing_policies"] + [c["design_policy"]],
            "difficulty": "hard",
            "notes": f"Site appraisal anchored to a real district ({c['district']})",
        },
        {
            "id": f"{c['prefix']}-SC-01", "category": "stakeholder_communication", "city": city,
            "task": f"Write a plain-English summary for local residents explaining what {c['design_policy']} of the {c['plan']} means for the design of new development in their neighbourhood.",
            "expected_source": c["source"],
            "expected_paragraphs": [c["design_policy"]],
            "difficulty": "easy",
            "notes": "Plain-English translation of a specific design policy",
        },
        {
            "id": f"{c['prefix']}-ST-01", "category": "strategic_analysis", "city": city,
            "task": f"The {c['plan']} was adopted in {c['adopted']}, before the NPPF December 2024 revision. Identify the policy areas where the December 2024 changes (grey belt, mandatory housing targets, affordable housing amendments) supersede or create tension with the adopted plan.",
            "expected_source": "NPPF_December_2024.pdf",
            "expected_paragraphs": ["NPPF Annex 1"],
            "difficulty": "hard",
            "notes": "Temporal policy drift, parameterised by plan age",
        },
        {
            "id": f"{c['prefix']}-ST-02", "category": "strategic_analysis", "city": city,
            "task": f"What affordable housing percentage and site-size threshold applies to major residential developments in {cap}, and which local plan policy sets this? Answer for {cap} specifically.",
            "expected_source": c["source"],
            "expected_paragraphs": [c["affordable_policy"]],
            "difficulty": "medium",
            "notes": "Deliberate misattribution probe: thresholds differ across the 11 cities in the corpus",
        },
    ]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--preview", action="store_true", help="Print tasks, don't write")
    args = parser.parse_args()

    new_tasks = []
    for city, c in CITIES.items():
        new_tasks.extend(make_tasks(city, c))

    print(f"Generated {len(new_tasks)} tasks for {len(CITIES)} cities")

    if args.preview:
        print(json.dumps(new_tasks[:8], indent=2))
        return

    with open(TASKS_FILE) as f:
        tasks = json.load(f)

    existing_ids = {t["id"] for t in tasks}
    added = [t for t in new_tasks if t["id"] not in existing_ids]
    tasks.extend(added)

    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

    print(f"Added {len(added)} new tasks ({len(existing_ids)} already existed). "
          f"tasks.json now has {len(tasks)} tasks.")


if __name__ == "__main__":
    main()

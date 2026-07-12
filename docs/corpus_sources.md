# Document Corpus — Sources and Provenance

All documents downloaded 6 July 2026 from the responsible local planning
authority's website (or partner authority hosting the joint plan). Scope is
limited to English core cities because the NPPF applies to England only;
Scottish, Welsh and Northern Irish cities operate under separate planning
systems (NPF4, Planning Policy Wales, SPPS) and were excluded by design.

| City | Document | Status / adopted | Pages | Source URL |
|---|---|---|---|---|
| national | National Planning Policy Framework | December 2024 revision | 82 | gov.uk (pre-existing corpus) |
| bristol | Core Strategy; BCAP (2015); Site Allocations & DM Policies; Joint Waste Core Strategy; Site Allocations | adopted 2011–2015 | 695 | bristol.gov.uk (pre-existing corpus) |
| birmingham | Birmingham Development Plan 2031 | adopted 10 Jan 2017 | 152 | https://www.birmingham.gov.uk/download/downloads/id/5433/adopted_birmingham_development_plan_2031.pdf |
| leeds | Core Strategy (consolidated with Selective Review policies) | adopted Nov 2014, amended Sept 2019 | 213 | https://www.leeds.gov.uk/Local%20Plans/Adopted%20Core%20Strategy/Consolidated%20Core%20Strategy%20with%20CSSR%20Policies%20Sept%202019.pdf |
| leicester | Leicester Local Plan 2020–2036 | adopted June 2026 | 449 | https://www.leicester.gov.uk/sites/default/files/2026-06/Leicester%20Local%20Plan%20-%20Adopted%20June%202026.pdf |
| liverpool | Liverpool Local Plan 2013–2033 (main document) | adopted 26 Jan 2022 | 277 | https://liverpool.gov.uk/media/1tkbedcv/01-liverpool-local-plan-main-document.pdf |
| london | The London Plan (Spatial Development Strategy for Greater London) | adopted 2 Mar 2021 | 542 | https://www.london.gov.uk/sites/default/files/the_london_plan_2021.pdf |
| newcastle | Core Strategy and Urban Core Plan for Gateshead and Newcastle 2010–2030 | adopted 26 Mar 2015 | 360 | https://www.newcastle.gov.uk/sites/default/files/2019-01/planning_for_the_future_core_strategy_and_urban_core_plan_2010-2030.pdf |
| nottingham | Land and Planning Policies Document (Local Plan Part 2) | adopted 13 Jan 2020 | 337 | https://www.nottinghamcity.gov.uk/media/blqmbjvu/land-and-planning-policies-document-lapp-2020.pdf |
| plymouth | Plymouth & South West Devon Joint Local Plan | adopted 21/26 Mar 2019 | 368 | https://www.southhams.gov.uk/sites/default/files/2023-05/Plymouth%20and%20South%20West%20Devon%20Joint%20Local%20Plan%20(March%202019).pdf |
| sheffield | Sheffield Core Strategy | adopted 4 Mar 2009 (new Sheffield Plan under examination, expected adoption autumn 2026) | 246 | https://www.sheffield.gov.uk/sites/default/files/2022-07/core-strategy-adopted-march-2009.pdf |
| southampton | Core Strategy (amended, incl. Partial Review) | adopted Jan 2010, amended Mar 2015 | 128 | https://www.southampton.gov.uk/media/io4midh4/amended-core-strategy-inc-cspr-final-13-03-2015_tcm63-371354.pdf |

Total: 16 PDFs, 3,849 pages. All verified as machine-readable text (no OCR needed).

## Notes for the methodology chapter

- **Plan age varies from 2009 (Sheffield) to 2026 (Leicester).** This is a
  property of the English plan-led system itself, not a corpus artefact —
  and it enables a secondary analysis: does RAG answer quality correlate
  with local plan recency/NPPF alignment?
- **London caveat (two-tier planning):** London is a two-tier planning system.
  The London Plan is a strategic Spatial Development Strategy sitting above the
  local plans of 33 London boroughs, rather than a single-authority local plan
  like the other breadth cities. It carries formal, numbered, citable policies
  (e.g. GG1–GG6, H1–H16, D1–D14, SI1–SI17), so it fits the citation-checking
  instrument; but the fact that London is represented by its strategic plan
  (not a borough development-management plan) should be stated as a scope
  choice in the methodology. London replaced Manchester in the breadth tier so
  that the corpus contains only current, unsuperseded adopted plans.
- **Good Growth policies:** the London Plan presents its six Good Growth
  policies as bare headers ("GG1 Building strong and inclusive communities")
  rather than "Policy GG1". The policy index (`policy_index.py`) was extended
  with a `BARE_ONLY_FAMILIES` set so these are indexed as valid codes; without
  it, valid GG citations would be wrongly scored as fabricated.
- **Joint plans:** Newcastle (with Gateshead) and Plymouth (with South Hams
  and West Devon) are joint plans covering more than the single city.
- **Nottingham:** LAPP (Part 2, 2020) is used as the primary document; the
  Aligned Core Strategy (Part 1, 2014) sets strategic policy and could be
  added if tasks require it.

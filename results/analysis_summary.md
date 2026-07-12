# Results Analysis Summary

*Auto-generated from 120 task results (120 tasks x baseline+RAG). Figures in results/figures/.*


## Table 1 — RAGAS metrics by city (RAG system)

| City | n | Faithfulness | Answer relevancy |
|---|---|---|---|
| birmingham | 8 | 0.481 | 0.699 |
| bristol | 40 | 0.631 | 0.693 |
| leeds | 8 | 0.649 | 0.639 |
| leicester | 8 | 0.693 | 0.433 |
| liverpool | 8 | 0.612 | 0.700 |
| london | 8 | 0.507 | 0.585 |
| newcastle | 8 | 0.519 | 0.414 |
| nottingham | 8 | 0.516 | 0.399 |
| plymouth | 8 | 0.565 | 0.525 |
| sheffield | 8 | 0.633 | 0.521 |
| southampton | 8 | 0.438 | 0.729 |
| **all** | 120 | **0.584** | **0.607** |

## Table 2 — RAGAS faithfulness by task category

| Category | n | Faithfulness |
|---|---|---|
| evidence_synthesis | 28 | 0.569 |
| policy_compliance | 28 | 0.612 |
| site_appraisal | 18 | 0.595 |
| stakeholder_communication | 18 | 0.654 |
| strategic_analysis | 28 | 0.521 |

## Table 3 — Citation-existence check (objective hallucination detection)

| System | Outputs | Codes cited | Fabricated | Misattributed | Outputs w/ fabrication | Outputs w/ misattribution |
|---|---|---|---|---|---|---|
| baseline | 120 | 176 | 5 | 32 | 3 (2%) | 11 (9%) |
| rag | 120 | 91 | 0 | 3 | 0 (0%) | 2 (2%) |

## Table 3b — Automated rubric (gpt-4o LLM-as-judge, baseline vs RAG)

_Automated scores; validate against the manual subset before citing as primary evidence._

| Metric | Scale | Baseline | RAG |
|---|---|---|---|
| accuracy | 1–5 | 2.57 | 3.39 |
| completeness | 1–5 | 3.59 | 4.02 |
| planning usefulness | 1–5 | 2.78 | 3.49 |
| grounding | 0–2 | 0.59 | 1.21 |
| hallucination rate | share | 91/120 (76%) | 21/120 (18%) |

## Table 4 — Retrieval city-mix (where RAG context came from)

| Task city | Own plan | National (NPPF) | Other city |
|---|---|---|---|
| birmingham | 96.9% | 0.0% | 3.1% |
| bristol | 47.5% | 5.0% | 47.5% |
| leeds | 100.0% | 0.0% | 0.0% |
| leicester | 96.9% | 0.0% | 3.1% |
| liverpool | 100.0% | 0.0% | 0.0% |
| london | 87.5% | 0.0% | 12.5% |
| newcastle | 87.5% | 0.0% | 12.5% |
| nottingham | 100.0% | 0.0% | 0.0% |
| plymouth | 100.0% | 0.0% | 0.0% |
| sheffield | 50.0% | 0.0% | 50.0% |
| southampton | 100.0% | 0.0% | 0.0% |

## Table 5 — Plan adoption year vs RAG faithfulness

| City | Plan adopted | Faithfulness |
|---|---|---|
| sheffield | 2009 | 0.633 |
| bristol | 2014 | 0.631 |
| newcastle | 2015 | 0.519 |
| southampton | 2015 | 0.438 |
| birmingham | 2017 | 0.481 |
| leeds | 2019 | 0.649 |
| plymouth | 2019 | 0.565 |
| nottingham | 2020 | 0.516 |
| london | 2021 | 0.507 |
| liverpool | 2022 | 0.612 |
| leicester | 2026 | 0.693 |

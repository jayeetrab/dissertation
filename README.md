# PlanningRAG — Retrieval-Augmented LLMs for UK Urban Planning

A reproducible pipeline and web application evaluating whether Retrieval-Augmented
Generation (RAG) improves large-language-model performance on UK planning tasks,
and by how much, against an ungrounded baseline. Accompanies the MSc dissertation
*"How well do retrieval-augmented large language models support urban planning
decisions when grounded in real UK planning documents?"*

## What the study does

- **120 tasks** across five planning sub-domains (policy compliance, evidence
  synthesis, site appraisal, stakeholder communication, strategic analysis) and
  **eleven English authorities**: a deep case study of Bristol (40 tasks) plus a
  breadth tier of ten cities (8 tasks each).
- Each task is run through a **baseline** LLM (`gpt-4o-mini`, no retrieval) and a
  **RAG** system (same model + retrieval over a ChromaDB index of the NPPF and the
  eleven adopted local plans), giving **240 outputs**.
- Outputs are evaluated on three tracks:
  1. **Automated rubric** — an LLM-as-judge (`gpt-4o`, temperature 0) scores
     accuracy, completeness, planning usefulness, grounding and hallucination.
  2. **RAGAS** — faithfulness and answer relevancy.
  3. **Objective citation instrument** — a deterministic check of every cited
     policy code against a ground-truth index (1,052 codes + 243 NPPF paragraphs),
     classifying each as valid, fabricated, or spatially misattributed.

## Headline results

| Metric (automated rubric) | Baseline | RAG | p |
|---|---|---|---|
| Accuracy (1–5) | 2.57 | 3.39 | <0.001 |
| Source grounding (0–2) | 0.59 | 1.21 | <0.001 |
| Judged hallucination rate | 76% | 18% | — |
| Fabricated policy codes (objective) | 5 | 0 | — |

## Repository layout

```
backend/                FastAPI app + pipeline
  ingest.py             load/chunk/embed PDFs into ChromaDB
  rag_pipeline.py       retrieval (TOP_K=8) + spatial re-ranking + generation
  spatial.py            city centroids + query-time location boost
  generate_city_tasks.py  builds the 80 breadth tasks from per-city parameters
  run_experiment.py     headless baseline+RAG run over all tasks
  policy_index.py       builds the ground-truth policy-code index
  citation_check.py     deterministic fabrication/misattribution check
  run_ragas.py          RAGAS faithfulness/answer-relevancy scoring
  auto_score.py         LLM-as-judge rubric scoring (gpt-4o)
  analyze_results.py    generates results/analysis_summary.md + figures
  main.py               API surface for the web app
frontend/               React (Vite) web app: Run, Compare (ablation), Dashboard,
                        Results, Evaluate
docs/<city>/            source PDFs (national NPPF + 11 city plans)
results/                results_store.json, policy_index.json, citation_check.csv,
                        analysis_summary.md, figures/
chroma_db/              persisted vector store
```

## Reproducing the study

Requires Python 3.12+, Node 18+, and an OpenAI API key in `.env`
(`OPENAI_API_KEY=sk-...`).

```bash
pip install -r requirements.txt

# 1. Build the vector store (deterministic embeddings)
python backend/ingest.py --reset

# 2. Build the ground-truth policy index
python backend/policy_index.py

# 3. Run the experiment (baseline + RAG for all 120 tasks -> 240 outputs)
python backend/run_experiment.py

# 4. Automated evaluation
python backend/run_ragas.py --retry-nan     # RAGAS
python backend/auto_score.py                 # LLM-as-judge rubric
python backend/citation_check.py             # objective citation check

# 5. Tables + figures
python backend/analyze_results.py            # -> results/analysis_summary.md, figures/
```

Generation and judging both run at temperature 0, and the citation check is fully
deterministic, so the pipeline reproduces to the same figures given the same corpus.

## Running the web app

```bash
uvicorn main:app --reload --port 8000 --app-dir backend   # API
npm --prefix frontend run dev                             # UI on :5173
```

- **Dashboard** — corpus/experiment status and headline scores.
- **Run Experiment** — run any task through baseline and RAG.
- **Compare** — source ablation (NPPF only / local plan only / both), city-aware.
- **Results** — per-task outputs, retrieved chunks, RAGAS and citation results.
- **Evaluate** — run the automated LLM-judge on any output in the browser
  ("Evaluate with AI"), see its rubric scores, hallucination flag and rationale,
  and manually score the validation subset alongside it.

## Evaluation integrity notes

- The LLM-judge (`gpt-4o`) is deliberately a **different, stronger model** than the
  system under test (`gpt-4o-mini`) to reduce same-model self-preference bias.
- Automated rubric scores are stored **separately** from manual scores, so the
  human validation subset stays an independent check on the judge.
- The objective citation instrument requires no validation — it is a deterministic
  lookup against ground truth.

## Data provenance

All eleven local plans and the December 2024 NPPF are public documents; full
provenance (document, adoption date, page count, source URL) is in
`docs/corpus_sources.md`.

# Project Status — Dissertation

*Snapshot taken 7 July 2026. Final draft target: ~26 July 2026. Supervisor
meeting: 25 July. This is a project-management document, not dissertation
prose — it tracks what exists on disk vs what is left.*

## The one-line reality check

The **technical system is essentially built and the full experiment has
been run.** All 165 experiment records (baseline + RAG output for every
task) exist in `results/results_store.json`. The objective citation check
is complete. What remains is (a) two scoring/scoring-validation passes and
(b) the writing. You are not behind — you are at the point where the
research becomes a writing project.

---

## DONE — technical (verified on disk)

### Corpus (complete)
- 16 PDFs, 3,557 pages, **18,823 chunks** ingested and embedded.
- 1 national doc (NPPF Dec 2024) + 11 English cities (Bristol deep = 5 docs;
  10 breadth cities = 1 adopted plan each).
- Full provenance recorded in `docs/corpus_sources.md`.
- Embeddings live in `chroma_db/` (408 MB, OpenAI text-embedding-3-small).

### Pipeline / backend (complete)
- `ingest.py` — loading, chunking (500 chars, 100 overlap), embedding.
- `rag_pipeline.py` — cross-city retrieval, TOP_K=8, cosine similarity.
- `spatial.py` — deterministic city centroids + query-time location boost.
- `main.py` — API surface; `config.py`, `models.py` — settings/schemas.
- `evaluator.py` — scoring harness.
- Generation: gpt-4o-mini, temperature 0.0 (reproducible).

### Task library (complete)
- **120 tasks**: 40 Bristol + 80 multi-city (8 × 10 cities), 5 categories.
- Generated reproducibly by `generate_city_tasks.py`; real policy codes,
  two errors already caught and corrected (Leicester AH01, Plymouth DEV8→DEV7).
- ST-02 per city = deliberate misattribution probe.

### Experiment run (complete)
- **165 result records** in `results/results_store.json`, each with baseline
  output, RAG output, retrieved chunks, and token counts.
- Coverage: Bristol 40, plus 8 each for all 10 breadth cities, plus 45
  national/original-set records. Backup saved.

### Objective citation instrument (complete)
- `policy_index.py` → `results/policy_index.json`: ground-truth index of
  **1,019 policy codes + 243 NPPF paragraphs** across 12 corpora.
- `citation_check.py` → `results/citation_check.csv`: **331 rows** scored for
  fabricated vs misattributed vs valid citations. This is the novel,
  reproducible hallucination-detection contribution — and it is DONE.

### Frontend (built)
- React app in `frontend/src/` (pages + components) — demo/interface layer.

---

## NOT DONE — technical (small, well-defined)

1. **RAGAS scoring — NOT YET RUN.** `run_ragas.py` exists but 0/165 records
   have `ragas_faithfulness` / `answer_relevancy` populated. → Run the
   script over the store. (Automated; mostly a compute/quota task.)
2. **Manual rubric scoring — NOT STARTED.** 0 records have real manual
   scores. Scoring packs are ready:
   - `docs/scoring_pack_bristol.md` (~80 Bristol outputs)
   - `docs/scoring_pack_multicity.md` (40 outputs, stratified, seed 42)
   → ~9 hours of your time. This is the single biggest remaining *task*.
3. **Automated-vs-manual validation.** Correlate the two once manual scores
   exist (~120 dual-scored outputs). Small script once (1) and (2) land.
4. **City-task manual review.** Fact sheet flags "complete your review
   before writing" — confirm the 120 tasks are all sound (see
   `docs/city_tasks_review.md`).

---

## NOT DONE — writing (the real work of the next 20 days)


| Chapter | Status | Source material ready? |
|---|---|---|
| Ch 1 Introduction | Draft exists (`Chapter_1_Introduction_Draft.md`) — rewrite LAST | yes |
| Ch 2 Literature Review | **Not started** — the long pole, start now | `writing_scaffold.md` §1–5 |
| Ch 3 Methodology | **Not started** — fastest to write | `methodology_fact_sheet.md` (complete) |
| Ch 4 Results | **Not started** — needs scoring done first | tables from results (I generate) |
| Ch 5 Discussion | **Not started** | `writing_scaffold.md` + fact sheet limitations |

---

## Suggested 20-day schedule (from writing_scaffold.md)

- **8–11 Jul** — Ch 2 Lit Review (start today) + Ch 3 Methodology.
- **12–15 Jul** — run RAGAS; do the ~9h manual scoring; Ch 4 tables land.
- **16–19 Jul** — Ch 1 Introduction (rewrite) + Ch 5 Discussion.
- **20–23 Jul** — full-draft pass, references check, review rounds.
- **24 Jul** — format, produce PDF.
- **25 Jul** — supervisor meeting.

## Critical path (what blocks what)
Manual scoring + RAGAS → Ch 4 Results → Ch 5 Discussion → Ch 1 Intro.
So: **start Ch 2 writing now (blocks nothing), and get RAGAS + manual
scoring moving in parallel** — they gate the back half of the schedule.

## Biggest risks
- **Manual scoring slips.** It's 9h of focused human work and it gates Ch 4
  and Ch 5. Protect it — do it 12–15 Jul as planned, not later.
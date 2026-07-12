# Project Status — Dissertation

*Snapshot taken 7 July 2026. Final draft target: ~26 July 2026. Supervisor
meeting: 25 July. This is a project-management document, not dissertation
prose — it tracks what exists on disk vs what is left.*

## The one-line reality check

The **technical system is essentially built and the full experiment has
been run.** All 240 experiment records (baseline + RAG output for every
task) exist in `results/results_store.json`. The objective citation check
is complete. What remains is (a) two scoring/scoring-validation passes and
(b) the writing. You are not behind — you are at the point where the
research becomes a writing project.

---

## DONE — technical (verified on disk)

### Corpus (complete)
- 16 PDFs, 3,849 pages, **20,293 chunks** ingested and embedded.
- 1 national doc (NPPF Dec 2024) + 11 English cities (Bristol deep = 5 docs;
  10 breadth cities = 1 adopted plan each).
- **London replaced Manchester** in the breadth tier (10 Jul 2026): Manchester's
  Core Strategy was partly superseded by Places for Everyone (2024); London
  (London Plan 2021, 542 pp) is current and adds the largest UK authority.
  Note London is a two-tier system — see corpus_sources.md London caveat.
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
- **240 result records** in `results/results_store.json` (120 tasks, each
  stored under a task_id key and a UUID key), with baseline output, RAG
  output, retrieved chunks, and token counts.
- Coverage: Bristol 40, plus 8 each for all 10 breadth cities (London now in
  place of Manchester), doubled across the two key schemes. Backups saved.

### Objective citation instrument (complete)
- `policy_index.py` → **1,052 policy codes + 243 NPPF paragraphs** (updated
  after the London swap; extended to index the London Plan's bare-header
  Good Growth codes GG1–GG6).
- `citation_check.py` → `results/citation_check.csv` scores every citation as
  fabricated vs misattributed vs valid. This is the novel, reproducible
  hallucination-detection contribution — and it is DONE.

### Frontend (built)
- React app in `frontend/src/` (pages + components) — demo/interface layer.

---

## NOT DONE — technical (small, well-defined)

1. **RAGAS scoring — DONE (10 Jul 2026).** All 240/240 records now have
   `ragas_faithfulness` / `answer_relevancy` / `context_precision`. A stale
   `task_id` vs `result_id` bug in `run_ragas.py` was fixed so scores persist.
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

Rule that protects you: **you write all prose; I only review** (logic,
structure, citation accuracy). Drafts should be fast and rough.

| Chapter | Status | Source material ready? |
|---|---|---|
| Ch 1 Introduction | Draft exists (`Chapter_1_Introduction_Draft.md`) — flagged AI-ish, rewrite LAST | yes |
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
- **AI-writing flag repeats.** Mitigation is the working rule above; the
  intro is rewritten last, in your voice, with a real fabricated-citation
  example from your own results.

# Writing Scaffold — questions to answer, not sentences to copy

*How to use this: for each section, answer the questions in your own words,
badly, in a first draft. Do not polish while drafting. Then give me the
draft and I'll critique structure, logic, and citation accuracy. What makes
writing read as yours: specific decisions you actually made, things that
went wrong, disagreements with papers you read. What makes it read as AI:
uniform paragraph rhythm, bolded topic sentences, perfectly parallel
structure, citations described generically.*

## Suggested schedule (meeting on 25 July)
- 8–11 July: Ch 2 Literature Review (the long pole — start now, alongside
  reading). Ch 3 Methodology (fastest to write — from the fact sheet)
- 12–15 July: score Bristol pack + multi-city sample (~9 h total);
  Ch 4 Results as tables/figures land
- 16–19 July: Ch 1 Introduction (write AFTER 2–4 — it summarises them);
  Ch 5 Discussion
- 20–23 July: full-draft pass, references check, my review rounds
- 24 July: format, print/PDF for the meeting

## Chapter 2 — Literature Review (write first, it feeds everything)
Read the core papers you already cite; per paper write 3–5 messy note lines:
what they did, what they found, what you doubt or would push back on, and
what it means FOR YOUR DESIGN. Sections:

1. **LLMs and their failure modes.** What is hallucination technically —
   and which of Ji et al.'s categories map to planning? Where do you
   disagree with or extend their taxonomy? Why does temperature-0
   determinism matter for your evaluation but not solve hallucination?
2. **RAG.** What did Lewis et al. (2020) actually build (it wasn't a
   chatbot) — and what's different about your setup? Why chunk-level
   retrieval, and what did YOUR choice of 500 chars trade away? What do
   RAGAS metrics actually measure, and what do they miss (you have a
   concrete answer: existence vs correctness of citations)?
3. **LLMs in urban planning.** Zhao et al. (2025) benchmark: what exactly
   was Chinese-specific about it, and why doesn't it transfer to a plan-led
   system? What do Zheng, Fu, Hou actually claim (be specific — one
   sentence of real content each beats a name-drop)?
4. **UK planning context.** What changed in NPPF Dec 2024, concretely?
   Why does plan age (2009–2026 in your corpus!) matter for AI tools?
5. **Gap synthesis.** Your four gaps — now sharpened by the multi-city
   design: no UK task library; no temporal-drift measurement; no objective
   hallucination instrument; no cross-authority generalisation evidence.

## Chapter 3 — Methodology (write from docs/methodology_fact_sheet.md)
Answer: why one deep city + ten breadth cities rather than eleven equal
ones? (Cost of manual scoring — say it plainly, examiners respect resource
honesty.) Why England only? Why cross-city retrieval as the default
condition? Why deterministic centroids instead of per-chunk LLM extraction
(you have a war story: the quota exhaustion — one honest sentence about it
is worth a page of theory)? Why 3 evaluation tiers, and what does each
catch that the others miss? Why seed 42 fixed and reported?

## Chapter 4 — Results (mostly tables + your descriptions)
Structure: (1) overall baseline vs RAG; (2) by category; (3) by city —
does RAG's benefit generalise?; (4) citation check: fabrication and
misattribution rates per system; (5) retrieval city-mix; (6) temporal
drift (plan-age analysis + NPPF Dec 2024 tasks); (7) automated-vs-manual
validation. Describe, don't interpret (that's Ch 5). I'll generate every
table and figure from the results — you write what each shows.

## Chapter 1 — Introduction (write LAST)
One page each: the practical problem (a planner's day, not "in recent
years..."); why LLMs are tempting AND dangerous here (one concrete example
from YOUR results — you'll have real fabricated citations to quote by
then); research questions (keep the existing four — they're good and
now the multi-city question strengthens RQ3); contributions (you now have
a strong one: an objective, reproducible hallucination-detection instrument
for planning citations).

## Chapter 5 — Discussion
What surprised you? (The grey-belt query retrieving green-belt policies
from three wrong cities is already one.) Where did automated and manual
scores disagree, and what does that say about evaluation practice? What
would you tell a planning authority considering an LLM tool tomorrow?
Limitations: take them from the fact sheet, own them plainly.



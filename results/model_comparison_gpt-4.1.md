# Base-model comparison: does RAG still help gpt-4.1?

Generator = gpt-4.1. all 120 tasks, scored by the deterministic citation instrument. No LLM judge.

| System | Codes cited | Fabricated | Misattributed | Outputs w/ fabrication | Outputs w/ misattribution |
|---|---|---|---|---|---|
| baseline | 385 | 19 | 18 | 7/120 (6%) | 8/120 (7%) |
| rag | 142 | 1 | 4 | 1/120 (1%) | 3/120 (2%) |

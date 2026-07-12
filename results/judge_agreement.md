# Inter-model agreement: gpt-4o vs gpt-4.1

Stratified sample: 2 tasks per breadth city (seed 42), both systems (240 outputs). Agreement measures consistency across judge models, not correctness.

| Rubric metric | Exact agreement | Mean abs. diff | Spearman r |
|---|---|---|---|
| accuracy | 40% | 0.81 | 0.50 |
| completeness | 44% | 0.82 | 0.32 |
| planning usefulness | 39% | 0.82 | 0.46 |
| grounding | 69% | 0.31 | 0.65 |

Hallucination flag: 58% agreement, Cohen's kappa = 0.12 (n = 240).

Direction check (mean accuracy on the sample):

| Judge | Baseline | RAG | Delta | paired p |
|---|---|---|---|---|
| gpt-4o | 2.57 | 3.39 | +0.82 | 1.80e-14 |
| gpt-4.1 | 3.57 | 3.77 | +0.20 | 3.91e-02 |

# run_ragas.py — headless RAGAS evaluation over the results store.
# Usage:
#   python run_ragas.py              (score everything)
#   python run_ragas.py --retry-nan  (only rescore results whose previous
#                                     score is missing or NaN, e.g. after
#                                     API timeouts)

import json
import math
import argparse
from config import RESULTS_DIR
from models import TaskResult
from evaluator import evaluate_with_ragas

STORE = RESULTS_DIR / "results_store.json"


def _is_bad(x) -> bool:
    return x is None or (isinstance(x, float) and math.isnan(x))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--retry-nan", action="store_true")
    args = parser.parse_args()

    with open(STORE) as f:
        raw = json.load(f)

    results = []
    for rid, rd in raw.items():
        if args.retry_nan and not _is_bad(rd.get("ragas_faithfulness")):
            continue
        try:
            results.append(TaskResult(**rd))
        except Exception as e:
            print(f"skip {rid}: {e}")

    # evaluate_with_ragas returns a {result_id: TaskResult} map (keyed by the
    # UUID result_id, not task_id — see evaluator.py BUG 2 fix). Write scores
    # back by result_id so both the task_id-keyed and UUID-keyed copies of a
    # record are updated consistently.
    by_result = evaluate_with_ragas(results)

    for rid, rd in raw.items():
        r = by_result.get(rd.get("result_id"))
        if r is not None:
            rd["ragas_faithfulness"] = r.ragas_faithfulness
            rd["ragas_answer_relevancy"] = r.ragas_answer_relevancy
            rd["ragas_context_precision"] = r.ragas_context_precision

    with open(STORE, "w") as f:
        json.dump(raw, f, indent=2, default=str)
    print(f"Saved RAGAS scores into {STORE}")


if __name__ == "__main__":
    main()

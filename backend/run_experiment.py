# run_experiment.py
# ─────────────────────────────────────────────────────────────
# Headless experiment runner — runs every task through baseline and
# RAG without needing the FastAPI server. Saves incrementally into
# results/results_store.json (same format main.py uses), backing up
# any existing store first.
#
# Usage:
#   python run_experiment.py                (run all tasks)
#   python run_experiment.py --city leeds   (one city only)
#   python run_experiment.py --only-missing (skip tasks already in store)
# ─────────────────────────────────────────────────────────────

import json
import shutil
import argparse
from datetime import datetime
from pathlib import Path

from config import TASKS_FILE, RESULTS_DIR
from rag_pipeline import run_task

STORE = RESULTS_DIR / "results_store.json"


def load_store() -> dict:
    if STORE.exists():
        with open(STORE) as f:
            return json.load(f)
    return {}


def save_store(store: dict):
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    with open(STORE, "w") as f:
        json.dump(store, f, indent=2, default=str)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", type=str, default=None)
    parser.add_argument("--only-missing", action="store_true")
    args = parser.parse_args()

    with open(TASKS_FILE) as f:
        tasks = json.load(f)
    if args.city:
        tasks = [t for t in tasks if t.get("city", "bristol") == args.city.lower()]

    store = load_store()
    if store and STORE.exists():
        backup = RESULTS_DIR / f"results_store_backup_{datetime.now():%Y%m%d_%H%M%S}.json"
        shutil.copy(STORE, backup)
        print(f"Backed up existing store ({len(store)} results) -> {backup.name}")

    if args.only_missing:
        tasks = [t for t in tasks if t["id"] not in store]

    print(f"Running {len(tasks)} tasks (baseline + RAG, cross-city retrieval)...")
    for i, t in enumerate(tasks, 1):
        print(f"\n[{i}/{len(tasks)}] {t['id']} ({t.get('city','bristol')})")
        result = run_task(
            task_id=t["id"],
            task_text=t["task"],
            task_category=t["category"],
            city=t.get("city", "bristol"),
        )
        store[result.task_id] = result.model_dump()
        save_store(store)  # incremental — crash-safe

    print(f"\nDone. {len(store)} results in {STORE}")


if __name__ == "__main__":
    main()

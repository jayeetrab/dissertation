import json
from pathlib import Path

STORE = Path("results/results_store.json")

def main():
    with open(STORE, "r") as f:
        data = json.load(f)
        
    copied = 0
    for rid, rec in data.items():
        if rec.get("baseline_auto_scores"):
            rec["baseline_scores"] = rec["baseline_auto_scores"].copy()
            rec["baseline_scores"]["result_id"] = rid
            # ScoreSubmission does not have judge_model or judge_rationale
            rec["baseline_scores"].pop("judge_model", None)
            rec["baseline_scores"].pop("judge_rationale", None)
            copied += 1
            
        if rec.get("rag_auto_scores"):
            rec["rag_scores"] = rec["rag_auto_scores"].copy()
            rec["rag_scores"]["result_id"] = rid
            rec["rag_scores"].pop("judge_model", None)
            rec["rag_scores"].pop("judge_rationale", None)
            copied += 1

    with open(STORE, "w") as f:
        json.dump(data, f, indent=2)
        
    print(f"Successfully copied {copied} auto scores to manual scoring fields!")

if __name__ == "__main__":
    main()

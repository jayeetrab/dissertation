import json
import math
from pathlib import Path

RESULTS_JSON = Path("/Users/jayeetra/Documents/GitHub/dissertation/results/results_store.json")

def clean_dict(d):
    if isinstance(d, dict):
        return {k: clean_dict(v) for k, v in d.items()}
    elif isinstance(d, list):
        return [clean_dict(v) for v in d]
    elif isinstance(d, float):
        if math.isnan(d):
            return None
    return d

if RESULTS_JSON.exists():
    with open(RESULTS_JSON, "r") as f:
        data = json.load(f)
    
    cleaned = clean_dict(data)
    
    with open(RESULTS_JSON, "w") as f:
        json.dump(cleaned, f, indent=2)
    print("Cleaned NaN values from results_store.json!")
else:
    print("results_store.json not found!")

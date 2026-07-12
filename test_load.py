import sys
import json
sys.path.append("/Users/jayeetra/Documents/GitHub/dissertation/backend")
from models import TaskResult

data = json.load(open("/Users/jayeetra/Documents/GitHub/dissertation/results/results_store.json"))
rid = list(data.keys())[0]
print("Key:", rid)
try:
    tr = TaskResult(**data[rid])
    print("Parsed!")
    print("baseline_scores:", tr.baseline_scores)
except Exception as e:
    import traceback
    traceback.print_exc()

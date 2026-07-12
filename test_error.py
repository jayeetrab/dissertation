import sys
sys.path.append("/Users/jayeetra/Documents/GitHub/dissertation/backend")
from fastapi.testclient import TestClient
from main import app, load_results_from_disk

try:
    load_results_from_disk()
    client = TestClient(app)
    response = client.get("/results")
    print(response.status_code)
    print(response.text)
except Exception as e:
    import traceback
    traceback.print_exc()

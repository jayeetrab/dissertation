import requests
import time

def test_compare():
    url = "http://localhost:8001/run/task"
    
    subsets = [
        {"id": "nppf_only", "docs": ["NPPF_December_2024.pdf"]},
        {"id": "blp_only", "docs": ["Core_Strategy_WEB_PDF_low_res_with_links.pdf"]},
        {"id": "both", "docs": None}
    ]
    
    for s in subsets:
        print(f"Running {s['id']}...")
        payload = {
            "task_id": "PC-01",
            "run_baseline": False,
            "run_rag": True,
            "corpus_filter": s['docs']
        }
        res = requests.post(url, json=payload)
        print(f"Status: {res.status_code}")
        if res.status_code != 200:
            print(res.text)
        else:
            print("OK")
            
if __name__ == "__main__":
    test_compare()

# test_endpoint.py — Week 12: prove your server works (run while uvicorn is up)
#   python test_endpoint.py
import requests

BASE = "http://127.0.0.1:8000"

print("health:", requests.get(f"{BASE}/health", timeout=5).json())

good = {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}
r = requests.post(f"{BASE}/predict", json=good, timeout=5)
print("predict:", r.status_code, r.json())

bad = {"sepal_length": "not a number"}
r = requests.post(f"{BASE}/predict", json=bad, timeout=5)
print("bad input ->", r.status_code, "(expect 422: Pydantic rejected it before your code ran)")

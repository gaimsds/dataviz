# test_endpoint.py — Week 12: prove your server works (run while uvicorn is up)
#   python test_endpoint.py
#
# Three requests, each checking something different: that the server is alive,
# that a prediction comes back in the shape you designed, and that a bad
# request is rejected before your code ever runs.
import requests

BASE = "http://127.0.0.1:8000"

print("health:", requests.get(f"{BASE}/health", timeout=5).json())
print()

# 1. An easy one. Setosa is linearly separable from the other two, so the model
#    is certain and the probabilities come back 1.0 / 0.0 / 0.0.
easy = {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}
r = requests.post(f"{BASE}/predict", json=easy, timeout=5)
print("easy   ->", r.status_code, r.json())

# 2. A hard one. This is a real flower from the dataset, sitting on the
#    versicolor/virginica boundary. The model answers "virginica" at about 53%
#    confidence -- which is the whole reason the response carries a confidence
#    and not just a label. A client that prints the label and drops the number
#    reports a coin flip as a fact.
hard = {"sepal_length": 6.0, "sepal_width": 2.7, "petal_length": 5.0, "petal_width": 1.7}
r = requests.post(f"{BASE}/predict", json=hard, timeout=5)
print("hard   ->", r.status_code, r.json())

# 3. A broken one. The server should refuse it rather than crash.
#    FastAPI answers 422 on its own: Pydantic checks the request against the
#    schema and predict() is never called. The Flask server answers 400,
#    because there the check is code somebody had to write.
bad = {"sepal_length": "not a number"}
r = requests.post(f"{BASE}/predict", json=bad, timeout=5)
if r.status_code == 422:
    print("bad    -> 422 (rejected by the schema, before your code ran)")
    print("detail:", r.json()["detail"][0]["msg"])
elif r.status_code == 400:
    print("bad    -> 400 (rejected by a check the server wrote itself)")
    print("detail:", r.json().get("detail"))
else:
    print("bad    ->", r.status_code, "(expected 422 or 400: the server did not reject it)")
    print("detail:", r.text[:120])

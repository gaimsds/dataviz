# server_flask.py — Week 12: the same iris server, written in Flask
# Run with:  flask --app server_flask run --port 8000
# Then:      python test_endpoint.py        (the same script as for FastAPI)
#
# Needs one extra package:  pip install flask
#
# This file answers the same three requests as the FastAPI server, with the
# same response. Read it next to server_skeleton.py: everything FastAPI did
# from the two class declarations is written out by hand here, and there is no
# /docs page, because nothing in this file states what a request looks like.
from pathlib import Path

from flask import Flask, jsonify, request
import joblib
import pandas as pd

app = Flask(__name__)

# Next to THIS file, not next to wherever you launched Flask from.
BUNDLE_PATH = Path(__file__).resolve().parent / "model.joblib"
if not BUNDLE_PATH.exists():
    raise FileNotFoundError(
        f"{BUNDLE_PATH.name} not found next to {Path(__file__).name}. "
        f"Create it first:\n    python train_model.py"
    )

bundle = joblib.load(BUNDLE_PATH)       # LOAD ONCE, at startup
model = bundle["model"]
FEATURES = bundle["feature_names"]
CLASSES = bundle["class_names"]

# The request contract. In FastAPI this was the Flower class, and the framework
# enforced it. Here it is a tuple of names, and enforcing it is our job.
FIELDS = ("sepal_length", "sepal_width", "petal_length", "petal_width")


@app.get("/health")
def health():
    return jsonify(status="ok", classes=[str(c) for c in CLASSES])


@app.post("/predict")
def predict():
    data = request.get_json(silent=True)

    # --- validation, by hand -------------------------------------------
    # Without this block a bad request is not rejected at the door: it
    # travels into predict_proba and comes back as a 500 with a traceback.
    if not isinstance(data, dict):
        return jsonify(detail="Send a JSON object with the four measurements."), 400

    values, problems = [], []
    for field in FIELDS:
        if field not in data:
            problems.append(f"{field}: missing")
            continue
        try:
            values.append(float(data[field]))
        except (TypeError, ValueError):
            problems.append(f"{field}: not a number")
    if problems:
        return jsonify(detail=problems), 400
    # -------------------------------------------------------------------

    row = pd.DataFrame([values], columns=FEATURES)
    proba = model.predict_proba(row)[0]
    i = int(proba.argmax())

    # Nothing checks this dictionary against a declared response. If a key is
    # misspelled here, the client finds out, not the server.
    return jsonify(prediction=str(CLASSES[i]),
                   confidence=float(proba[i]),
                   probabilities={str(c): float(p) for c, p in zip(CLASSES, proba)})

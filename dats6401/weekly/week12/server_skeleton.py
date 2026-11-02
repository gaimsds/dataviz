# server_skeleton.py — Week 12 Block 3: COMPLETE THE TODOs
# Run with:  uvicorn server_skeleton:app --reload
# Then test in the auto-docs:  http://127.0.0.1:8000/docs
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path

app = FastAPI(title="My Model Server")

# Next to THIS file, not next to wherever you launched uvicorn from. A bare
# "model.joblib" resolves against the working directory, so starting the server
# from anywhere else raises FileNotFoundError at import -- which reads like a
# broken server rather than a wrong directory.
BUNDLE_PATH = Path(__file__).resolve().parent / "model.joblib"
if not BUNDLE_PATH.exists():
    raise FileNotFoundError(
        f"{BUNDLE_PATH.name} not found next to {Path(__file__).name}. "
        f"Create it first:\n    python train_model.py"
    )

bundle = joblib.load(BUNDLE_PATH)       # LOAD ONCE, at startup
model = bundle["model"]
FEATURES = bundle["feature_names"]      # the four iris measurements
CLASSES = bundle["class_names"]


class Flower(BaseModel):
    """The request schema. Pydantic validates types automatically:
    a bad request gets a 422 before your code even runs."""
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/health")
def health():
    # TODO 1: return a dict with a status field and the model's class names
    ...


@app.post("/predict")
def predict(x: Flower):
    # TODO 2: build a one-row DataFrame in the FEATURE ORDER the model expects:
    #   row = pd.DataFrame([[x.sepal_length, x.sepal_width, x.petal_length, x.petal_width]],
    #                      columns=FEATURES)
    # TODO 3: get predict_proba for the row; find the argmax index
    # TODO 4: return {"prediction": <class name>, "confidence": <float>,
    #                 "probabilities": {<class>: <float> for each class}}
    ...

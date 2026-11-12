# server_solution.py — Week 12 reference implementation
# Run with:  uvicorn server_solution:app --reload
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path

app = FastAPI(title="Iris Model Server")

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
FEATURES = bundle["feature_names"]
CLASSES = bundle["class_names"]


class Flower(BaseModel):
    """The REQUEST contract."""
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class Prediction(BaseModel):
    """The RESPONSE contract. Declaring it is what makes /docs describe what
    comes back, and FastAPI checks the return value against it."""
    prediction: str
    confidence: float
    probabilities: dict[str, float]


@app.get("/health")
def health():
    return {"status": "ok", "classes": list(CLASSES)}


@app.post("/predict", response_model=Prediction)
def predict(x: Flower):
    row = pd.DataFrame(
        [[x.sepal_length, x.sepal_width, x.petal_length, x.petal_width]],
        columns=FEATURES,
    )
    proba = model.predict_proba(row)[0]
    i = int(proba.argmax())
    return {
        "prediction": str(CLASSES[i]),
        "confidence": float(proba[i]),
        "probabilities": {str(c): float(p) for c, p in zip(CLASSES, proba)},
    }

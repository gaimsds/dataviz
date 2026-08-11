# Week 12 — Block 2 Demo Guide (~40 min)

Setup before class: `python train_model.py` (creates model.joblib).
Dependencies: `pip install fastapi uvicorn scikit-learn joblib pandas requests`

## Part 1 (~12 min) — schema first
Open `server_solution.py` but build it live from an empty file, in this order:
load the bundle (narrate LOAD ONCE), then the Pydantic `Flower` class.
Key line of narration: *"the schema IS the API contract — design it before any logic."*

## Part 2 (~15 min) — the /predict endpoint
Write `/predict` live (or fill `server_skeleton.py`'s TODOs).
Run `uvicorn server_solution:app --reload`, open **http://127.0.0.1:8000/docs** —
the auto-generated docs are the wow moment. Make a request from the docs UI.

## Part 3 (~13 min) — test like a client
Run `python test_endpoint.py`. Narrate the 422: validation rejected bad input
before your code ran. Then: students get `server_skeleton.py` in Block 3.

Block 3 (~35 min): students complete the skeleton's 4 TODOs, run `test_endpoint.py`
against THEIR server, then add a `/model-info` endpoint if they finish early.

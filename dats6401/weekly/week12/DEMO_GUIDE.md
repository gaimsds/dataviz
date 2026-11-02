# Week 12 — Block 2 Demo Guide (~70 min)

**Before class, in this folder:**

```bash
python train_model.py        # writes model.joblib (not distributed -- pickles
                             # are tied to the scikit-learn version that wrote them)
```

Dependencies: `pip install fastapi uvicorn scikit-learn joblib pandas requests`

## Part 1 (~20 min) — schema first

Open `server_solution.py` for reference but build it live from an empty file, in
this order: load the bundle, then the Pydantic `Flower` class.

Two things to narrate:

- **Load once.** The `joblib.load` sits at module level, not inside the endpoint.
  Ask why before you say why.
- **Resolve the path against the file, not the working directory.** `Path(__file__).resolve().parent / "model.joblib"`. A bare `"model.joblib"` works
  right up until someone starts uvicorn from one folder up, and then it raises
  `FileNotFoundError` at *import*, which reads like a broken server.

Key line: *"the schema IS the API contract — design it before any logic."*

## Part 2 (~28 min) — the /predict endpoint

Write `/predict` live. Run `uvicorn server_solution:app --reload` and open
**http://127.0.0.1:8000/docs** — the auto-generated docs are the wow moment.
Make a request from the docs UI.

Return `probabilities` as well as `prediction` and `confidence`. Part 3 is
where that pays off.

## Part 3 (~22 min) — test like a client

Run `python test_endpoint.py`. Three results, three points:

| request | result | the point |
|---|---|---|
| easy flower | `setosa`, confidence **1.0** | setosa separates cleanly; the model is certain |
| hard flower | `virginica`, confidence **0.53** | a real flower on the boundary — versicolor 0.47 |
| bad input | **422** | validation rejected it before your code ran |

The hard case is the one worth dwelling on. It is the reason the response
carries a confidence and not just a label: a client that prints the label and
drops the number reports a coin flip as a fact. That is also the thread into
Week 13, where this output gets visualized.

## Block 3 (~45 min, on your own after class)

Students complete `server_skeleton.py`'s 4 TODOs, run `test_endpoint.py` against
**their** server, then add a `/model-info` endpoint if they finish early.

This runs after the session, so the notebook and the skeleton have to stand on
their own: everything needed is in this folder, and `test_endpoint.py` tells a
student whether their server works without anyone looking at it.

# Final Project Deployment Checklist (DATS 6401)

## Repo & reproducibility
- [ ] `requirements.txt` pins all dependencies — BOTH pieces (client + server)
- [ ] `train_model.py` regenerates the model; no cross-version pickle committed
- [ ] README: how to run locally (exact commands), how to test, deployed URLs
- [ ] No secrets, keys, or tokens anywhere in the repo history

## Server
- [ ] `/health` responds 200 on the deployed URL
- [ ] `/predict` validates input (bad request -> 422 with a useful message)
- [ ] `/model-info` reports model type, features, training date
- [ ] Model + scalers load ONCE at startup, not per request

## Client
- [ ] `API_URL` read from `st.secrets` / env var, with a localhost fallback — never hard-coded
- [ ] Server down -> `st.error` + the app survives (no traceback)
- [ ] Expensive loads cached; nothing slow inside the widget path
- [ ] Uncertainty shown honestly (full distribution where it matters)

## Honesty & accessibility (the Week 14 lenses)
- [ ] Axes honest or flagged; smoothing/classification disclosed
- [ ] Colorblind-safe palette; no meaning carried by color alone
- [ ] Captions/alt text on figures; model limitations stated where users see them

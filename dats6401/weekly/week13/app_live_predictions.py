# app_live_predictions.py — Week 13: Streamlit client for the Week 12 model server
# 1) Start the server (week12 folder):  uvicorn server_solution:app --reload
# 2) Run this app:                      streamlit run app_live_predictions.py
import streamlit as st
import requests
import pandas as pd

st.title("Live Model Predictions")
st.caption("This app holds NO model — every prediction is a round trip to the FastAPI server.")

API_URL = st.sidebar.text_input("Server URL", "http://127.0.0.1:8000")

st.sidebar.header("Flower measurements (cm)")
sl = st.sidebar.slider("Sepal length", 4.0, 8.0, 5.8)
sw = st.sidebar.slider("Sepal width", 2.0, 4.5, 3.0)
pl = st.sidebar.slider("Petal length", 1.0, 7.0, 4.3)
pw = st.sidebar.slider("Petal width", 0.1, 2.5, 1.3)

if st.button("Predict", type="primary"):
    payload = {"sepal_length": sl, "sepal_width": sw,
               "petal_length": pl, "petal_width": pw}
    try:
        r = requests.post(f"{API_URL}/predict", json=payload, timeout=5)
        r.raise_for_status()
        out = r.json()
        st.success(f"Prediction: **{out['prediction']}**")
        st.progress(out["confidence"], text=f"Confidence: {out['confidence']:.0%}")
        with st.expander("Full probability distribution (the honest view)"):
            st.bar_chart(pd.Series(out["probabilities"]))
    except requests.RequestException as e:
        st.error(f"Server error: {e}")
        st.caption("Is the Week 12 server running?  uvicorn server_solution:app --reload")

# ------------------------------------------------------------------
# TODO (pick one in class):
# 1. Make the full probability bar chart the PRIMARY display (not an expander)
# 2. Add a "borderline example" button that sets the sliders to 5.5/2.8/4.3/1.8
# 3. Show a small history table of this session's predictions (st.session_state)
# ------------------------------------------------------------------

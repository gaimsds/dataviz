# starter_template.py — Week 5 hands-on scaffolding
# Replace the data load and the chart with YOUR Weeks 2-4 analysis.
# Run with:  streamlit run starter_template.py
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st

st.title("My App Title")            # TODO: name your app


# --- Data --------------------------------------------------------------------
@st.cache_data
def load_data():
    return px.data.tips()           # TODO: your data here


# Optional: let the user supply their own file instead of the built-in example.
# file_uploader returns None until someone picks a file, so handle that branch.
uploaded = st.sidebar.file_uploader("Upload a CSV", type="csv")
if uploaded is None:
    df = load_data()
else:
    df = pd.read_csv(uploaded)

# --- Controls ----------------------------------------------------------------
# TODO: at least two widgets in the sidebar that filter or parameterize df.
choice = st.sidebar.selectbox("A control", sorted(df["day"].unique()), key="choice")

sub = df[df["day"] == st.session_state.choice]

# TODO: add a layout element -- st.columns for metrics, or st.tabs for views.

# --- Chart -------------------------------------------------------------------
# Pick ONE of the three. Use your own figure whenever the encodings matter,
# which after Weeks 2-4 is most of the time.

# (a) Streamlit's built-in: quick, but it chooses the encodings.
st.scatter_chart(sub, x="total_bill", y="tip")

# (b) Your matplotlib / seaborn figure, unchanged from the notebook:
# fig, ax = plt.subplots(figsize=(7, 4))
# ax.scatter(sub["total_bill"], sub["tip"])
# st.pyplot(fig)
# plt.close(fig)                    # or figures pile up across re-runs

# (c) Your plotly figure, still interactive in the browser:
# fig = px.scatter(sub, x="total_bill", y="tip", color="time")
# st.plotly_chart(fig, use_container_width=True)

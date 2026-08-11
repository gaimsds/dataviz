# demo_2_widgets_layout.py — Week 5, Part 2: widgets, layout, state
# Run with:  streamlit run demo_2_widgets_layout.py
import streamlit as st
import plotly.express as px

st.title("Tips Dashboard")
df = px.data.tips()

# --- Sidebar: controls live here ---
days = st.sidebar.multiselect("Days", sorted(df["day"].unique()), default=list(df["day"].unique()))
smoker = st.sidebar.radio("Smoker", ["All", "Yes", "No"])

sub = df[df["day"].isin(days)]
if smoker != "All":
    sub = sub[sub["smoker"] == smoker]

# --- Layout: metrics in columns ---
c1, c2, c3 = st.columns(3)
c1.metric("Parties", len(sub))
c2.metric("Avg bill", f"${sub['total_bill'].mean():.2f}")
c3.metric("Avg tip %", f"{(sub['tip']/sub['total_bill']).mean()*100:.1f}%")

tab1, tab2 = st.tabs(["Chart", "Data"])
with tab1:
    st.scatter_chart(sub, x="total_bill", y="tip", color="time")
with tab2:
    st.dataframe(sub)

# --- session_state: variables do NOT survive re-runs; state does ---
st.divider()
if "clicks" not in st.session_state:
    st.session_state.clicks = 0
if st.button("I clicked the chart insight button"):
    st.session_state.clicks += 1
st.caption(f"Button clicked {st.session_state.clicks} times this session "
           "(a plain variable would reset to 0 on every interaction).")

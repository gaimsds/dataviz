# demo_1_basic.py — Week 5, Part 1: a first real app
# Run with:  streamlit run demo_1_basic.py
import streamlit as st
import plotly.express as px

st.title("Tips Explorer")
st.write("Every interaction re-runs this script top to bottom. Watch.")

df = px.data.tips()

day = st.selectbox("Day", sorted(df["day"].unique()))
sub = df[df["day"] == day]

st.write(f"{len(sub)} parties on {day}")
st.scatter_chart(sub, x="total_bill", y="tip")

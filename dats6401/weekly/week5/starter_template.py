# starter_template.py — Week 5 hands-on scaffolding
# Replace the data-load and chart with YOUR Weeks 2-4 analysis.
import streamlit as st
import plotly.express as px

st.title("My App Title")            # TODO: name your app

@st.cache_data
def load_data():
    return px.data.tips()           # TODO: your data here

df = load_data()

# TODO: add at least two widgets in the sidebar that filter/parameterize df
choice = st.sidebar.selectbox("A control", sorted(df["day"].unique()))

# TODO: add a layout element (st.columns or st.tabs)

# TODO: your chart, driven by the widgets
st.scatter_chart(df[df["day"] == choice], x="total_bill", y="tip")

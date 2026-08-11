# app_starter.py — Week 1: your first Streamlit app
# Run with:  streamlit run app_starter.py
import streamlit as st
import plotly.express as px

st.title("My First App")            # TODO 1: make the title yours

df = px.data.tips()                 # TODO 2: swap in another px.data dataset
                                    #         (gapminder, iris) or your own CSV
st.caption(f"{len(df)} rows")
st.dataframe(df.head(20))
st.scatter_chart(df, x="total_bill", y="tip")

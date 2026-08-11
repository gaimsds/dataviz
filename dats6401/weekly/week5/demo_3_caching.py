# demo_3_caching.py — Week 5, Part 3: caching
# Run with:  streamlit run demo_3_caching.py
# FIRST: comment out the @st.cache_data line, run, move a widget -> 3 s lag each time.
# THEN: restore the decorator -> instant after the first load.
import streamlit as st
import plotly.express as px
import time

st.title("Why caching matters")

@st.cache_data            # <- comment me out for the 'before' experience
def slow_load():
    time.sleep(3)         # simulate an expensive load / API call / model fit
    return px.data.gapminder()

df = slow_load()

year = st.slider("Year", int(df["year"].min()), int(df["year"].max()), 2007, step=5)
sub = df[df["year"] == year]
st.scatter_chart(sub, x="gdpPercap", y="lifeExp", size="pop", color="continent")
st.caption("With the cache on, moving the slider is instant: slow_load() ran once.")

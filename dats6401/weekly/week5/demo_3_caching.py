# demo_3_caching.py — Week 5, Part 3: caching
# Run with:  streamlit run demo_3_caching.py
# FIRST: comment out the @st.cache_data line, run, move a widget -> 3 s lag each time.
# THEN: restore the decorator -> instant after the first load.
import time

import plotly.express as px
import streamlit as st

st.title("Why caching matters")


@st.cache_data            # <- comment me out for the 'before' experience
def slow_load():
    time.sleep(3)         # simulate an expensive load / API call / model fit
    return px.data.gapminder()


df = slow_load()

year = st.slider("Year", int(df["year"].min()), int(df["year"].max()), 2007, step=5)
sub = df[df["year"] == year]
fig = px.scatter(sub, x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 log_x=True, size_max=45)
st.plotly_chart(fig, use_container_width=True)
st.caption("With the cache on, moving the slider is instant: slow_load() ran once.")

# ---------------------------------------------------------------------------
# The part that bites people: the two decorators do NOT behave the same way.
# ---------------------------------------------------------------------------
st.divider()
st.subheader("cache_data vs cache_resource")


@st.cache_data
def as_data():
    return {"calls": 0}


@st.cache_resource
def as_resource():
    return {"calls": 0}


if st.button("Mutate both, then read them back"):
    as_data()["calls"] += 1          # mutates a COPY -- the cache is untouched
    as_resource()["calls"] += 1      # mutates the ONE shared object

st.write("cache_data sees:", as_data(), " -> stays 0: you were handed a copy")
st.write("cache_resource sees:", as_resource(), " -> climbs: same object every time")

st.caption(
    "Use @st.cache_data for dataframes and results; it hands back a copy, so "
    "changing what you got is safe. Use @st.cache_resource for connections and "
    "models, and do not mutate what it returns -- on a deployed app that object "
    "is shared with every other user."
)

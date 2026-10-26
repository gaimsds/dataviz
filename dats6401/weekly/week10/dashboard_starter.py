# dashboard_starter.py — Week 10: a dashboard for point data
# Run with:  streamlit run dashboard_starter.py
# Requires:  pip install streamlit-folium scikit-learn
import json

import folium
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

st.set_page_config(page_title="Supercharger Dashboard", layout="wide")
st.title("Supercharger Dashboard")

EARTH_KM = 6371.0088


@st.cache_data
def load():
    df = pd.read_csv("data/superchargers_us.csv")
    # Contiguous states only, so the map is not mostly ocean. This is a choice
    # and it belongs in the caption.
    return df[(df.lat.between(24, 50)) & (df.lon.between(-125, -66))].copy()


sites = load()

# --- one control drives everything ------------------------------------------
states = ["All"] + sorted(sites.state.unique())
state = st.sidebar.selectbox("State", states)
min_stalls = st.sidebar.slider("Minimum stalls", 1, int(sites.stalls.max()), 1)

shown = sites if state == "All" else sites[sites.state == state]
shown = shown[shown.stalls >= min_stalls]
st.caption(f"{len(shown)} of {len(sites)} contiguous-US sites shown. "
           f"Alaska, Hawaii and Puerto Rico are excluded.")

if shown.empty:
    st.warning("No sites match those filters.")
    st.stop()


def as_geojson(df):
    """One GeoJson layer rather than one marker per point.

    The deck measured this: 2,254 points are about 1,481 KB as CircleMarkers
    and about 401 KB as a single GeoJson layer. The map looks the same.
    """
    return {"type": "FeatureCollection", "features": [
        {"type": "Feature",
         "geometry": {"type": "Point", "coordinates": [r.lon, r.lat]},
         "properties": {"name": r["name"], "stalls": int(r.stalls)}}
        for _, r in df.iterrows()]}


m = folium.Map(location=[shown.lat.mean(), shown.lon.mean()],
               zoom_start=4 if state == "All" else 6,
               tiles="OpenStreetMap", scrollWheelZoom=False)
folium.GeoJson(
    as_geojson(shown),
    name="Supercharger sites",
    marker=folium.CircleMarker(radius=4, fill=True, fill_opacity=0.7,
                               color="#d9534f", fill_color="#d9534f"),
    tooltip=folium.GeoJsonTooltip(fields=["name", "stalls"],
                                  aliases=["", "stalls:"]),
).add_to(m)
folium.LayerControl(collapsed=False).add_to(m)

st_folium(m, width=900, height=460)

# ------------------------------------------------------------------
# TODO 1: a coordinated chart.
#         A map cannot rank. Add a bar chart of the ten cities with the most
#         stalls IN THE CURRENT SELECTION, so it changes when the filters do.
#
# TODO 2: a number the map cannot show.
#         Compute the median distance from each shown site to its nearest
#         neighbor, with BallTree and metric="haversine", and display it with
#         st.metric. Remember: radians in, and the result is an angle until
#         you multiply by EARTH_KM.
# ------------------------------------------------------------------

# dashboard_starter.py — Week 10: the coordinated geospatial dashboard
# Run with:  streamlit run dashboard_starter.py
# Requires:  pip install streamlit-folium
import streamlit as st
import geopandas as gpd
import pandas as pd
import json
import folium
from streamlit_folium import st_folium

st.title("County Dashboard")

@st.cache_data
def load():
    gdf = gpd.read_file("../week9/data/counties.geojson").set_crs(epsg=4326, allow_override=True)
    stats = pd.read_csv("../week9/data/county_stats.csv")
    j = gdf.merge(stats, on="county_id")
    j["rate"] = j["events"] / j["population"] * 1000
    return j

joined = load()

# --- ONE control drives everything ---
metric = st.sidebar.selectbox("Metric", ["rate", "events", "population"])

minx, miny, maxx, maxy = joined.total_bounds
center = [(miny + maxy) / 2, (minx + maxx) / 2]   # bounds midpoint: no CRS warning, no centroid math
m = folium.Map(location=center, zoom_start=8, tiles="cartodbpositron")
folium.Choropleth(
    geo_data=json.loads(joined.to_json()),
    data=joined, columns=["county_id", metric],
    key_on="feature.properties.county_id",
    fill_color="OrRd", legend_name=metric,
).add_to(m)
folium.GeoJson(
    json.loads(joined.to_json()),
    style_function=lambda f: {"fillOpacity": 0, "weight": 0},
    tooltip=folium.GeoJsonTooltip(fields=["name", metric]),
).add_to(m)

out = st_folium(m, width=700, height=450)

# ------------------------------------------------------------------
# TODO 1: the coordinated ranking — top-10 bar chart of `metric`
#         (maps can't rank; give the comparison POSITION)

# TODO 2: details on demand — read out["last_object_clicked"],
#         sjoin the point into `joined`, show st.metric panel
# ------------------------------------------------------------------
st.caption("Scheme: linear color ramp on raw values — Week 9 rules: disclose or classify!")

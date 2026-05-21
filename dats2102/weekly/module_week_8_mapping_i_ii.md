# Week 8 — Mapping I & II

*Foundations & Choropleths; Spatial Joins, Enrichment & Interactivity*

## 📖 Background & Motivation

This two‑session module builds a solid foundation for geographic data visualization and then applies it to real analytical workflows. In **Mapping I**, students learn core geospatial concepts (data types, formats, and coordinate systems) and produce clear choropleth maps with appropriate normalization, classification, and legends. In **Mapping II**, students connect maps to real analysis tasks by performing spatial and attribute joins, enriching with socio‑economic context, and delivering interactive maps for exploration and communication.

---

## 🔎 Learning Objectives

- Distinguish vector vs. raster data; recognize common geospatial file formats (Shapefile, GeoJSON, TopoJSON, GeoPackage).
- Explain Coordinate Reference Systems (CRS) and projections; choose and document an appropriate CRS.
- Create choropleths with sensible normalization, classification, color, and legends.
- Perform spatial joins (point‑in‑polygon, polygon overlaps) and attribute joins on stable keys (e.g., FIPS/GEOID).
- Enrich maps with socio‑economic variables (e.g., ACS) and build interactive web maps.

---

## 📚 Readings & Resources

- **GeoPandas** User Guide — [geopandas.org](https://geopandas.org/en/stable/docs/user_guide/)
- **PyGIS — Intro to GIS in Python** — [pygis.io/docs/a\_intro.html](https://pygis.io/docs/a_intro.html)
- **Folium** Quickstart — [python-visualization.github.io/folium](https://python-visualization.github.io/folium/latest/)
- **Plotly Express** Choropleth — [plotly.com/python/choropleth-maps](https://plotly.com/python/choropleth-maps/)
- **Claus Wilke**, *Fundamentals of Data Visualization* (Geospatial) — [clauswilke.com/dataviz/geospatial.html](https://clauswilke.com/dataviz/geospatial.html)
- **ColorBrewer 2.0** — [colorbrewer2.org](https://colorbrewer2.org/)
- **EPSG.io** (CRS search) — [epsg.io](https://epsg.io/)
- **Census/ACS** data portal — [data.census.gov](https://data.census.gov/)
- **Social Explorer** — [socialexplorer.com/home](https://www.socialexplorer.com/home)
- **TopoJSON** docs — [github.com/topojson/topojson](https://github.com/topojson/topojson)


---

## 🛠️ Setup

Install/verify:

```bash
pip install geopandas folium plotly mapclassify pyproj shapely pandas matplotlib
```

Notes:

- If computing areas/lengths, reproject to an appropriate **projected** CRS (e.g., equal‑area).
- Interactive HTML maps (Folium/Plotly) load tiles/scripts at view time.

---

## 🧭 Session 1 — Mapping I: Foundations & Choropleths

### 1) Why map? When *not* to map

- Use maps when spatial structure matters (clusters, corridors, gradients).
- Prefer **rates/ratios** over raw counts; preview MAUP & ecological fallacy.

### 2) Geographic data fundamentals

- Vector (points/lines/polygons/multiparts) vs Raster (continuous/categorical); resolution, extent.

### 3) File formats

- **Shapefile** (.shp/.shx/.dbf/.prj) – common pitfalls: field name limits, encoding, missing .prj.
- **GeoJSON** (WGS84 lon/lat); **TopoJSON** (shared arcs, smaller web payloads); GeoPackage, Parquet+WKB.

### 4) CRS & projections

- Geographic vs Projected CRS; angular vs linear units.
- **WGS84 (EPSG:4326)** vs **Web Mercator (EPSG:3857)** vs **Equal‑Area** (e.g., **ESRI:102003** for CONUS).
- Distortions (area/distance/direction); document CRS in captions.

### 5) Choropleths: principles

- Appropriate use: polygon‑level **rates** with clear denominators and time windows.
- Classification: **Quantiles**, **Equal Interval**, **Natural Breaks (Jenks)**, Std‑Dev; 4–7 bins.
- Color: sequential for ordered magnitudes; diverging for centered (±mean); avoid rainbow; accessible palettes.
- Legends & captions: variable name + units, bin method, CRS, data period, source.

### 6) Demos

- **GeoPandas + Matplotlib**: static choropleth; export PNG/SVG.
- **Plotly Express**: interactive choropleth with hover; export HTML.
- **Folium**: tile basemap, tooltips/popups, layer control; export HTML.
- **Download** the [Jupyter Notebook and Data](week8/week8.zip)

### 7) Mini‑exercise

- Given polygons + counts + population: make **two** choropleths (quantiles vs equal‑interval).
- Add a 3‑sentence note comparing how binning changes the story.

---

## 🧭 Session 2 — Mapping II: Spatial Joins, Enrichment & Interactivity

### 1) Spatial joins

- Point‑in‑polygon (assign incidents/POIs to tracts), polygon‑to‑polygon (overlaps), nearest joins.
- GeoPandas `sjoin` predicates: `within`, `contains`, `intersects`; geometry validity & CRS alignment.

### 2) Attribute joins & data hygiene

- Join on stable keys (FIPS/GEOID). Handle types, leading zeros, whitespace, duplicates, missing keys.

### 3) Aggregation, normalization, and stability

- Dissolve/aggregate to analysis geography; **per‑capita / per‑household / per‑area** rates.
- Consider rate stabilization (mention: Empirical Bayes) for small populations.

### 4) Socio‑economic enrichment

- Typical sources: **ACS** (income, education, housing, commute), **CDC PLACES**, **BLS**.
- Temporal alignment and definitional consistency.

### 5) Interactive mapping patterns

- Layer toggles (choropleth + points), marker clustering, heatmaps (when appropriate).
- Filters (sliders/dropdowns), hover templates, annotations; geometry simplification & TopoJSON for performance.

### 6) Demos (brief)

- **Demo A**: spatial join (points→polygons) → counts per polygon → normalized rate.
- **Demo B**: attribute join with ACS; compute indicator; classify & map.
- **Demo C**: interactive Folium (choropleth + proportional symbols, tooltips, layer control).
- **Demo D**: interactive Plotly/Mapbox; export standalone HTML.

### 7) In‑class activity

- Start‑to‑finish pipeline:
  1. spatial join incidents → polygons,
  2. enrich with ACS denominator,
  3. build an interactive map with two layers,
  4. 3–5 sentence reflection on design choices + limitations.
  5. **Download** the [Jupyter Notebook and Data](week8/hands_on_session2.zip)

---

## 💻 Starter Notebook Snippets

```python
# GeoPandas read + quick plot
import geopandas as gpd
polys = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
polys.to_crs(3857).plot(edgecolor='white')
```

```python
# Attribute join on a key
import pandas as pd
attrs = pd.read_csv('attrs.csv')  # contains GEOID and a value
joined = polys.merge(attrs, how='left', left_on='iso_a3', right_on='GEOID')
```

```python
# Choropleth (static)
joined.plot(column='rate_per_10k', cmap='Blues', legend=True, edgecolor='0.7')
```

```python
# Plotly Express (interactive)
import plotly.express as px
import json
geojson = json.loads(polys.to_json())
fig = px.choropleth(joined, geojson=geojson, locations=joined.index,
                    color='rate_per_10k', featureidkey='properties.index')
fig.update_geos(fitbounds='locations', visible=False)
fig.show()
```

```python
# Spatial join (points → polygons)
pts = gpd.read_file('points.geojson').to_crs(polys.crs)
joined_pts = gpd.sjoin(pts, polys, predicate='within')
counts = joined_pts.groupby('polygon_id').size().rename('count')
result = polys.join(counts).fillna({'count':0})
```

---

## 🧪 In‑Class Activities

- Use provided notebook or your own dataset.
- Maintain a caption block for each map (CRS, data period, binning, source, denominator).

---

## 🏠 Homework

1. Pick a geographic unit (country/state/county/tract) + a topic.
2. Build a **reproducible pipeline** (notebook) that includes:
    - One **static choropleth** with clear legend + caption.
    - One **interactive map** (Folium or Plotly) with at least two layers (e.g., choropleth + points) and tooltips.
    - At least **one join** (spatial or attribute) and appropriate normalization.
    - A **150–250 word** reflection on design choices, denominators, classification, CRS, and limitations.
3. Use Quarto to render your notebook and submit the zip file.

**Rubric (10 pts)**

- Correct joins & CRS handling (3)
- Sound normalization + clear classification/legend (3)
- Interactive map quality (layers, tooltips, usability) (2)
- Reflection clarity & critique of limitations (2)

---

## ✅ Submission Checklist

Before submitting, make sure:

- Your assignment has fulfilled all the basic requirements listed above.
- The visualizations and your reflections in the Jupyter notebook are properly organized and displayed.
- Use Quarto to render the notebook into HTML and zip the files for submission.

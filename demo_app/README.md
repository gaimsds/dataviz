# Course demo app

A small Streamlit app for the course site. It is what
`dats6401/_live_app_embed.qmd` embeds, so once it is deployed the eight chapters
that include that file show a live app instead of a placeholder.

Three tabs, one idea each: encodings (Week 2), ordering a correlation matrix
(Week 3), and axis honesty (Week 4).

## Run it locally

```bash
pip install -r demo_app/requirements.txt
streamlit run demo_app/app.py
```

## Deploy it

1. share.streamlit.io → **New app**, pick this repository.
2. Set **Main file path** to `demo_app/app.py`.
3. Deploy, then copy the resulting URL.
4. Paste it into `dats6401/_live_app_embed.qmd`, replacing
   `https://YOUR-APP-NAME.streamlit.app` and keeping `?embed=true` on the end —
   that suppresses Streamlit's own chrome inside the iframe.

## Why this app is built the way it is

The free Community Cloud tier gives a small shared container that **sleeps when
idle**, so a visitor's first hit pays a cold start. Two consequences shaped this
app:

- **No long-running loops.** Every interaction is a click and a redraw. An
  animation loop of the kind in `dats6401/weekly/week4/app_rolling_animation.py`
  holds the app process for its whole run and is a poor fit for a shared free
  container — fine to run locally, bad to embed in a course page.
- **Four dependencies, in `demo_app/requirements.txt`.** The repository-root
  `requirements.txt` is the environment for *rendering the book* and pulls in
  geopandas, bertopic and umap-learn. Building that for a four-import app would
  make every cold start slow. Keep this list short.

The only data is the gapminder table bundled with plotly, so there is nothing to
download at startup and no data files to ship.

## Do not deploy the answer keys

`weekly_materials/week5/example_solution.py` is the Block 3 reference solution.
It lives outside this repository on purpose. A deployed URL is discoverable, so
it should not be published.

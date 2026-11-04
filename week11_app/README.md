# Week 11 live demo — consuming an API

A small Streamlit client for the Week 11 chapter. It is what
`dats6401/_live_app_week11.qmd` embeds, so once it is deployed the chapter
shows a running client instead of a placeholder.

It is Block 2 made clickable. Four things are on display:

- **Query parameters as the interface.** Every control changes a parameter on
  the request, not a filter on a table you already have.
- **The three checks.** Status, content type, and shape, shown as pass/fail so
  you can see *which one* caught a problem.
- **Caching keyed on arguments.** Repeat a combination of controls and the
  answer returns without touching the network.
- **Graceful failure.** A "break it on purpose" control points the same code at
  a 400, at a 200 that returns HTML, and at a host that does not resolve.

## Run it locally

```bash
pip install -r week11_app/requirements.txt
streamlit run week11_app/app.py
```

## Deploy it

1. share.streamlit.io → **New app**, pick this repository.
2. Set **Main file path** to `week11_app/app.py`.
3. Deploy, then copy the resulting URL.
4. Paste it into `dats6401/_live_app_week11.qmd`, replacing
   `https://YOUR-WEEK11-APP.streamlit.app` and keeping `?embed=true` on the end —
   that suppresses Streamlit's own chrome inside the iframe.

This is a second app alongside `demo_app/`; the free tier allows more than one.

## Why this app is built the way it is

The same constraints as `demo_app/README.md`: no long-running loops, a short
requirements list, and a layout that works inside a ~600px iframe with no
sidebar.

One difference. The demo app ships no data and downloads nothing at startup;
this one calls a live endpoint on every cold start, which is the entire point.
The endpoint chosen is the USGS Earthquake Catalog: public, no API key, and it
answered in about 0.16s when this was written. Nothing here needs a secret, so
there is nothing to configure in Community Cloud.

## Do not deploy the answer keys

`weekly_materials/week11/client_solution.py` and `week11_SOLUTIONS.ipynb` are
the Block 3 reference answers. They live outside this repository on purpose. A
deployed URL is discoverable, so they should not be published.

This app is not that solution. Block 3 asks students to pick *their own* API;
this one is the USGS client the instructor already builds live in Block 2.

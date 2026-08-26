# dataviz — GW Data Visualization Courses

Source for two Quarto-book course sites, published to GitHub Pages:

- **DATS 6401 — Visualization of Complex Data** (graduate) → `dats6401/`
- **DATS 2102 — Data Visualization for Data Science** (undergraduate) → `dats2102/`

Live site: `https://gaimsds.github.io/dataviz/`
(→ `…/dataviz/dats6401/` and, once added, `…/dataviz/dats2102/`)

---

## Repository layout

```
dataviz/
├── index.html                 # landing page linking both courses
├── requirements.txt           # Python deps for rendering executable chapters
├── .gitignore
├── .github/workflows/publish.yml   # builds + deploys to GitHub Pages
└── dats6401/                  # the graduate course book (Quarto project)
    ├── _quarto.yml            # book config (chapters, theme, freeze)
    ├── index.qmd              # book landing page
    ├── _live_app_embed.qmd    # reusable include: embed a live Streamlit app
    ├── week_01..04_*.qmd      # EXECUTABLE chapters (code runs at render time)
    └── week_05..14_*.qmd      # ILLUSTRATIVE chapters (static code + app embeds)
```

---

## The execution model (read this first)

This project uses Quarto's **freeze** feature (`execute: freeze: auto` in `_quarto.yml`):

1. **You render locally.** Running `quarto render` on your machine executes the
   Python cells in Weeks 1–4 and caches the results in `dats6401/_freeze/`.
2. **`_freeze/` is committed to git.** (It is intentionally *not* in `.gitignore`.)
3. **CI just publishes.** The GitHub Action assembles the already-frozen HTML and
   deploys it — it does **not** run Python. This keeps the build fast and avoids
   installing heavy libraries (geopandas, bertopic, …) in the runner.

**Workflow rule of thumb:** edit `.qmd` → `quarto render dats6401` locally →
commit the `.qmd` *and* the updated `_freeze/` → push. Pages updates automatically.

Only Weeks 1–4 contain executable cells (` ```{python} `). All later chapters use
plain ` ```python ` blocks that are shown as copy-and-run source, not executed.

---

## Local setup

```bash
# 1. Install Quarto: https://quarto.org/docs/get-started/
# 2. Python env for the executable chapters:
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 3. Preview the grad book with live reload:
quarto preview dats6401

# 4. Full render (executes Weeks 1-4, writes _freeze/):
quarto render dats6401
```

The executable cells use datasets that ship with `plotly`, `scikit-learn`, and
`statsmodels`, so rendering needs **no network access** — the build won't break
on a flaky connection.

---

## One-time GitHub Pages setup

1. Push this repo to `github.com/gaimsds/dataviz` on the `main` branch.
2. In the repo: **Settings → Pages → Build and deployment → Source = GitHub Actions**.
3. The `publish.yml` workflow runs on every push to `main` and deploys the site.

---

## Embedding live Streamlit apps

App code (Streamlit, FastAPI) can't execute inside a static page. Instead, deploy
each app and embed the **running** app via the include in `_live_app_embed.qmd`:
replace the placeholder URL with your deployed app URL plus `?embed=true`.

---

## Lecture slides

`slides/` is a **separate Quarto project** (revealjs, not a book) holding the 14
DATS 6401 lecture decks. It follows the same execution model as the books:
figures execute locally and are cached in `slides/_freeze/`, which is committed,
so CI publishes without running Python.

```bash
quarto render slides                      # all 14 decks -> slides/_output/
quarto preview slides/week06_graph_network_data.qmd   # live reload, one deck
```

The publish workflow renders it to `_site/dats6401/slides/`, so a deck lands at
`…/dataviz/dats6401/slides/week06_graph_network_data.html`. Note `slides/_output/`
is git-ignored — commit the `.qmd` and `_freeze/`, never the rendered decks.

`slides/index.qmd` is the landing page listing all 14 decks, served at
`…/dataviz/dats6401/slides/`. It is the one file here that is **not** a deck —
it overrides the project's revealjs format to plain HTML in its own front
matter. Add a row to its table whenever a deck is added.

---

## Adding the undergraduate course later

1. Create a `dats2102/` folder with its own `_quarto.yml` (copy `dats6401/_quarto.yml`
   as a starting point and change the title/chapters).
2. Uncomment the DATS 2102 render step in `.github/workflows/publish.yml`.
3. Uncomment the DATS 2102 card in `index.html`.

---

## Working with Claude Code

This repo is structured so Claude Code can iterate locally: edit a `.qmd`, run
`quarto render dats6401`, read any execution error, fix the cell, and re-render
until clean — then commit `.qmd` + `_freeze/` and push. Good first tasks: make a
later chapter's chart code executable, wire a deployed app URL into a chapter's
embed, or scaffold the `dats2102/` book.

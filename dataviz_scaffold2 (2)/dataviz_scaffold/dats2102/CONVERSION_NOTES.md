# DATS 2102 — Conversion Notes

Auto-generated summary of how each module's code snippets were converted.

- **Executable** = ` ```{python} ` cell; runs and renders when you `quarto render`.
- **Static** = ` ```python ` cell; shown as copy-and-run source (depends on local files / external context). Edit these page-by-page if you want them live.
- 🌐 = executable but fetches data at render time (seaborn/plotly); render with a network connection.

| Chapter | Executable | Static | Notes |
|---|---|---|---|
| index.qmd | 0 | 0 |  |
| project_final.qmd | 0 | 0 |  |
| project_midterm.qmd | 0 | 0 |  |
| week_01_getting_started.qmd | 🌐 4 | 0 |  |
| week_02_language_of_graphs.qmd | 🌐 5 | 0 |  |
| week_03_distributions_variation.qmd | 🌐 1 | 0 | Fixed `numpy` import order so the ECDF cell runs. |
| week_04_wrangling_with_pandas.qmd | 0 | 1 | 1 static block reads `nyc_taxi_sample.csv` (in the linked notebook). |
| week_05_perception_principles.qmd | 1 | 0 |  |
| week_06_comparisons.qmd | 🌐 4 | 0 |  |
| week_07_text_labels_tables.qmd | 🌐 2 | 0 |  |
| week_08_mapping_i_ii.qmd | 0 | 5 | All 5 blocks static — interdependent geodata sequence (reads shapefiles/GeoJSON). Full notebook+data in `week8.zip`. |
| week_09_color_accessibility.qmd | 🌐 3 | 0 |  |
| week_10_relationships_modeling.qmd | 🌐 4 | 0 |  |
| week_11_uncertainty_error.qmd | 🌐 3 | 0 |  |
| week_12_viz_ml_nlp.qmd | 3 | 2 | ROC snippet fixed to use a binary iris subset. Word-cloud and BERTopic blocks left static (need extra packages / corpus). |

# Week 5 — Block 3 Hands-On (~55 min)

**Goal:** convert one of YOUR notebooks from Weeks 2–4 into a deployed Streamlit app.

## Steps

1. (~31 min) Pick an analysis you built in Weeks 2–4 — the encodings chart, the PCA
   scatter, the rolling-mean trend. Create `app.py` and port it:
   data load → widgets → chart.

   **You do not need to rebuild the chart.** Whatever you drew in the notebook comes
   across as it is:

   ```python
   st.pyplot(fig)                              # matplotlib / seaborn
   plt.close(fig)                              # or figures pile up across re-runs
   st.plotly_chart(fig, use_container_width=True)   # plotly, stays interactive
   ```

   Use `st.line_chart` / `st.scatter_chart` only where the encodings do not matter.
   No analysis handy? `starter_template.py` in this folder has the scaffolding.

2. (~12 min) Add at least: a sidebar, TWO widgets that change the output, and one
   layout element (`st.columns` or `st.tabs`). Wrap the data load in `@st.cache_data`.

   Worth reaching for if they fit your app:
   - `st.form` — when several inputs belong together, or a text box would otherwise
     re-run the page on every keystroke
   - `@st.fragment` — when one control should redraw a chart without re-running an
     expensive page
   - `st.file_uploader` — so someone can point the app at their own CSV

3. (~12 min) Deploy: push to a GitHub repo → share.streamlit.io → New app.
   Paste your live URL in the class thread.

## Checklist before you leave

- [ ] `streamlit run app.py` works locally with no errors
- [ ] Two widgets, one layout element, caching applied
- [ ] The chart is the one you designed, not a fallback you settled for
- [ ] If you used `file_uploader`, the app still works before a file is chosen
- [ ] Deployed URL loads for your neighbour

A completed reference (`example_solution.py`, a Week-3 PCA explorer) is for AFTER you try.

# Week 5 — Block 2 Demo Guide (~45 min)

Streamlit apps can't live in a notebook, so this demo is a sequence of **progressive app files**.
Open each in your editor, run it, narrate, then move to the next.

Dependencies: `pip install streamlit plotly pandas matplotlib`

## Part 1 — A first real app (~19 min): `demo_1_basic.py`

Run: `streamlit run demo_1_basic.py`

- Narrate the **re-run model**: the entire script re-executes top-to-bottom on every interaction.
- Change the title while it runs → show hot reload.
- Add `st.write("script ran!")` at the top live; move the **Day** selector and watch it
  print on every change.
- Then the part that matters for Block 3: flip the **"Draw it with"** radio through
  `st.scatter_chart` → `matplotlib` → `plotly`.
  - `st.scatter_chart` is a convenience that picks the encodings for you.
  - `st.pyplot(fig)` takes the matplotlib figure they already know how to build.
  - `st.plotly_chart(fig)` keeps hover and zoom in the browser.
  - Point at `plt.close(fig)` and say why: without it, figures accumulate across
    re-runs and Streamlit eventually warns.

**This is the slide students most need for their own app** — every Weeks 2–4 chart
moves in through `st.pyplot` or `st.plotly_chart`, unchanged.

## Part 2 — Widgets, layout, state (~13 min): `demo_2_widgets_layout.py`

- Sidebar vs main; columns; metrics; tabs.
- Point out `key=` on the sidebar widgets, and that the values are read back from
  `st.session_state` rather than passed around.
- **The form**: type in the label box with the form open — nothing happens until
  *Apply*. Ask what would happen without the form (a re-run per keystroke).
- **The fragment**: change the histogram selectbox and note that the metrics above
  do not recompute. Only the fragment re-runs.
- The counter at the bottom: why `session_state` is needed at all (plain variables
  reset on every re-run).

## Part 3 — Caching (~13 min): `demo_3_caching.py`

- Run it WITHOUT the `@st.cache_data` decorator first (comment it out): every widget
  change re-sleeps 3 s.
- Uncomment → instant. Narrate: cache key = the function's arguments *and* its source.
- Then the second half of the file: press **"Mutate both, then read them back"** a few
  times. `cache_data` stays at 0 because you were handed a copy; `cache_resource`
  climbs because it is the same object every time. Land the rule: `cache_data` for
  dataframes and results, `cache_resource` for connections and models, and never
  mutate what `cache_resource` gives you — on a deployed app it is shared with every
  other user.
- Close: deploy `demo_2` to Streamlit Community Cloud live if time allows
  (push to GitHub → share.streamlit.io).

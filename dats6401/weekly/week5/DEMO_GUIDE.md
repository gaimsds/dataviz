# Week 5 — Block 2 Demo Guide (~35 min)

Streamlit apps can't live in a notebook, so this demo is a sequence of **progressive app files**.
Open each in your editor, run it, narrate, then move to the next.

## Part 1 — A first real app (~15 min): `demo_1_basic.py`
Run: `streamlit run demo_1_basic.py`
- Narrate the **re-run model**: the entire script re-executes top-to-bottom on every interaction.
- Change the title while it runs -> show hot reload.
- Add `st.write("script ran!")` at the top live; move the species selector and watch it print on every change.

## Part 2 — Widgets, layout, state (~10 min): `demo_2_widgets_layout.py`
- Sidebar vs main; columns; metrics.
- Show `st.session_state` with the counter at the bottom: WHY it's needed (variables reset on re-run).

## Part 3 — Caching (~10 min): `demo_3_caching.py`
- Run it WITHOUT the `@st.cache_data` decorator first (comment it out): every widget change re-sleeps 3 s.
- Uncomment -> instant. Narrate: cache key = function arguments.
- Close: deploy `demo_2` to Streamlit Community Cloud live if time allows (push to GitHub -> share.streamlit.io).

Dependencies: `pip install streamlit plotly pandas`

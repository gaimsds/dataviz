# client_starter.py — Week 11: a Streamlit client that consumes an API
#
# This needs TWO processes, in TWO terminals, both left running:
#
#   1.  uvicorn course_endpoint:app --port 8001     <- the server. Yours, not
#                                                      the instructor's: 127.0.0.1
#                                                      means YOUR machine.
#   2.  streamlit run client_starter.py             <- the client
#
# Killing the first one while the second is running is how you test the error
# path, and it is the behavior the homework grades.
#
# Needs: pip install fastapi uvicorn scikit-learn streamlit requests pandas
import streamlit as st
import requests
import pandas as pd

st.title("API Client — Course Endpoint")

BASE = st.sidebar.text_input("Endpoint base URL", "http://127.0.0.1:8001")
species = st.sidebar.selectbox("Species", ["(all)", "setosa", "versicolor", "virginica"])

@st.cache_data(ttl=300)
def fetch(base, species):
    params = {} if species == "(all)" else {"species": species}
    r = requests.get(f"{base}/data", params=params, timeout=5)
    r.raise_for_status()
    # raise_for_status checks the STATUS only. See Part B of the Block 2 demo
    # for why that is not enough against an API you do not control, and for the
    # get_json() helper that also checks the content type and the shape.
    return r.json()

if st.button("Fetch"):
    try:
        payload = fetch(BASE, species)
        df = pd.DataFrame(payload["records"])
        st.success(f"{payload['count']} records")
        st.scatter_chart(df, x="sepal length (cm)", y="petal length (cm)", color="species")
        st.dataframe(df.head(20))
    except requests.RequestException as e:
        st.error(f"Request failed: {e}")
        st.caption("Is the server running? Is the URL right? (This is the graceful path.)")

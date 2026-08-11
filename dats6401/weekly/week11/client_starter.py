# client_starter.py — Week 11: a Streamlit client that consumes an API
# Run with:  streamlit run client_starter.py
# (For the course endpoint, the instructor's server must be running on port 8001.)
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

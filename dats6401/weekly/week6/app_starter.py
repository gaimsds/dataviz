# app_starter.py — Week 6 starter: interactive network explorer
# Run with:  streamlit run app_starter.py
import streamlit as st
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

st.title("Network Explorer — Les Misérables")
st.caption("Week 6 starter app. Extend it for your homework!")

# --- Sidebar controls ---
layout = st.sidebar.selectbox("Layout", ["force-directed", "circular"])
min_degree = st.sidebar.slider("Hide nodes with degree below", 1, 10, 1)

# --- Load and filter the graph ---
@st.cache_data
def load_edges():
    G = nx.les_miserables_graph()
    return G

G = load_edges()
keep = [n for n, d in G.degree() if d >= min_degree]
H = G.subgraph(keep)

c1, c2, c3 = st.columns(3)
c1.metric("Nodes", H.number_of_nodes())
c2.metric("Edges", H.number_of_edges())
c3.metric("Layout", layout)

# --- Build the interactive PyVis network ---
net = Network(height="600px", width="100%", cdn_resources="in_line", notebook=False)
net.from_nx(H)
if layout == "circular":
    net.toggle_physics(False)

net.save_graph("graph.html")
with open("graph.html", "r", encoding="utf-8") as f:
    components.html(f.read(), height=620)

# ------------------------------------------------------------------
# TODO (pick one in class; extend further for homework):
# 1. Color nodes by detected community
#    (networkx.algorithms.community.greedy_modularity_communities)
# 2. Size nodes by betweenness centrality (scale up! e.g. v*2000+20)
# 3. Add a selectbox that switches the sizing between degree,
#    betweenness, and closeness centrality
# ------------------------------------------------------------------

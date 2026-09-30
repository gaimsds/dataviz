#!/usr/bin/env python3
"""Generate the interactive karate-club network embedded in the Week 6 deck,
the Week 6 chapter, and the course demo app.

The output is written once and committed, rather than built at render time, so
that `quarto render` needs no extra dependency and CI -- which runs no Python --
is unaffected.

    python3 make_interactive_network.py

Writes karate_network.html next to this script. cdn_resources="in_line" bundles
vis.js into the file, so the page works with no network access when a student
opens it.
"""
import re
from pathlib import Path

import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
from pyvis.network import Network

OUT = Path(__file__).with_name("karate_network.html")
PALETTE = ["#2E6E8E", "#d9534f", "#6aa84f", "#b07aa1", "#e6a23c", "#5a6672"]

G = nx.karate_club_graph()
degree = dict(G.degree())
community = {n: i for i, c in enumerate(greedy_modularity_communities(G)) for n in c}

net = Network(height="520px", width="100%", bgcolor="#ffffff",
              font_color="#222222", cdn_resources="in_line", notebook=False)

for n in G.nodes():
    net.add_node(
        n, label=str(n),
        # Same encodings as the static slide: size = degree, colour = community.
        size=8 + degree[n] * 1.6,
        color=PALETTE[community[n] % len(PALETTE)],
        title=f"node {n} · degree {degree[n]} · community {community[n]}",
    )
for u, v in G.edges():
    net.add_edge(u, v, color="#cccccc")

# Slow the simulation down a little: the default settles so fast that students
# never see the force layout doing its work.
net.set_options("""
{
  "physics": {
    "barnesHut": {"gravitationalConstant": -8000, "springLength": 120,
                  "springConstant": 0.03, "damping": 0.35},
    "stabilization": {"iterations": 120}
  },
  "interaction": {"hover": true, "tooltipDelay": 120, "navigationButtons": true},
  "nodes": {"borderWidth": 0, "font": {"size": 11, "color": "#ffffff"}},
  "edges": {"smooth": false, "width": 1}
}
""")

net.save_graph(str(OUT))

# PyVis inlines vis.js but its template still links Bootstrap from a CDN, which
# nothing here uses -- we render no PyVis menus or buttons. Strip those two tags
# so the file really does work with no network access.
html = OUT.read_text(encoding="utf-8")
before = html.count("cdn.jsdelivr.net")
html = re.sub(r'\s*<(link|script)[^>]*cdn\.jsdelivr\.net[^>]*>(</script>)?', "", html)
OUT.write_text(html, encoding="utf-8")

# PyVis writes a fixed canvas height, so the graph is cropped whenever the iframe
# embedding it is shorter than that. Make the container fill the viewport instead,
# so one file works at whatever height the deck, the chapter or the app gives it.
responsive = """
<style>
  html, body { height: 100%; margin: 0; padding: 0; }
  #mynetwork { height: 100% !important; width: 100% !important; border: none !important; }
  .card { height: 100%; border: none !important; }
</style>
</head>"""
assert html.count("</head>") == 1, "unexpected PyVis template"
html = html.replace("</head>", responsive)

# vis.js leaves the camera wherever the simulation ended, so the graph can start
# part-way off screen. Fit the view once the layout settles, and again if the
# frame is resized.
fit = """
<script type="text/javascript">
  function fitNetwork() { network.fit({animation: false}); }
  network.once("stabilizationIterationsDone", fitNetwork);
  window.addEventListener("resize", fitNetwork);
</script>
</body>"""
assert html.count("</body>") == 1, "unexpected PyVis template"
html = html.replace("</body>", fit)
OUT.write_text(html, encoding="utf-8")

remaining = html.count("http://") + html.count("https://")
print(f"wrote {OUT}  ({OUT.stat().st_size/1024:.0f} KB)")
print(f"removed {before} CDN reference(s); external URLs left in file: {remaining}")

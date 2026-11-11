# app_detect_client.py — Week 13: Streamlit client for the Week 12 detection server
# 1) Start the server (week12 folder):  uvicorn detect_server:app --reload
# 2) Run this app:                      streamlit run app_detect_client.py
#
# This app holds NO model. It sends an image to the server, gets back every box
# the model scored, and decides for itself which ones are worth showing.
import base64
import io
import time
from pathlib import Path

import pandas as pd
import requests
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image, ImageDraw, ImageFont

COLORS = ["red", "blue", "orange", "green", "purple", "brown", "magenta", "teal"]
SAMPLE = Path(__file__).resolve().parent / "sample_astronaut.jpg"


def compare(left, right, label_left="original", label_right="processed"):
    """A before/after slider, the same helper as the Week 8 image browser."""
    def b64(im):
        buf = io.BytesIO(); im.convert("RGB").save(buf, format="PNG")
        return base64.b64encode(buf.getvalue()).decode()

    right = right.resize(left.size)
    w, h = left.size
    shown_h = int(700 * h / w)
    cap = ("position:absolute;top:8px;background:rgba(0,0,0,.6);color:#fff;"
           "padding:2px 8px;font:13px sans-serif;border-radius:3px")
    components.html(f"""
      <div style="position:relative;max-width:700px">
        <img src="data:image/png;base64,{b64(left)}" style="width:100%;display:block">
        <img id="top" src="data:image/png;base64,{b64(right)}"
             style="width:100%;position:absolute;top:0;left:0;clip-path:inset(0 0 0 50%)">
        <span style="{cap};left:8px">{label_left}</span>
        <span style="{cap};right:8px">{label_right}</span>
        <input type="range" min="0" max="100" value="50" style="width:100%;margin-top:6px"
               oninput="document.getElementById('top').style.clipPath=
                        'inset(0 0 0 '+this.value+'%)'">
      </div>
    """, height=shown_h + 50)


def server_is_up(url):
    # Never cached: a cached health check reports the server up after it has
    # gone down (Week 11).
    try:
        return requests.get(f"{url}/health", timeout=3).ok
    except requests.RequestException:
        return False


@st.cache_data(show_spinner="Asking the server...")
def detect(image_bytes, url):
    # Cached on the image and the URL -- and NOT on the threshold. Moving the
    # slider re-filters boxes we already have; it never calls the model again.
    start = time.perf_counter()
    r = requests.post(f"{url}/detect", files={"file": ("image", image_bytes)},
                      timeout=60)
    r.raise_for_status()
    out = r.json()
    out["round_trip"] = time.perf_counter() - start
    return out


def draw_boxes(image, detections):
    """Return a copy of `image` with one labeled box per detection.

    Sizes are set from the image WIDTH, because the page shows every image at
    the same width: a label then reads the same size on a phone photo and on a
    small thumbnail, and stays legible from the back of a room.
    """
    out = image.copy()
    pen = ImageDraw.Draw(out)
    line = max(2, round(out.width / 250))
    font = ImageFont.load_default(size=max(14, round(out.width / 32)))
    pad = max(2, round(out.width / 300))
    labels = sorted({d["label"] for d in detections})
    # Least confident first, so where labels overlap the surest one is on top.
    for d in sorted(detections, key=lambda d: d["score"]):
        color = COLORS[labels.index(d["label"]) % len(COLORS)]
        b = d["box"]
        pen.rectangle([b["xmin"], b["ymin"], b["xmax"], b["ymax"]],
                      outline=color, width=line)
        text = f'{d["label"]} {d["score"]:.2f}'
        left, top, right, bottom = pen.textbbox((0, 0), text, font=font)
        w, h = right - left + 2 * pad, bottom - top + 2 * pad
        # Sit the label on top of the box, or just inside it when the box
        # touches the top of the image; keep it from running off the right.
        x = min(max(b["xmin"], 0), max(out.width - w, 0))
        y = b["ymin"] - h if b["ymin"] - h >= 0 else b["ymin"]
        pen.rectangle([x, y, x + w, y + h], fill=color)
        pen.text((x + pad - left, y + pad - top), text, fill="white", font=font)
    return out


st.title("Live Object Detection")
st.caption("This app holds NO model — every detection is a round trip to the FastAPI server.")

API_URL = st.sidebar.text_input("Server URL", "http://127.0.0.1:8000")
threshold = st.sidebar.slider("Show boxes scoring at least", 0.10, 1.00, 0.50, 0.05)
st.sidebar.caption("The server returns every box above 0.10. This slider only "
                   "chooses which ones to draw, so moving it does not call the model.")

if not server_is_up(API_URL):
    st.error(f"No server answering at {API_URL}.")
    st.caption("Start it from the week12 folder:  uvicorn detect_server:app --reload")
    st.stop()

upload = st.file_uploader("An image", type=["jpg", "jpeg", "png"])
if upload is not None:
    image_bytes = upload.getvalue()
elif SAMPLE.exists():
    image_bytes = SAMPLE.read_bytes()
    st.caption("No upload yet, so this is the sample image.")
else:
    st.info("Upload an image to begin.")
    st.stop()

try:
    result = detect(image_bytes, API_URL)
except requests.HTTPError as e:
    # The server answered, and said no. Show ITS reason, not ours.
    st.error(f"The server rejected the image: {e.response.json().get('detail', e)}")
    st.stop()
except requests.RequestException as e:
    st.error(f"Could not reach the server: {e}")
    st.stop()

image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
everything = result["detections"]
shown = [d for d in everything if d["score"] >= threshold]

a, b, c = st.columns(3)
a.metric("Boxes drawn", len(shown))
b.metric("Boxes returned", len(everything))
c.metric("Model time", f'{result["seconds"] * 1000:.0f} ms')
st.caption(f'Round trip {result["round_trip"] * 1000:.0f} ms, of which the model '
           f'took {result["seconds"] * 1000:.0f} ms. The rest is the network and the upload.')

compare(image, draw_boxes(image, shown), "original", f"score ≥ {threshold:.2f}")

st.subheader("Every box the server returned")
table = pd.DataFrame({"label": [d["label"] for d in everything],
                      "score": [d["score"] for d in everything],
                      "drawn": [d["score"] >= threshold for d in everything]})
st.dataframe(table, hide_index=True,
             column_config={"score": st.column_config.ProgressColumn(
                 "score", min_value=0.0, max_value=1.0, format="%.2f")})

# ------------------------------------------------------------------
# TODO (pick one):
# 1. Color the boxes by SCORE instead of by label, so doubt is visible on the image
# 2. Add a multiselect that limits the boxes to chosen labels
# 3. Plot how the number of boxes drawn changes as the threshold moves from 0.1 to 1.0
# ------------------------------------------------------------------

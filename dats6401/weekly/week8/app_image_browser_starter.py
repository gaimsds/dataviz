# app_image_browser_starter.py — Week 8: image browser + stats
# Run with:  streamlit run app_image_browser_starter.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from PIL import Image

st.title("Image Browser")

tab1, tab2 = st.tabs(["Digits dataset", "Upload your own"])

with tab1:
    digits = load_digits()
    cls = st.selectbox("Class", sorted(np.unique(digits.target)))
    idxs = np.where(digits.target == cls)[0]
    i = st.slider("Image #", 0, len(idxs) - 1, 0)
    img = digits.images[idxs[i]]
    c1, c2 = st.columns(2)
    with c1:
        fig, ax = plt.subplots(); ax.imshow(img, cmap="gray"); ax.axis("off")
        st.pyplot(fig)
    with c2:
        st.metric("Mean intensity", f"{img.mean():.1f}")
        st.metric("Ink (nonzero px)", int((img > 0).sum()))

with tab2:
    up = st.file_uploader("PNG/JPG", type=["png", "jpg", "jpeg"])
    if up:
        pil = Image.open(up)
        arr = np.array(pil)
        st.image(pil, caption=f"shape: {arr.shape}")
        if arr.ndim == 3:
            st.bar_chart({"R": [arr[...,0].mean()], "G": [arr[...,1].mean()], "B": [arr[...,2].mean()]})

# ------------------------------------------------------------------
# TODO (pick one):
# 1. Add the class MEAN image next to the selected image
# 2. Add an intensity histogram (np.histogram -> st.bar_chart)
# 3. Channel histograms for uploads (per-channel, overlaid)
# ------------------------------------------------------------------

# detect_server.py — Week 12: the same four steps, serving a real model
# Run with:  uvicorn detect_server:app --reload
# Then:      http://127.0.0.1:8000/docs      (or: python test_detect.py)
#
# The iris server taught the contract on a model small enough to ignore. This
# one wraps an object detector from the Hugging Face Hub, and nothing about the
# structure changes: load once, declare the response, validate, answer.
#
# Extra packages for this file:  pip install -r requirements_detect.txt
# The first run downloads the model (about 25 MB) and caches it.
import io
import time

from fastapi import FastAPI, File, HTTPException, UploadFile
from PIL import Image, UnidentifiedImageError
from pydantic import BaseModel
import torch
from transformers import AutoImageProcessor, AutoModelForObjectDetection

MODEL_NAME = "hustvl/yolos-tiny"

# The server returns every box it scores above this floor, including ones it
# barely believes. Deciding which are worth showing is the CLIENT's job -- the
# same reason the iris server returned the whole distribution, not the winner.
FLOOR = 0.10

app = FastAPI(title="Object Detection Server")

# LOAD ONCE, at startup. With iris this rule was easy to ignore: loading took
# milliseconds. Here it takes seconds, so a server that loaded the model inside
# the endpoint would make every caller wait for it on every request.
processor = AutoImageProcessor.from_pretrained(MODEL_NAME)
model = AutoModelForObjectDetection.from_pretrained(MODEL_NAME).eval()


class Box(BaseModel):
    """Pixel coordinates in the image that was sent."""
    xmin: float
    ymin: float
    xmax: float
    ymax: float


class Detection(BaseModel):
    label: str
    score: float
    box: Box


class Detections(BaseModel):
    """The RESPONSE contract. `seconds` is the time the model took, so a client
    can tell a slow model from a slow network."""
    width: int
    height: int
    seconds: float
    detections: list[Detection]


@app.get("/health")
def health():
    return {"status": "ok", "model": MODEL_NAME,
            "labels": len(model.config.id2label)}


@app.post("/detect", response_model=Detections)
def detect(file: UploadFile = File(...)):
    # A request with no file at all never reaches this line: FastAPI answers
    # 422, as it did for a bad flower. A file that is not an image does reach
    # it, because "is this a picture?" is not something a type can check. That
    # validation we write ourselves.
    try:
        image = Image.open(io.BytesIO(file.file.read())).convert("RGB")
    except UnidentifiedImageError:
        raise HTTPException(status_code=400,
                            detail="That file is not an image this server can read.")

    start = time.perf_counter()
    with torch.no_grad():
        outputs = model(**processor(images=image, return_tensors="pt"))
    result = processor.post_process_object_detection(
        outputs, threshold=FLOOR, target_sizes=[image.size[::-1]])[0]
    seconds = time.perf_counter() - start

    found = [
        {"label": model.config.id2label[int(label)],
         "score": float(score),
         "box": dict(zip(("xmin", "ymin", "xmax", "ymax"),
                         (float(v) for v in box)))}
        for score, label, box in zip(result["scores"], result["labels"],
                                     result["boxes"])
    ]
    found.sort(key=lambda d: d["score"], reverse=True)

    return {"width": image.width, "height": image.height,
            "seconds": seconds, "detections": found}

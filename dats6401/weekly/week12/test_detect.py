# test_detect.py — Week 12: prove the detection server works
#   python test_detect.py            (while uvicorn detect_server:app is up)
#
# Four requests. The first three mirror test_endpoint.py; the fourth is the one
# the iris server could not show you.
import requests

BASE = "http://127.0.0.1:8000"

print("health:", requests.get(f"{BASE}/health", timeout=10).json())
print()

# 1. A real photo. The server returns EVERY box above its floor, sorted by
#    score -- including ones it barely believes.
with open("sample_astronaut.jpg", "rb") as f:
    r = requests.post(f"{BASE}/detect", files={"file": f}, timeout=60)
out = r.json()
print(f"image  -> {r.status_code}  {out['width']}x{out['height']} px, "
      f"model took {out['seconds'] * 1000:.0f} ms")
for d in out["detections"]:
    print(f"   {d['score']:.2f}  {d['label']}")
print("   Only the first is right. The 'knife' is a model space shuttle and the "
      "'clock' is a helmet: the model has no label for either, so it picks the "
      "nearest one it knows. The score is how you tell.")
print()

# 2. No file at all. FastAPI rejects it before detect() runs -- the same 422
#    the iris server gave a bad flower.
r = requests.post(f"{BASE}/detect", timeout=10)
print("empty  ->", r.status_code, "(expect 422: rejected before the code ran)")

# 3. A file that is not an image. This one DOES reach detect(), because no type
#    can say "is a picture". The 400 is validation the server wrote itself.
r = requests.post(f"{BASE}/detect",
                  files={"file": ("notes.txt", b"not an image", "text/plain")},
                  timeout=10)
print("text   ->", r.status_code, r.json()["detail"] if r.status_code == 400 else r.text[:100])

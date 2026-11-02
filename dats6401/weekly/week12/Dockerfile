# Dockerfile — Week 12 optional extension: ship the environment, not just the code
#
# Build and run locally:
#     docker build -t iris-server .
#     docker run -p 8000:7860 iris-server
#     # then: http://127.0.0.1:8000/docs
#
# The point of containerising this is not deployment for its own sake. It is
# that "it works on my machine" stops being a defence: the image carries the
# Python version, the libraries and the model together.

FROM python:3.12-slim

# Spaces and most PaaS hosts run the container as a non-root user with UID
# 1000. Creating that user ourselves, and copying files as them, avoids the
# permission errors that are the usual reason a first container build fails.
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH
WORKDIR $HOME/app

# Dependencies first, in their own layer: this layer is only rebuilt when
# requirements.txt changes, so editing the server does not reinstall pandas.
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY --chown=user . .

# Train the model INSIDE the image rather than copying a .joblib in.
#
# A pickle is tied to the scikit-learn that wrote it, so a model file built on
# your laptop may refuse to load in the container. Training here means the
# version that writes the model is by construction the version that reads it --
# the pinned one in requirements.txt.
RUN python train_model.py

# Which module to serve. Override at build or run time if you renamed your
# file:   docker run -e APP_MODULE=server:app ...
ENV APP_MODULE=server_skeleton:app

# 7860 is what Hugging Face Docker Spaces expect; Render, Fly and friends
# inject their own $PORT. Honouring both keeps one Dockerfile portable.
ENV PORT=7860
EXPOSE 7860

# Shell form, so ${PORT} is expanded at run time rather than taken literally.
# --host 0.0.0.0 is required: the default 127.0.0.1 is only reachable from
# inside the container, which looks exactly like a container that will not start.
CMD uvicorn $APP_MODULE --host 0.0.0.0 --port ${PORT:-7860}

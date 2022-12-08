FROM ubuntu:20.04

ENV SOURCES=/usr/project

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv

COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade build && \
    python3 -m pip install -r requirements.txt

WORKDIR $SOURCES
VOLUME ["$SOURCES"]

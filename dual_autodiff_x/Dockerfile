FROM python:3.10-slim

RUN apt-get update && apt-get install -y git gcc build-essential python3-dev

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip setuptools wheel setuptools_scm build numpy Cython

RUN pip install .

RUN python -m build
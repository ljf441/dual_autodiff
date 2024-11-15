FROM python:3.10-slim

RUN apt-get update && apt-get install -y git gcc build-essential python3-dev libffi-dev cython3

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip setuptools wheel setuptools_scm build numpy Cython

RUN python3.10 setup.py build_ext --inplace --verbose

RUN pip install -e .

RUN python -c "import dual_autodiff_x"
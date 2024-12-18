FROM python:3.10-slim

RUN apt-get update && apt-get install -y git gcc build-essential python3-dev libffi-dev

WORKDIR /app

COPY dual_autodiff_x/wheelhouse/*.whl /app/wheelhouse/

COPY wheelhouse/*.whl /app/wheelhouse

COPY requirements.txt /app/

COPY dual_autodiff.ipynb /app/

COPY tests/* /app/tests

RUN pip install --upgrade pip setuptools wheel setuptools_scm build numpy Cython

RUN pip install -r requirements.txt

RUN pip install jupyter notebook

RUN pip install mpmath

RUN find /app/wheelhouse/ -name "*.whl" ! -name "*cp311*" -exec pip install {} \;

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
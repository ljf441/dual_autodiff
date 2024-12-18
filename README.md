# dual_autodiff
Python packages for automatic differentiation using dual numbers.

# how to install
This project contains two packages:
1. `dual_autodiff`: a pure Python package for automatic differentiation using dual numbers.
2. `dual_autodiff_x`: a Cythonized package for automatic differentiation using dual numbers.

To install `dual_autodiff` as a local editable package, navigate to the root directory of this repository and type:
```
pip install -e .
```

To install `dual_autodiff` from wheels, navigate to the root directory of this repository and type:
```
pip install wheelhouse/dual_autodiff-0.0.1-py3-none-any.whl
```


Similarly, to install `dual_autodiff_x` as a local editable package, navigate to `dual_autodiff_x` and type:
```
pip install -e .
```

To install `dual_autodiff_x` from wheels, if Python 3.10 is installed, navigate to the root directory of this repository and type:

```
pip install dual_autodiff_x/wheelhouse/dual_autodiff_x-0.0.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
```

Or, if Python 3.11 is installed:
```
pip install dual_autodiff_x/wheelhouse/dual_autodiff_x-0.0.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
```

Currently, `dual_autodiff_x` is only compiled for Python 3.10 and 3.11.

# how to use with Docker
This project is able to be run using a Docker image. This environment is configured to use Python 3.10 and includes a Jupyter Notebook containing a tutorial notebook.

## steps

1. Build the Docker image within the directory.
```
docker build -t dual_autodiff-img .
```
7. Run the Docker image, making sure to allow for port usage.
```
docker run -p 8888:8888 dual_autodiff-img
```
8. This will result in Jupyter Notebook being run. You will see a URL like:
```
http://127.0.0.1:8888/?token=<token>
```
9. View this URL with a browser of your choice. Google Chrome or Firefox is recommended.
10. To stop running the container use Docker Desktop. To stop running Jupyter Notebook, type `CTRL-C` in the terminal.

## within the Docker image
The Docker image contains:
1. Jupyter Notebooks:
    - `dual_autodiff.ipynb`, covering tasks 2 and 9 of the coursework.
2. Testing suite for use with `pytest`
    - `test_dual.py`, for testing the `Dual` class in `dual_autodiff`
    - `test_dual_x.py` for testing the `Dual` class in `dual_autodiff_x`
    - `test_collection.py` for testing the `Collection` class in `dual_autodiff` 
    - `test_collection_x.py` for testing the `Collection` class in `dual_autodiff_x` 

# where to find the report
The report is located in the `report` folder and is named `report.pdf`.

# where to find the Sphinx documentation
`cd` to `docs` and run `build html`. The `.html` pages will be in `docs/_build/html`.

# where to find the wheels
- The wheels for the pure Python package are found in `wheelhouse`.
- The wheels for the Cythonized package are found in `dual_autodiff_x/wheelhouse`

# use of auto-generation tools
Auto-generation tools were used as follows:
- Parsing error messages throughout the project.
- Assistance in formatting the report in $\LaTeX$, specifically with tables and referencing.
- Code prototyping with `__array_ufunc__` and `__array_function__` so that `NumPy` functions are able to be used on `Dual` objects.
- Code alterations when Cythonizing the package.

Auto-generation tools were not used elsewhere.
from setuptools import setup, find_packages
from Cython.Build import cythonize
import numpy as np
setup(
    name="dual_autodiff_x",
    packages = find_packages(where="dual_autodiff_x"),
    ext_modules=cythonize('dual_autodiff_x/dual.pyx')
    )

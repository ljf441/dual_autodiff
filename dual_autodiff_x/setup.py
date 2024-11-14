from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    name="dual_autodiff_x",
    ext_modules=cythonize('dual_autodiff_x/dual.pyx')
    )

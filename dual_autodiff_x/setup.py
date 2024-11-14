from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import numpy as np
import sys

ext_modules = [
    Extension(
        name = "dual_autodiff_x",
        sources = ["dual_autodiff_x/dual.pyx"],
        include_dirs = [np.get_include()],
    )
]
setup(
    name="dual_autodiff_x",
    version ="0.0.1",
    description="A Python package for automatic differentiation using dual numbers.",
    packages = ["dual_autodiff_x/dual_autodiff_x"],
    ext_modules=cythonize(ext_modules),
    python_requires=">=3.10"
    )

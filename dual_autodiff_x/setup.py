from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import numpy as np

ext_modules = [
    Extension(
        name="dual_autodiff_x.dual",  
        sources=["dual_autodiff_x/dual.pyx"], 
        include_dirs=[np.get_include()],  
    )
]

setup(
    name="dual_autodiff_x",
    version="0.0.1",
    description="A Python package for automatic differentiation using dual numbers.",
    python_requires=">=3.10",
    packages=find_packages(), 
    ext_modules=cythonize(ext_modules),
    include_dirs=[np.get_include()],
    zip_safe=False,
)

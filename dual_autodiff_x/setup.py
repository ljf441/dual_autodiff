from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy as np

ext_modules = [
    Extension(name="src.dual_autodiff_x.dual", sources=["src/dual_autodiff_x/dual.pyx"], 
        include_dirs=[np.get_include()],  
    )
]

setup(
    name="dual_autodiff_x",
    version="0.0.1",
    description="A Python package for automatic differentiation using dual numbers.",
    python_requires=">=3.10",
    packages=["dual_autodiff_x"], 
    package_dir={"":"."},
    ext_modules=cythonize(ext_modules, compiler_directives={'language_level':"3"}),
    zip_safe=False,
    package_data={"dual_autodiff_x": ["*.so"]},
    exclude_package_data={"dual_autodiff_x": ["*.pyx"]},
)

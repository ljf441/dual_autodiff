from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy as np

ext_modules = [
    Extension("dual_autodiff_x.dual", ["src/dual_autodiff_x/dual.pyx"]),
]

setup(
    # name="dual_autodiff_x",
    # version="0.0.1",
    # description="A Python package for automatic differentiation using dual numbers.",
    # python_requires=">=3.10",
    # cmdclass={"build_ext": build_ext},
    packages=["dual_autodiff_x"], 
    package_dir={"":"src"},
    ext_modules=cythonize(ext_modules, compiler_directives={'language_level':"3"}),
    # include_dirs=[np.get_include()],
    zip_safe=False,
    package_data={"dual_autodiff_x": ["*.so"]},
    exclude_package_data={"dual_autodiff_x": ["*.pyx"]},
)

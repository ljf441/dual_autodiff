from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    name="dual_autodiff_x",
    ext_modules=cythonize('dual_autodiff_x/dual.pyx', compiler_directives={'language_level': "3"}),
    install_requires=['numpy', 'cython'],
    packages=['dual_autodiff_x'],
    include_dirs=[np.get_include()],
    setup_requires=['cython'],
)

# dual_autodiff/__init__.py
from .dual import Dual
import numpy as np

def cos(x):
    if isinstance(x, Dual):
        return x.cos()
    return np.cos(x)

def sin(x):
    if isinstance(x, Dual):
        return x.sin()
    return np.sin(x)

def tan(x):
    if isinstance(x, Dual):
        return x.tan()
    return np.tan(x)

def log(x):
    if isinstance(x, Dual):
        return x.log()
    return np.log(x)

def exp(x):
    if isinstance(x, Dual):
        return x.exp()
    return np.exp(x)
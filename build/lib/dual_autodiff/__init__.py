# dual_autodiff/__init__.py
from .dual import Dual, Collection
import numpy as np
import mpmath as mp

__all__ = ['Dual', 'Collection']
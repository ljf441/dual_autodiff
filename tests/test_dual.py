import pytest
import numpy as np
from dual_autodiff.dual import Dual

def test_dual_init():
    x = Dual(1, 2)

    assert x.real == 1
    assert x.dual == 2

def test_dual_cos():
    x = Dual(1, 1)
    y = x.cos()
    
    assert np.isclose(y.real, np.cos(1))
    assert np.isclose(y.dual, -np.sin(1))

def test_cos_derivative():
    x = Dual(0, 1)
    y = x.cos()

    assert np.isclose(y.real, np.cos(0))
    assert np.isclose(y.dual, -np.sin(0))    

def test_cos_neg():
    x = Dual(-1, 1)
    y = x.cos()

    assert np.isclose(y.real, np.cos(-1))
    assert np.isclose(y.dual, -np.sin(-1))

def test_dual_sin():
    x = Dual(1, 1)
    y = x.sin()

    assert np.isclose(y.real, np.sin(1))
    assert np.isclose(y.dual, np.cos(1))

def test_sin_derivative():
    x = Dual(0, 1)
    y = x.sin()

    assert np.isclose(y.real, np.sin(0))
    assert np.isclose(y.dual, np.cos(0))    

def test_sin_neg():
    x = Dual(-1, 1)
    y = x.sin()

    assert np.isclose(y.real, np.sin(-1))
    assert np.isclose(y.dual, np.cos(-1))


def test_dual_tan():
    x = Dual(1, 1)
    y = x.tan()

    assert np.isclose(y.real, np.tan(1))
    assert np.isclose(y.dual, (1/np.cos(1)**2))

def test_tan_derivative():
    x = Dual(0, 1)
    y = x.tan()

    assert np.isclose(y.real, np.tan(0))
    assert np.isclose(y.dual, (1/np.cos(0)**2))    

def test_tan_neg():
    x = Dual(-1, 1)
    y = x.tan()

    assert np.isclose(y.real, np.tan(-1))
    assert np.isclose(y.dual, (1/np.cos(-1)**2))


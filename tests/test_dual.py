import pytest
import numpy as np
from dual_autodiff.dual import Dual

def test_dual_init():
    x = Dual(1, 2)

    assert x.real == 1
    assert x.dual == 2

def test_dual_add():
    x = Dual(1, 2)
    y = Dual(3, 4)
    z = x + y

    assert z.real == 4
    assert z.dual == 6

def test_add():
    x = Dual(1, 2)
    y = x + 3
    
    assert y.real == 4
    assert y.dual == 2

def test_dual_sub():
    x = Dual(1, 4)
    y = Dual(2, 3)
    z = x - y

    assert z.real == -1
    assert z.dual == 1

def test_sub():
    x = Dual(1, 2)
    y = x - 3

    assert y.real == -2
    assert y.dual == 2

def test_dual_mul():
    x = Dual(1, 2)
    y = Dual(3, 4)
    z = x * y

    assert z.real == 3
    assert z.dual == 10

def test_mul():
    x = Dual(1, 2)
    y = x * 3

    assert y.real == 3
    assert y.dual == 6

def test_dual_div():
    x = Dual(6, 2)
    y = Dual(3, 1)
    z = x / y

    assert z.real == 2
    assert z.dual == 0

def test_div():
    x = Dual(6, 2)
    y = x / 2

    assert y.real == 3
    assert y.dual == 1

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

def test_dual_log():
    x = Dual(1, 2)
    y = x.log()

    assert np.isclose(y.real, np.log(1))
    assert np.isclose(y.dual, 2)

def test_log_neg():
    x = Dual(-1, 1)
    with pytest.raises(Exception, match="Logarithm is undefined for non-positive real numbers."):x.log()

def test_log_zero():
    x = Dual(0,1)
    with pytest.raises(Exception, match="Logarithm is undefined for non-positive real numbers."):x.log()

def test_dual_exp():
    x = Dual(1,2)
    y = x.exp()

    assert np.isclose(y.real, np.exp(1))
    assert np.isclose(y.dual, 2*np.exp(1))

def test_dual_exp_neg():
    x = Dual(-1,2)
    y = x.exp()

    assert np.isclose(y.real, np.exp(-1))
    assert np.isclose(y.dual, 2*np.exp(-1))

def test_pow():
    x = Dual(2, 3)
    y = x**2

    assert np.isclose(y.real, 4)
    assert np.isclose(y.dual, 2 * 2**(2-1) * 3)

def test_dual_pow():
    x = Dual(2, 2)
    y = Dual(3, 4)
    z = x**y

    assert np.isclose(z.real, 8)
    assert np.isclose(z.dual, 3*2**(3-1)*4 + 8*np.log(2)*4)
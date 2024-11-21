import pytest
import numpy as np
import mpmath as mp
from dual_autodiff_x.dual import Dual

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

def test_radd():
    x = Dual(1, 2)
    y = 3 + x

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

def test_rsub():
    x = Dual(1, 3)
    y = 3 - x

    assert y.real == 2
    assert y.dual == -3

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

def test_rmul():
    x = Dual(1, 2)
    y = 3*x

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

def test_rdiv():
    x = Dual(3, 2)
    y = 6 / x

    assert y.real == 2
    assert np.isclose(y.dual, -(6*2) / (3**2))

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

def test_dual_arccos():
    x = Dual(0.5, 1)
    y = x.arccos()

    assert np.isclose(y.real, np.arccos(0.5))
    assert np.isclose(y.dual, -1/np.sqrt(1-0.5**2))

def test_dual_cosh():
    x = Dual(1, 1)
    y = x.cosh()

    assert np.isclose(y.real, np.cosh(1))
    assert np.isclose(y.dual, -np.sinh(1))

def test_dual_arccosh():
    x = Dual(2, 1)
    y = x.arccosh()

    assert np.isclose(y.real, np.arccosh(2))
    assert np.isclose(y.dual, 1/np.sqrt(2**2 - 1))

def test_dual_sec():
    x = Dual(1, 1)
    y = x.sec()

    assert np.isclose(y.real, float(mp.sec(1)))
    assert np.isclose(y.dual, float(-np.tan(1)*mp.sec(1)))

def test_dual_arcsec():
    x = Dual(2, 1)
    y = x.arcsec()

    assert np.isclose(y.real, float(mp.asec(2)))
    assert np.isclose(y.dual, 1/(2**2 * np.sqrt(1 - 1/2**2)))

def test_dual_sech():
    x = Dual(1, 1)
    y = x.sech()
    assert np.isclose(y.real, float(mp.sech(1)))
    assert np.isclose(y.dual, float(-mp.tanh(1)*mp.sech(1)))

def test_dual_arcsech():
    x = Dual(0.5, 1)
    y = x.arcsech()
    assert np.isclose(y.real, float(mp.asech(0.5)))
    assert np.isclose(y.dual, -1/(0.5 * np.sqrt(1 - 0.5**2)))

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

def test_dual_arcsin():
    x = Dual(0.5, 1)
    y = x.arcsin()

    assert np.isclose(y.real, np.arcsin(0.5))
    assert np.isclose(y.dual, 1/(np.sqrt(1-0.5**2)))

def test_dual_sinh():
    x = Dual(1, 1)
    y = x.sinh()

    assert np.isclose(y.real, np.sinh(1))
    assert np.isclose(y.dual, np.cosh(1))

def test_dual_arcsinh():
    x = Dual(0.5, 1)
    y = x.arcsinh()

    assert np.isclose(y.real, np.arcsinh(0.5))
    assert np.isclose(y.dual, 1/(np.sqrt(1+0.5**2)))

def test_dual_csc():
    x = Dual(0.5, 1)
    y = x.csc()

    assert np.isclose(y.real, float(mp.csc(0.5)))
    assert np.isclose(y.dual, float(-mp.cot(0.5)*mp.csc(0.5)))

def test_dual_arccsc():
    x = Dual(2, 1)
    y = x.arccsc()

    assert np.isclose(y.real, float(mp.acsc(2)))
    assert np.isclose(y.dual, -1/(2*np.sqrt(2**2 - 1)))

def test_dual_csch():
    x = Dual(2, 1)
    y = x.csch()

    assert np.isclose(y.real, float(mp.csch(2)))
    assert np.isclose(y.dual, float(-mp.coth(2)*mp.csch(2)))

def test_dual_arccsch():
    x = Dual(2, 1)
    y = x.arccsch()

    assert np.isclose(y.real, float(mp.acsch(2)))
    assert np.isclose(y.dual, -1/(2**2 * np.sqrt(1 + 1/2**2)))

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

def test_dual_arctan():
    x = Dual(0.5, 1)
    y = x.arctan()

    assert np.isclose(y.real, np.arctan(0.5))
    assert np.isclose(y.dual, 1/(1+0.5**2))

def test_dual_tanh():
    x = Dual(1, 1)
    y = x.tanh()

    assert np.isclose(y.real, np.tanh(1))
    assert np.isclose(y.dual, 1/np.cosh(1)**2)

def test_dual_arctanh():
    x = Dual(0.5, 1)
    y = x.arctanh()

    assert np.isclose(y.real, float(mp.atanh(0.5)))
    assert np.isclose(y.dual, 1/(1-0.5**2))

def test_dual_cot():
    x = Dual(1, 1)
    y = x.cot()

    assert np.isclose(y.real, float(mp.cot(1)))
    assert np.isclose(y.dual, float(-mp.csc(1)**2))

def test_dual_arccot():
    x = Dual(2, 1)
    y = x.arccot()

    assert np.isclose(y.real, float(mp.acot(2)))
    assert np.isclose(y.dual, -1/(1+2**2))

def test_dual_coth():
    x = Dual(1, 1)
    y = x.coth()
    
    assert np.isclose(y.real, float(mp.coth(1)))
    assert np.isclose(y.dual, float(-mp.csch(1)**2))

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

def test_rpow():
    x = Dual(2, 3)
    y = 2**x

    assert np.isclose(y.real, 4)
    assert np.isclose(y.dual, 2**2 * 3 * np.log(2))

def test_dual_zero_init():
    x = Dual(0,0)
    y = x + 1

    assert y.real == 1
    assert y.dual == 0

def test_floordiv():
    x = Dual(5,5)
    y = x//2

    assert y.real == 2
    assert y.dual == 2

def test_dual_floordiv():
    x = Dual(5,4)
    y = Dual(2, 3)
    z = x//y

    assert z.real == 2
    assert z.dual == (5*2 - 4*3)//3**2

def test_rfloordiv():
    x = Dual(2,2)
    y = 5//x
    
    assert y.real == 2
    assert y.dual == -5*2 // 2**2

import pytest
import numpy as np
import mpmath as mp
from dual_autodiff_x.dual import Dual, Collection

def test_collection_init():
    x = Dual(1, 2)
    y = Dual(3, 4)
    vars = Collection([x, y])

    assert vars[0] == x
    assert vars[1] == y

def test_collection_add():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars1 = Collection([x, y])
    
    a = Dual(3, 7)
    b = Dual(4, 8)
    vars2 = Collection([a, b])

    result = vars1 + vars2
    compare = Collection([Dual(4, 12), Dual(6, 14)])
    
    assert result == compare

def test_dual_add():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    a = Dual(3, 7)

    result = vars + a
    compare = Collection([Dual(4, 12), Dual(5, 13)])

    assert result == compare

def test_real_add():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])

    result = vars + 2
    compare = Collection([Dual(3, 5), Dual(4, 6)])

    assert result == compare

def test_dual_radd():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    a = Dual(3, 7)

    result = a + vars
    compare = Collection([Dual(4, 12), Dual(5, 13)])

    assert result == compare

def test_real_radd():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])

    result = 2 + vars 
    compare = Collection([Dual(3, 5), Dual(4, 6)])

    assert result == compare

def test_collection_sub():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars1 = Collection([x, y])
    
    a = Dual(3, 7)
    b = Dual(4, 8)
    vars2 = Collection([a, b])

    result = vars1 - vars2
    compare = Collection([Dual(-2, -2), Dual(-2, -2)])
    
    assert result == compare

def test_dual_sub():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    a = Dual(3, 7)

    result = vars - a
    compare = Collection([Dual(-2, -2), Dual(-1, -1)])

    assert result == compare

def test_real_sub():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])

    result = vars - 2
    compare = Collection([Dual(-1, 5), Dual(0, 6)])

    assert result == compare

def test_dual_rsub():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    a = Dual(3, 7)

    result = a - vars
    compare = Collection([Dual(2, 2), Dual(1, 1)])

    assert result == compare

def test_real_rsub():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])

    result = 2 - vars 
    compare = Collection([Dual(1, -5), Dual(0, -6)])

    assert result == compare

def test_collection_mul():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars1 = Collection([x, y])
    
    a = Dual(3, 7)
    b = Dual(4, 8)
    vars2 = Collection([a, b])

    result = vars1 * vars2
    compare = Collection([Dual(3, 22), Dual(8, 40)])
    
    assert result == compare

def test_dual_mul():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    a = Dual(3, 7)

    result = vars * a
    compare = Collection([Dual(3, 22), Dual(6, 32)])

    assert result == compare

def test_real_mul():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])

    result = vars * 2
    compare = Collection([Dual(2, 10), Dual(4, 12)])

    assert result == compare

def test_dual_rmul():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    a = Dual(3, 7)

    result = a * vars
    compare = Collection([Dual(3, 22), Dual(6, 32)])

    assert result == compare

def test_real_rmul():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])

    result = 2 * vars 
    compare = Collection([Dual(2, 10), Dual(4, 12)])

    assert result == compare

def test_collection_div():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars1 = Collection([x, y])
    
    a = Dual(3, 7)
    b = Dual(4, 8)
    vars2 = Collection([a, b])

    result = vars1 / vars2
    compare = Collection([Dual(1/3, (5*3-1*7)/7**2), Dual(2/4, (6*4-2*8)/8**2)])
    
    assert result == compare

def test_dual_div():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    a = Dual(3, 7)

    result = vars / a
    compare = Collection([Dual(1/3, (5*3-1*7)/7**2), Dual(2/3, (6*3-2*7)/7**2)])

    assert result == compare

def test_real_div():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])

    result = vars / 2
    compare = Collection([Dual(1/2, 5/2), Dual(1, 3)])

    assert result == compare

def test_dual_rdiv():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    a = Dual(3, 7)

    result = a / vars
    compare = Collection([Dual(3/1, (7*1-3*5)/5**2), Dual(3/2, (7*2-3*6)/6**2)])

    assert result == compare

def test_real_rdiv():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])

    result = 2 / vars 
    compare = Collection([Dual(2, -2*5), Dual(1, (-2*6)/2**2)])

    assert result == compare

def test_collection_floordiv():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars1 = Collection([x, y])
    
    a = Dual(3, 7)
    b = Dual(4, 8)
    vars2 = Collection([a, b])

    result = vars1 // vars2
    compare = Collection([Dual(1//3, (5*3-1*7)//7**2), Dual(2//4, (6*4-2*8)//8**2)])
    
    assert result == compare

def test_dual_floordiv():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    a = Dual(3, 7)

    result = vars // a
    compare = Collection([Dual(1//3, (5*3-1*7)//7**2), Dual(2//3, (6*3-2*7)//7**2)])

    assert result == compare

def test_real_floordiv():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])

    result = vars // 2
    compare = Collection([Dual(1//2, 5//2), Dual(1, 3)])

    assert result == compare

def test_dual_rfloordiv():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    a = Dual(3, 7)

    result = a // vars
    compare = Collection([Dual(3//1, (7*1-3*5)//5**2), Dual(3//2, (7*2-3*6)//6**2)])

    assert result == compare

def test_real_rfloordiv():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])

    result = 2 // vars 
    compare = Collection([Dual(2, -2*5), Dual(1, (-2*6)//2**2)])

    assert result == compare

def test_collection_pow():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars1 = Collection([x, y])
    
    a = Dual(3, 7)
    b = Dual(4, 8)
    vars2 = Collection([a, b])

    result = vars1 ** vars2
    compare = Collection([x**a, y**b])

    assert result == compare

def test_dual_pow():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    a = Dual(3, 7)

    result = vars ** a
    compare = Collection([x**a, y**a])

    assert result == compare

def test_real_pow():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    result = vars ** 2
    compare = Collection([x**2, y**2])

    assert result == compare

def test_dual_rpow():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    a = Dual(3, 7)

    result = a**vars
    compare = Collection([a**x, a**y])

    assert result == compare

def test_real_rpow():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    result = 2**vars
    compare = Collection([2**x, 2**y])

    assert result == compare

def test_collection_cos():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    result = vars.cos()
    compare = Collection([x.cos(), y.cos()])

    assert result == compare

def test_collection_arccos():
    x = Dual(0.1, 5)
    y = Dual(0.2, 6)
    vars = Collection([x, y])
    
    result = vars.arccos()
    compare = Collection([x.arccos(), y.arccos()])

    assert result == compare

def test_collection_cosh():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    result = vars.cosh()
    compare = Collection([x.cosh(), y.cosh()])

    assert result == compare

def test_collection_arccosh():
    x = Dual(2, 5)
    y = Dual(3, 6)
    vars = Collection([x, y])
    
    result = vars.arccosh()
    compare = Collection([x.arccosh(), y.arccosh()])

    assert result == compare

def test_collection_sec():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    result = vars.sec()
    compare = Collection([x.sec(), y.sec()])

    assert result == compare

def test_collection_arcsec():
    x = Dual(2, 5)
    y = Dual(3, 6)
    vars = Collection([x, y])
    
    result = vars.arcsec()
    compare = Collection([x.arcsec(), y.arcsec()])

def test_collection_sech():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    result = vars.sech()
    compare = Collection([x.sech(), y.sech()])

def test_collection_arcsech():
    x = Dual(0.1, 5)
    y = Dual(0.2, 6)
    vars = Collection([x, y])
    
    result = vars.arcsech()
    compare = Collection([x.arcsech(), y.arcsech()])

def test_collection_sin():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    result = vars.sin()
    compare = Collection([x.sin(), y.sin()])

    assert result == compare

def test_collection_arcsin():
    x = Dual(0.1, 5)
    y = Dual(0.2, 6)
    vars = Collection([x, y])
    
    result = vars.arcsin()
    compare = Collection([x.arcsin(), y.arcsin()])

    assert result == compare

def test_collection_sinh():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    result = vars.sinh()
    compare = Collection([x.sinh(), y.sinh()])

    assert result == compare

def test_collection_arcsinh():
    x = Dual(0.1, 5)
    y = Dual(0.2, 6)
    vars = Collection([x, y])
    
    result = vars.arcsinh()
    compare = Collection([x.arcsinh(), y.arcsinh()])

    assert result == compare

def test_collection_csc():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    result = vars.csc()
    compare = Collection([x.csc(), y.csc()])

    assert result == compare

def test_collection_arccsc():
    x = Dual(2, 5)
    y = Dual(3, 6)
    vars = Collection([x, y])
    
    result = vars.arccsc()
    compare = Collection([x.arccsc(), y.arccsc()])

def test_collection_csch():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    result = vars.csch()
    compare = Collection([x.csch(), y.csch()])

def test_collection_arccsch():
    x = Dual(0.1, 5)
    y = Dual(0.2, 6)
    vars = Collection([x, y])
    
    result = vars.arccsch()
    compare = Collection([x.arccsch(), y.arccsch()])

def test_collection_tan():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    result = vars.tan()
    compare = Collection([x.tan(), y.tan()])

    assert result == compare

def test_collection_arctan():
    x = Dual(0.1, 5)
    y = Dual(0.2, 6)
    vars = Collection([x, y])
    
    result = vars.arctan()
    compare = Collection([x.arctan(), y.arctan()])

    assert result == compare

def test_collection_tanh():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    result = vars.tanh()
    compare = Collection([x.tanh(), y.tanh()])

    assert result == compare

def test_collection_arctanh():
    x = Dual(0.1, 5)
    y = Dual(0.2, 6)
    vars = Collection([x, y])
    
    result = vars.arctanh()
    compare = Collection([x.arctanh(), y.arctanh()])

    assert result == compare

def test_collection_cot():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    result = vars.cot()
    compare = Collection([x.cot(), y.cot()])

    assert result == compare

def test_collection_arccot():
    x = Dual(2, 5)
    y = Dual(3, 6)
    vars = Collection([x, y])
    
    result = vars.arccot()
    compare = Collection([x.arccot(), y.arccot()])

def test_collection_coth():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    result = vars.coth()
    compare = Collection([x.coth(), y.coth()])

def test_collection_log():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    result = vars.log()
    compare = Collection([x.log(), y.log()])

def test_collection_exp():
    x = Dual(1, 5)
    y = Dual(2, 6)
    vars = Collection([x, y])
    
    result = vars.exp()
    compare = Collection([x.exp(), y.exp()])
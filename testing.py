import dual_autodiff as df
from dual_autodiff import Dual, Collection
import numpy as np
x = df.Dual(1, 4)
y = df.Dual(2, 5)
z = df.Dual(3, 6)
vars = df.Collection([x, y, z])
vars2 = df.Collection([x, y, z])
print("vars")
print(vars)
print(".sin")
print(vars.sin())
print("np.sin")
print(np.sin(vars2))
print("vars*vars2")
print(vars*vars2)
print("vars*x, x*vars")
print(vars*x)
print(x * vars)
print("vars*2, 2*vars")
print(vars*2)
print(2*vars)
print("other")
def f(x, y, z):
    return x**2 + y.sin()  + z**2
print(x.partial(f, x, y, z))
print(y.partial(f, x, y, z))
import dual_autodiff as df
import numpy as np
x = df.Dual(1, 1)
y = df.Dual(2, 2)
z = df.Dual(3, 3)
vars = np.array([x, y, z])
vars2 = [x, y, z]
#print(vars*2)
print(vars2.sin())
print(np.sin(vars))
def f(x, y, z):
    return x**2 + y.sin()  + z**2
print(x.partial(f, x, y, z))
print(y.partial(f, x, y, z))

import numpy as np

class Dual:
    """
    A class to implement dual numbers.

    Attributes:
        real (float): real part of dual number.
        dual (float: dual part of dual number.
    """

    def __init__(self, real, dual):
        """
        Initialises Dual with given parameters.

        Parameters:
            real (float): real part of dual number.
            dual (float): dual part of dual number.
        """
        self.real = real
        self.dual = dual

    def __call__(self):
        return self.real

    def __add__(self, x):
        """
        Implements addition.
        """
        if isinstance(x, Dual):
            return Dual(self.real+x.real, self.dual+x.dual)
        else:
            return Dual(self.real + x, self.dual)
        
    def __sub__(self, x):
        """
        Implements subtraction.
        """
        if isinstance(x, Dual):
            return Dual(self.real-x.real, self.dual-x.dual)
        else:
            return Dual(self.real-x, self.dual)

    def __mul__(self, x):
        """
        Implements multiplication.
        """
        if isinstance(x, Dual):
            R_real = self.real*x.real
            R_dual = self.real*x.dual + self.dual*x.real
            return Dual(R_real, R_dual)
        else:
            return Dual(self.real*x, self.dual*x)
    
    def __truediv__(self, x):
        """
        Implements division.
        """
        if isinstance(x, Dual):
            if x.real == 0:
                raise ZeroDivisionError("Denominator is zero")
            R_real = self.real/x.real
            R_dual = (self.dual*x.real - self.real*x.dual)/(x.dual**2)
            return Dual(R_real, R_dual)
        else:
            if x == 0:
                raise ZeroDivisionError("Denominator is zero")
            return Dual(self.real/x, self.dual/x)

    def sin(self):
        """
        Implements sine function.
        """
        return Dual(np.sin(self.real), self.dual*np.cos(self.real))
    
    def cos(self):
        """
        Implements cosine function.
        """
        return Dual(np.cos(self.real), - self.dual*np.sin(self.real))

    def tan(self):
        """
        Implements tangent function.
        """
        return Dual(np.tan(self.real), self.dual*(1/np.cos(self.real))**2)

    def log(self):
        """
        Implements natural logarithm function.
        """
        if self.real <=0:
            raise Exception("Logarithm is undefined for negative real parts")
        return Dual(np.log(self.real), self.dual/self.real)

    def exp(self):
        return Dual(np.exp(self.real), self.dual*(np.exp(self.real)))

    def pow(self, x):
        if isinstance(x, Dual):
            R_real = self.real**x.real
            R_dual = (self.real**x.real) * (x.dual * np.log(self.real) + self.dual*x.real/self.real)
        else:
            R_real = self.real**x
            R_dual = self.dual*x*(self.real ** (x - 1))
            return Dual()
        return Dual(R_real, R_dual)
    
    def __repr__(self):
        """
        String representation of dual number.
        """
        if self.dual < 0:
            return f"({self.real} - {abs(self.dual)}\u03B5)"
        else:
            return f"({self.real} + {self.dual}\u03B5)"
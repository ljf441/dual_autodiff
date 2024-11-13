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

    def __add__(self, value):
        """
        Implements addition.
        """   
        return Dual(self.real+value.real, self.dual+value.real)
    def __sub__(self, value):
        """
        Implements subtraction.
        """
        return Dual(self.real-value.real, self.dual-value.dual)
    def __mul__(self, value):
        """
        Implements multiplication.
        """
        R_real = self.real*value.real
        R_dual = self.real*value.dual + self.dual*value.real
        return Dual(R_real, R_dual)
    def __truediv__(self, value):
        """
        Implements division.
        """
        if(value.real) !=0 :
            num = self.real*value.real - self.real*value.dual + self.dual*value.real
            den = value.real*value.real
            R_real = self.real/value.real
            R_dual = (self.dual*value.real - self.real*value.dual)/(value.dual**2)
            return Dual(R_real, R_dual)
        else:
            raise Exception("Denominator is zero")

    def __sin___(self):
        """
        Implements sine function.
        """
        return np.sin(self.real) + self.dual*np.cos(self.real)
    
    def __cos__(self):
        """
        Implements cosine function.
        """
        return np.cos(self.real) - self.dual*np.sin(self.real)

    def __tan__(self):
        """
        Implements tangent function.
        """
        return np.tan(self.real) + self.dual*(1/np.cos(self.real))**2

    def __log__(self):
        return

    def __exp__(self):
        return Dual(np.exp**self.real, np.exp**self.real * (self.dual*np.log(np.exp)))

    def __pow__(self, value):
        return Dual(self.real**value.real, self.real**(value.real-1) * (self.real*self.dual*np.log(self.real)+value.real*self.dual))
        #return Dual(self.real**value.real, self.real**value.real * (value.dual * np.log(self.real) + self.dual*value.real/self.real))

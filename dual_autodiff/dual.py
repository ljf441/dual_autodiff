import numpy as np

class Dual:
    """
    A class to implement dual numbers.

    Attributes:
        real (int, float): real part of dual number.
        dual (int, float): dual part of dual number.

    Methods:
        __add__(self, x): Adds two dual numbers.
        __sub__(self, x): Subtracts two dual numbers.
        __mul__(self, x): Multiplies two dual numbers.
        __truediv__(self, x): Divides two dual numbers.
        sin(self): Computes the sine of the dual number.
        cos(self): Computes the cosine of the dual number.
        tan(self): Computes the tangent of the dual number.
        log(self): Computes the natural logarithm of the dual number.
        exp(self): Computes the exponential of the dual number.
        __pow__(self, x): Raises the dual number to the power of another dual number.
        __repr__(self): Returns a string representation of the dual number.
    """

    def __init__(self, real, dual):
        """
        Initialises Dual with given parameters.

        Parameters:
            real (int, float): real part of dual number.
            dual (int, float): dual part of dual number.
        """
        self.real = real
        self.dual = dual

    def __add__(self, x):
        """
        Adds two dual numbers or a dual number and a real number.

        Parameters:
        x (Dual, float): The other dual number or a real number.

        Returns:
            Dual: A dual number of the sum.
        """
        if isinstance(x, Dual):
            return Dual(self.real+x.real, self.dual+x.dual)
        else:
            return Dual(self.real + x, self.dual)
        
    def __radd__(self, x):
        """
        Reverse additiion: adds a real number and a dual number.

        Parameters:
        x (Dual, float): The real number.

        Returns:
            Dual: A dual number of the sum.
        """
        return Dual(self.real+x, self.dual)
        
    def __sub__(self, x):
        """
        Subtracts a dual number from another or subtracts a real number from a dual number.
        
        Parameters:
        x (Dual, float): The other dual number or a real number.

        Returns:
            Dual: A dual number of the subtraction.
        """
        if isinstance(x, Dual):
            return Dual(self.real-x.real, self.dual-x.dual)
        else:
            return Dual(self.real-x, self.dual)
        
    def __rsub__(self, x):
        """
        Reverse subtraction: subtracts a dual number from a real number.

        Parameters:
        x (Dual, float): The real number.

        Returns:
            Dual: A dual number of the subtraction.
        """
        return Dual(x - self.real, -self.dual)

    def __mul__(self, x):
        """
        Multiplies two dual numbers or a dual number and a real number.
        
        Parameters:
        x (Dual, float): The other dual number or a real number.

        Returns:
            Dual: A dual number of the multiplication.
        """
        if isinstance(x, Dual):
            R_real = self.real*x.real
            R_dual = self.real*x.dual + self.dual*x.real
            return Dual(R_real, R_dual)
        else:
            return Dual(self.real*x, self.dual*x)
    
    def __rmul__(self, x):
        """
        Reverse multiplication: multiplies a real number and a dual number.

        Parameters:
        x (Dual, float): The real number.

        Returns:
            Dual: A dual number of the multiplication.
        """
        return Dual(self.real*x, self.dual*x)
    
    def __truediv__(self, x):
        """
        Divides one dual number with another dual number or a real number.

        Parameters:
        x (Dual, float): The other dual number or a real number.

        Returns:
            Dual: A dual number of the division.
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
        
    def __rtruediv__(self, x):
        """
        Reverse division: divides a real number with a dual number.

        Parameters:
        x (Dual, float): The real number.

        Returns:
            Dual: A dual number of the division.
        """
        if self.real == 0:
            raise ZeroDivisionError("Denominator is zero")
        R_real = x/self.real
        R_dual = -x*self.dual / self.real**2
        return Dual(R_real, R_dual)

    def sin(self):
        """
        Computes sine of the dual number.

        Returns:
            Dual: A dual number of the sine.
        """
        return Dual(np.sin(self.real), self.dual*np.cos(self.real))
    
    def cos(self):
        """
        Computes cosine of the dual number.

        Returns:
            Dual: A dual number of the cosine.
        """
        return Dual(np.cos(self.real), - self.dual*np.sin(self.real))

    def tan(self):
        """
        Computes tangent of the dual number.

        Returns:
            Dual: A dual number of the tangent.
        """
        return Dual(np.tan(self.real), self.dual*(1/np.cos(self.real))**2)

    def log(self):
        """
        Computes natural logarithm of the dual number.

        Returns:
            Dual: A dual number of the natural logarithm.
        """
        if self.real <=0:
            raise Exception("Logarithm is undefined for non-positive real numbers.")
        return Dual(np.log(self.real), self.dual/self.real)

    def exp(self):
        """
        Computes exponential of the dual number.

        Returns:
            Dual: A dual number of the exponential.
        """
        return Dual(np.exp(self.real), self.dual*(np.exp(self.real)))

    def __pow__(self, x):
        """
        Raises a dual number to the power of another dual number or a real number.

        Parameters:
        x (Dual, float): The other dual number or a real number.

        Returns:
            Dual: A dual number of the power.
        """
        if isinstance(x, Dual):
            R_real = self.real**x.real
            R_dual = x.real*self.real**(x.real - 1) * x.dual + (self.real**x.real)*np.log(self.real)*x.dual
        else:
            R_real = self.real**x
            R_dual = (x*self.real**(x - 1)) * self.dual
        return Dual(R_real, R_dual)
    
    def __rpow__(self, x):
        """
        Raises a real number to the power of a dual number.

        Parameters:
        x (Dual, float): The real number.

        Returns:
            Dual: A dual number of the multiplication.
        """
        return Dual(x**self.real, x**self.real * self.dual * np.log(x))
    
    def __repr__(self):
        """
        String representation of dual number.

        Returns:
            string: formatted string representation of dual number
        """
        return f"Dual(real={self.real}, dual={self.dual})"


@staticmethod
def cos(x):
    """
    Implements cosine function depending if x is a dual number or not.

    Parameters:
            x (Dual or real): dual number or real number.

        Returns:
            Dual: the cosine of the input, either as a dual number or real number.
    """
    if isinstance(x, Dual):
        return x.cos()
    return np.cos(x)

@staticmethod
def sin(x):
    """
    Implements sine function depending if x is a dual number or not.
    
    Parameters:
            x (Dual or real): dual number or real number.

        Returns:
            Dual: the sine of the input, either as a dual number or real number.
    """
    if isinstance(x, Dual):
        return x.sin()
    return np.sin(x)

@staticmethod
def tan(x):
    """
    Implements tangent function depending if x is a dual number or not.
    
    Parameters:
            x (Dual or real): dual number or real number.

        Returns:
            Dual: the tangent of the input, either as a dual number or real number.
    """
    if isinstance(x, Dual):
        return x.tan()
    return np.tan(x)

@staticmethod
def log(x):
    """
    Implements logarithm function depending if x is a dual number or not.

    Parameters:
            x (Dual or real): dual number or real number.

        Returns:
            Dual: the natural logarithm of the input, either as a dual number or real number.
    """
    if isinstance(x, Dual):
        return x.log()
    return np.log(x)

@staticmethod
def exp(x):
    """
    Implements exponential function depending if x is a dual number or not.
    
    Parameters:
            x (Dual or real): dual number or real number.

        Returns:
            Dual: the exponential of the input, either as a dual number or real number.
    """
    if isinstance(x, Dual):
        return x.exp()
    return np.exp(x)
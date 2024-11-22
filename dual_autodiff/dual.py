import numpy as np
import mpmath as mp

class Dual:
    """
    A class to implement dual numbers.

    Attributes:
        real (int, float): real part of dual number.
        dual (int, float): dual part of dual number.
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
        x (Dual, int, real): The other dual number or a real number.

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
        x (Dual, int, float): The real number.

        Returns:
            Dual: A dual number of the sum.
        """
        return Dual(self.real+x, self.dual)
        
    def __sub__(self, x):
        """
        Subtracts a dual number from another or subtracts a real number from a dual number.
        
        Parameters:
        x (Dual, int, float): The other dual number or a real number.

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
        x (Dual, int, float): The real number.

        Returns:
            Dual: A dual number of the subtraction.
        """
        return Dual(x - self.real, -self.dual)

    def __mul__(self, x):
        """
        Multiplies two dual numbers or a dual number and a real number.
        
        Parameters:
        x (Dual, int, float): The other dual number or a real number.

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
        x (Dual, int, float): The real number.

        Returns:
            Dual: A dual number of the multiplication.
        """
        return Dual(self.real*x, self.dual*x)
    
    def __truediv__(self, x):
        """
        Divides one dual number with another dual number or a real number.

        Parameters:
        x (Dual, int, float): The other dual number or a real number.

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
        x (int, float): The real number.

        Returns:
            Dual: A dual number of the division.
        """
        if self.real == 0:
            raise ZeroDivisionError("Denominator is zero")
        R_real = x/self.real
        R_dual = -x*self.dual / self.real**2
        return Dual(R_real, R_dual)

    def __floordiv__(self, x):
        """
        Divides one dual number with another dual or real number, returning the floor.

        Parameters:
        x (Dual, int, float): The other dual number or the real number.

        Returns:
            Dual: A dual number of the floor division.
        """
        if isinstance(x, Dual):
            if x.real == 0:
                raise ZeroDivisionError("Denominator is zero")
            R_real = self.real//x.real
            R_dual = (self.dual*x.real - self.real*x.dual)//(x.dual**2)
            return Dual(R_real, R_dual)
        else:
            if x == 0:
                raise ZeroDivisionError("Denominator is zero")
            return Dual(self.real//x, self.dual//x)

    def __rfloordiv__(self, x):
        """
        Reverse floor division: divides a real number with a dual number, returning the floor.

        Parameters:
        x (int, float): The real number.

        Returns:
            Dual: A dual number of the floor division.
        """
        if self.real == 0:
            raise ZeroDivisionError("Denominator is zero")
        R_real = x//self.real
        R_dual = -x*self.dual // self.real**2
        return Dual(R_real, R_dual)
    
    dfuncs = {
        'acos':'arccos',
        'asin':'arcsin',
        'atan':'arctan',
        'acosh':'arccosh',
        'asinh':'arcsinh',
        'atanh':'arctanh',
        'asech':'arcsech',
        'acsch':'arccsch',
    }
    
    def __array_ufunc__(self, ufunc, method, inputs, *args, **kwargs):

        if isinstance(self, Dual) and method == "call":
            ufunc_name = ufunc.__name__
            if hasattr(self, ufunc_name) or ufunc_name == self.dfuncs.get(ufunc_name):
                dfunc = getattr(self, ufunc_name)
                udfunc = np.frompyfunc(dfunc, len(inputs), 1)
                return udfunc()
            else:
                return NotImplemented


        else:
            return NotImplemented
    def sin(self):
        """
        Computes the sine of the dual number.

        Returns:
            Dual: A dual number of the sine.
        """
        return Dual(np.sin(self.real), self.dual*np.cos(self.real))
    
    def arcsin(self):
        """
        Computes the inverse sine of the dual number.

        Returns:
            Dual: A dual number of the inverse sine.
        """
        if self.real >= 1 or self.real <= -1:
            raise Exception("Inverse sine undefined for x not in (-1, 1).")
        return Dual(np.arcsin(self.real), self.dual/np.sqrt(1-self.real**2))
    
    def sinh(self):
        """
        Computes the hyperbolic sine of the dual number.

        Returns:
            Dual: A dual number of the hyperbolic sine.
        """
        return Dual(np.sinh(self.real), self.dual*np.cosh(self.real))
    
    def arcsinh(self):
        """
        Computes the inverse hyperbolic sine of the dual number.

        Returns:
            Dual: A dual number of the inverse hyperbolic sine.
        """
        return Dual(np.arcsinh(self.real), self.dual/np.sqrt(1+self.real**2))
    
    def csc(self):
        """
        Computes the cosecant of the dual number.

        Returns:
            Dual: A dual number of the cosecant.
        """
        return Dual(1/np.sin(self.real), -self.dual/(np.tan(self.real)*np.sin(self.real)))
    
    def arccsc(self):
        """
        Computes the inverse cosecant of the dual number.

        Returns:
            Dual: A dual number of the inverse cosecant.
        """
        if self.real > 1 or self.real < -1:
            return Dual(float(mp.acsc(self.real)), -self.dual/(np.abs(self.real)*np.sqrt(self.real**2 - 1)))
        else:
            raise Exception("Inverse cosecant derivative undefined when x is in range [-1, 1]")
    
    def csch(self):
        """
        Computes the hyperbolic cosecant of the dual number.

        Returns:
            Dual: A dual number of the hyperbolic cosecant.
        """
        return Dual(1/np.sinh(self.real), -self.dual/(np.tanh(self.real)*np.sinh(self.real)))
    
    def arccsch(self):
        """
        Computes the inverse hyperbolic cosecant of the dual number.

        Returns:
            Dual: A dual number of the inverse hyperbolic cosecant.
        """
        return Dual(np.log(1/self.real + np.sqrt(1 + 1/self.real**2)),-self.dual/(self.real**2 * np.sqrt(1 + 1/self.real**2)))
    
    def cos(self):
        """
        Computes the cosine of the dual number.

        Returns:
            Dual: A dual number of the cosine.
        """
        return Dual(np.cos(self.real), -self.dual*np.sin(self.real))
    
    def arccos(self):
        """
        Computes the inverse cosine of the dual number.

        Returns:
            Dual: A dual number of the inverse cosine.
        """
        if self.real >= 1 or self.real <= -1:
            raise Exception("Inverse cosine undefined for x not in (-1, 1).")
        else:
            return Dual(np.arccos(self.real), -self.dual/np.sqrt(1-self.real**2))
    
    def cosh(self):
        """
        Computes the hyperbolic cosine of the dual number.

        Returns:
            Dual: A dual number of the hyperbolic cosine.
        """
        return Dual(np.cosh(self.real), -self.dual*np.sinh(self.real))
    
    def arccosh(self):
        """
        Computes the inverse hyerbolic cosine of the dual number.

        Returns:
            Dual: A dual number of the inverse hyperbolic cosine.
        """
        if self.real > 1:
            return Dual(np.arccosh(self.real), self.dual/np.sqrt(self.real**2 - 1))
        else:
            raise Exception(f"Inverse hyperbolic cosine undefined for x not in (1,\u221E)")

    def sec(self):
        """
        Computes the secant of the dual number.

        Returns:
            Dual: A dual number of the secant.
        """
        return Dual(1/np.cos(self.real), -self.dual*np.tan(self.real)*(1/np.cos(self.real)))
    
    def arcsec(self):
        """
        Computes the inverse secant of the dual number.

        Returns:
            Dual: A dual number of the inverse secant.
        """
        if self.real > 1 or self.real < -1:
            return Dual(float(mp.asec(self.real)),self.dual/(np.abs(self.real) * np.sqrt(self.real**2 - 1))) 
        else:
            raise Exception("Inverse secant undefined in range [-1, 1]")
    
    def sech(self):
        """
        Computes the hyperbolic secant of the dual number.

        Returns:
            Dual: A dual numbre of the hyperbolic secant.
        """
        return Dual(1/np.cosh(self.real), -self.dual*np.tanh(self.real)/np.cosh(self.real))
    
    def arcsech(self):
        """
        Computes the inverse hyperbolic secant of the dual number.

        Returns:
            Dual: A dual number of the inverse hyperbolic secant.
        """
        if (self.real > 0) and (self.real <= 1):
            return Dual(np.log(1/self.real + np.sqrt(1/self.real**2 - 1)), -self.dual/(np.abs(self.real) * np.sqrt(1 - self.real**2)))
        else:
            raise Exception("Inverse hyperbolic secant undefined for x out of range (0, 1]")

    def tan(self):
        """
        Computes the tangent of the dual number.

        Returns:
            Dual: A dual number of the tangent.
        """
        return Dual(np.tan(self.real), self.dual*(1/np.cos(self.real))**2)

    def arctan(self):
        """
        Computes the inverse tangent of the dual number.

        Returns:
            Dual: A dual number of the inverse tangent.
        """
        return Dual(np.arctan(self.real), self.dual/(1 + self.real**2))
    
    def tanh(self):
        """
        Computes the hyperbolic tangent of the dual number.

        Returns:
            Dual: A dual number of the hyperbolic tangent.
        """
        return Dual(np.tanh(self.real), self.dual*(1/np.cosh(self.real))**2)
    
    def arctanh(self):
        """
        Computes the inverse hyperbolic tangent of the dual number.

        Returns:
            Dual: A dual number of the inverse hyperbolic tangent.
        """
        if np.abs(self.real) < 1:
            return Dual(0.5*(np.log(1 + self.real) - np.log(1 - self.real)), self.dual/(1 - self.real**2))
        else:
            raise Exception("Inverse hyperbolic tangent undefined outside of range (-1,1)")
    
    def cot(self):
        """
        Computes the cotangent of the dual number.

        Returns:
            Dual: A dual number of the cotangent.
        """
        return Dual(1/np.tan(self.real), -self.dual/np.sin(self.real)**2)

    def arccot(self):
        """
        Computes the inverse cotangent of the dual number.

        Returns:
            Dual: A dual number of the inverse cotangent.
        """
        return Dual(float(mp.acot(self.real)), -self.dual/(1+self.real**2))

    def coth(self):
        """
        Computes the hyperbolic cotangent of the dual number.

        Returns:
            Dual: A dual number of the hyperbolic cotangent.
        """
        return Dual(1/np.tanh(self.real), -self.dual/(np.sinh(self.real)**2))
    
    def log(self):
        """
        Computes the natural logarithm of the dual number.

        Returns:
            Dual: A dual number of the natural logarithm.
        """
        if self.real <=0:
            raise Exception("Logarithm is undefined for non-positive real numbers.")
        return Dual(np.log(self.real), self.dual/self.real)

    def exp(self):
        """
        Computes the exponential of the dual number.

        Returns:
            Dual: A dual number of the exponential.
        """
        return Dual(np.exp(self.real), self.dual*(np.exp(self.real)))

    def __pow__(self, x):
        """
        Raises a dual number to the power of another dual number or a real number.

        Parameters:
        x (Dual, int, float): The other dual number or a real number.

        Returns:
            Dual: A dual number of the power.
        """
        if isinstance(x, Dual):
            R_real = self.real**x.real
            R_dual = x.real*self.real**(x.real - 1) * x.dual + (self.real**x.real)*np.log(self.real)*x.dual
        else:
            R_real = self.real**x
            R_dual = x*self.real**(x - 1) * self.dual
        return Dual(R_real, R_dual)
    
    def __rpow__(self, x):
        """
        Raises a real number to the power of a dual number.

        Parameters:
        x (int, float): The real number.

        Returns:
            Dual: A dual number of the multiplication.
        """
        return Dual(x**self.real, x**self.real * self.dual * np.log(x))
    
    def __repr__(self):
        """
        String representation of dual number.

        Returns:
            string: The formatted string representation of dual number
        """
        return f"Dual(real={self.real}, dual={self.dual})"
    def partial(self, func, *args):
        """
        Calculates partial derivatives of function 'func' with respect to a dual number.

        The dual number has a real part equal to whatever value, and the dual part is set to one.
        All other variables are assumed to be dual numbers and have their dual parts set to zero.

        Parameters:
            func (function): Function to differentiate.
            *args (int, float): Dual numbers representing the variables in the order to be placed in the function.

        Returns:
            p_der (int, float): A real number representing the partial derivative.

        """
        vars = []
        for arg in args:
            if isinstance(arg, Dual):
                if self == arg:
                    vars.append(Dual(self.real, 1))
                else:
                    vars.append(Dual(arg.real, 0))
            else:
                raise Exception("This method is only defined for Dual class members.")

        p_der = func(*vars).dual

        return p_der
        

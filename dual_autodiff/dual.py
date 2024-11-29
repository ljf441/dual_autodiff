import numpy as np
import mpmath as mp

HANDLED_FUNCTIONS={}
class Dual:
    """
    A class to implement Dual numbers.

    Attributes:
        real (int, float): real part of Dual number.
        dual (int, float): dual part of Dual number.
    """

    def __init__(self, real, dual):
        """
        Initialises Dual with given parameters.

        Parameters:
            real (int, float): real part of Dual number.
            dual (int, float): dual part of Dual number.
        """
        self.real = real
        self.dual = dual

    def implement(function):
        """
        Register a function implementation for Dual objects.
        """
        def decorator(func):
            HANDLED_FUNCTIONS[function] = func
            return func
        return decorator

    HANDLED_NUMPY_FUNCTIONS = {
        """
        Maps numpy ufunc names to local function implementation names.
        """
        'acos':'arccos',
        'asin':'arcsin',
        'arctan':'arctan',
        'acosh':'arccosh',
        'asinh':'arcsinh',
        'atanh':'arctanh',
        'asech':'arcsech',
        'acsch':'arccsch',
    }
    
    def __array_ufunc__(self, ufunc, method, inputs, *args, **kwargs):
        """
        Overrides numpy ufuncs with local implementations instead when used on Dual numbers.
        """

        if isinstance(self, Dual) and method == "__call__":
            ufunc_name = ufunc.__name__
            if hasattr(self, ufunc_name):
                dfunc = getattr(self, ufunc_name)
            elif ufunc_name == self.HANDLED_NUMPY_FUNCTIONS.get(ufunc_name):
                dfunc = self.HANDLED_NUMPY_FUNCTIONS.get(ufunc_name)(self)
            else:
                return NotImplemented
            if dfunc: return dfunc()
        else:
            return NotImplemented
        
    def __array_function__(self, func, types, args, kwargs):
        """
        Indicates whether called function is handled by the Dual class or not. Also makes sure that all items in list are subclasses of Dual.
        """
        if func not in HANDLED_FUNCTIONS:
            return NotImplemented
        if not all(issubclass(t, self.__class__) for t in types):
            return NotImplemented
        return HANDLED_FUNCTIONS[func](*args, **kwargs)
    

    def __add__(self, x):
        """
        Adds two Dual numbers or a Dual number and a real number.

        Parameters:
        x (Dual, int, float): The other Dual number or a real number.

        Returns:
            Dual: A Dual number of the sum.
        """
        if isinstance(x, Dual):
            return Dual(self.real+x.real, self.dual+x.dual)
        elif isinstance(x, Collection):
            return Collection([self + t for t in x.elements])
        else:
            return Dual(self.real + x, self.dual)
        
    def __radd__(self, x):
        """
        Reverse additiion: adds a real number and a Dual number.

        Parameters:
        x (Dual, int, float): The real number.

        Returns:
            Dual: A Dual number of the sum.
        """
        return Dual(self.real+x, self.dual)
        
    def __sub__(self, x):
        """
        Subtracts a Dual number from another or subtracts a real number from a Dual number.
        
        Parameters:
        x (Dual, int, float): The other Dual number or a real number.

        Returns:
            Dual: A Dual number of the subtraction.
        """
        if isinstance(x, Dual):
            return Dual(self.real-x.real, self.dual-x.dual)
        elif isinstance(x, Collection):
            return Collection([self - t for t in x.elements])
        else:
            return Dual(self.real-x, self.dual)
        
    def __rsub__(self, x):
        """
        Reverse subtraction: subtracts a Dual number from a real number.

        Parameters:
        x (Dual, int, float): The real number.

        Returns:
            Dual: A Dual number of the subtraction.
        """
        return Dual(x - self.real, -self.dual)

    def __mul__(self, x):
        """
        Multiplies two Dual numbers or a Dual number and a real number.
        
        Parameters:
        x (Dual, int, float): The other Dual number or a real number.

        Returns:
            Dual: A Dual number of the multiplication.
        """
        if isinstance(x, Dual):
            R_real = self.real*x.real
            R_dual = self.real*x.dual + self.dual*x.real
            return Dual(R_real, R_dual)
        elif isinstance(x, Collection):
            return Collection([self*t for t in x.elements])
        else:
            return Dual(self.real*x, self.dual*x)
    
    def __rmul__(self, x):
        """
        Reverse multiplication: multiplies a real number and a Dual number.

        Parameters:
        x (Dual, int, float): The real number.

        Returns:
            Dual: A Dual number of the multiplication.
        """
        return Dual(self.real*x, self.dual*x)
    
    def __truediv__(self, x):
        """
        Divides one Dual number with another Dual number or a real number.

        Parameters:
        x (Dual, int, float): The other Dual number or a real number.

        Returns:
            Dual: A Dual number of the division.
        """
        if isinstance(x, Dual):
            if x.real == 0:
                raise ZeroDivisionError("Denominator is zero")
            R_real = self.real/x.real
            R_dual = (self.dual*x.real - self.real*x.dual)/(x.dual**2)
            return Dual(R_real, R_dual)
        elif isinstance(x, Collection):
            return Collection([self/t for t in x.elements])
        else:
            if x == 0:
                raise ZeroDivisionError("Denominator is zero")
            return Dual(self.real/x, self.dual/x)
        
    def __rtruediv__(self, x):
        """
        Reverse division: divides a real number with a Dual number.

        Parameters:
        x (int, float): The real number.

        Returns:
            Dual: A Dual number of the division.
        """
        if self.real == 0:
            raise ZeroDivisionError("Denominator is zero")
        R_real = x/self.real
        R_dual = -x*self.dual / self.real**2
        return Dual(R_real, R_dual)

    def __floordiv__(self, x):
        """
        Divides one Dual number with another Dual number or a real number, returning the floor.

        Parameters:
        x (Dual, int, float): The other Dual number or a real number.

        Returns:
            Dual: A Dual number of the floor division.
        """
        if isinstance(x, Dual):
            if x.real == 0:
                raise ZeroDivisionError("Denominator is zero")
            R_real = self.real//x.real
            R_dual = (self.dual*x.real - self.real*x.dual)//(x.dual**2)
            return Dual(R_real, R_dual)
        elif isinstance(x, Collection):
            return Collection([self//t for t in x.elements])
        else:
            if x == 0:
                raise ZeroDivisionError("Denominator is zero")
            return Dual(self.real//x, self.dual//x)

    def __rfloordiv__(self, x):
        """
        Reverse floor division: divides a real number with a Dual number, returning the floor.

        Parameters:
        x (int, float): The real number.

        Returns:
            Dual: A Dual number of the floor division.
        """
        if self.real == 0:
            raise ZeroDivisionError("Denominator is zero")
        R_real = x//self.real
        R_dual = -x*self.dual // self.real**2
        return Dual(R_real, R_dual)
    
    def __pow__(self, x):
        """
        Raises a Dual number to the power of another Dual number or a real number.

        Parameters:
        x (Dual, int, float): The other Dual number or a real number.

        Returns:
            Dual: A Dual number of the power.
        """
        if isinstance(x, Dual):
            R_real = self.real**x.real
            R_dual = x.real*self.real**(x.real - 1) * x.dual + (self.real**x.real)*np.log(self.real)*x.dual
        elif isinstance(x, Collection):
            return Collection([self ** t for t in x.elements])
        else:
            R_real = self.real**x
            R_dual = x*self.real**(x - 1) * self.dual
        return Dual(R_real, R_dual)
    
    def __rpow__(self, x):
        """
        Raises a real number to the power of a Dual number.

        Parameters:
        x (int, float): The real number.

        Returns:
            Dual: A Dual number of the multiplication.
        """
        return Dual(x**self.real, x**self.real * self.dual * np.log(x))
    
    def __repr__(self):
        """
        String representation of Dual number.

        Returns:
            string: The formatted string representation of Dual number
        """
        return f"Dual(real={self.real}, dual={self.dual})"
    
    def __eq__(self, x):
        """
        Checks equality of Dual numbers.

        Parameters:
            x (Dual): The other Dual number.
        """
        if isinstance(x, Dual):
            if self.real==x.real and self.dual==x.dual:
                return True
            else:
                return False
        else:
            return False
        
    def __ne__(self, x):
        """
        Checks inequality of Dual numbers.

        Parameters:
            x (Dual): The other Dual number.
        """
        if isinstance(x, Dual):
            if self.real != x.real or self.dual != x.dual:
                return True
            else:
                return False
        else:
            return False
    
    @implement(np.sin)
    def sin(self):
        """
        Computes the sine of the Dual number.

        Returns:
            Dual: A Dual number of the sine.
        """
        return Dual(np.sin(self.real), self.dual*np.cos(self.real))
    
    @implement(np.arcsin)
    def arcsin(self):
        """
        Computes the inverse sine of the Dual number.

        Returns:
            Dual: A Dual number of the inverse sine.
        """
        if self.real >= 1 or self.real <= -1:
            raise Exception("Inverse sine undefined for x not in (-1, 1).")
        return Dual(np.arcsin(self.real), self.dual/np.sqrt(1-self.real**2))
    
    @implement(np.sinh)
    def sinh(self):
        """
        Computes the hyperbolic sine of the Dual number.

        Returns:
            Dual: A Dual number of the hyperbolic sine.
        """
        return Dual(np.sinh(self.real), self.dual*np.cosh(self.real))
    
    @implement(np.arcsinh)
    def arcsinh(self):
        """
        Computes the inverse hyperbolic sine of the Dual number.

        Returns:
            Dual: A Dual number of the inverse hyperbolic sine.
        """
        return Dual(np.arcsinh(self.real), self.dual/np.sqrt(1+self.real**2))
    
    @implement(mp.csc)
    def csc(self):
        """
        Computes the cosecant of the Dual number.

        Returns:
            Dual: A Dual number of the cosecant.
        """
        return Dual(1/np.sin(self.real), -self.dual/(np.tan(self.real)*np.sin(self.real)))
    
    @implement(mp.acsc)
    def arccsc(self):
        """
        Computes the inverse cosecant of the Dual number.

        Returns:
            Dual: A Dual number of the inverse cosecant.
        """
        if self.real > 1 or self.real < -1:
            return Dual(float(mp.acsc(self.real)), -self.dual/(np.abs(self.real)*np.sqrt(self.real**2 - 1)))
        else:
            raise Exception("Inverse cosecant undefined in range (-1, 1)")
    
    @implement(mp.csch)
    def csch(self):
        """
        Computes the hyperbolic cosecant of the Dual number.

        Returns:
            Dual: A Dual number of the hyperbolic cosecant.
        """
        return Dual(1/np.sinh(self.real), -self.dual/(np.tanh(self.real)*np.sinh(self.real)))
    
    @implement(mp.acsch)
    def arccsch(self):
        """
        Computes the inverse hyperbolic cosecant of the Dual number.

        Returns:
            Dual: A Dual number of the inverse hyperbolic cosecant.
        """
        return Dual(np.log(1/self.real + np.sqrt(1 + 1/self.real**2)),-self.dual/(self.real**2 * np.sqrt(1 + 1/self.real**2)))
    
    @implement(np.cos)
    def cos(self):
        """
        Computes the cosine of the Dual number.

        Returns:
            Dual: A Dual number of the cosine.
        """
        return Dual(np.cos(self.real), -self.dual*np.sin(self.real))
    
    @implement(np.arccos)
    def arccos(self):
        """
        Computes the inverse cosine of the Dual number.

        Returns:
            Dual: A Dual number of the inverse cosine.
        """
        if self.real >= 1 or self.real <= -1:
            raise Exception("Inverse cosine undefined for x not in (-1, 1).")
        else:
            return Dual(np.arccos(self.real), -self.dual/np.sqrt(1-self.real**2))
    
    @implement(np.cosh)
    def cosh(self):
        """
        Computes the hyperbolic cosine of the Dual number.

        Returns:
            Dual: A Dual number of the hyperbolic cosine.
        """
        return Dual(np.cosh(self.real), -self.dual*np.sinh(self.real))
    
    @implement(np.arccosh)
    def arccosh(self):
        """
        Computes the inverse hyerbolic cosine of the Dual number.

        Returns:
            Dual: A Dual number of the inverse hyperbolic cosine.
        """
        if self.real > 1:
            return Dual(np.arccosh(self.real), self.dual/np.sqrt(self.real**2 - 1))
        else:
            raise Exception(f"Inverse hyperbolic cosine undefined for x not in (1,\u221E).")

    @implement(mp.sec)
    def sec(self):
        """
        Computes the secant of the Dual number.

        Returns:
            Dual: A Dual number of the secant.
        """
        return Dual(1/np.cos(self.real), -self.dual*np.tan(self.real)*(1/np.cos(self.real)))
    
    @implement(mp.asec)
    def arcsec(self):
        """
        Computes the inverse secant of the Dual number.

        Returns:
            Dual: A Dual number of the inverse secant.
        """
        if self.real > 1 or self.real < -1:
            return Dual(float(mp.asec(self.real)),self.dual/(np.abs(self.real) * np.sqrt(self.real**2 - 1))) 
        else:
            raise Exception("Inverse secant undefined in range (-1, 1).")
    
    @implement(mp.sech)
    def sech(self):
        """
        Computes the hyperbolic secant of the Dual number.

        Returns:
            Dual: A dual numbre of the hyperbolic secant.
        """
        return Dual(1/np.cosh(self.real), -self.dual*np.tanh(self.real)/np.cosh(self.real))
    
    @implement(mp.asech)
    def arcsech(self):
        """
        Computes the inverse hyperbolic secant of the Dual number.

        Returns:
            Dual: A Dual number of the inverse hyperbolic secant.
        """
        if (self.real > 0) and (self.real <= 1):
            return Dual(np.log(1/self.real + np.sqrt(1/self.real**2 - 1)), -self.dual/(np.abs(self.real) * np.sqrt(1 - self.real**2)))
        else:
            raise Exception("Inverse hyperbolic secant undefined outside of range (0, 1].")

    @implement(np.tan)
    def tan(self):
        """
        Computes the tangent of the Dual number.

        Returns:
            Dual: A Dual number of the tangent.
        """
        return Dual(np.tan(self.real), self.dual*(1/np.cos(self.real))**2)

    @implement(np.arctan)
    def arctan(self):
        """
        Computes the inverse tangent of the Dual number.

        Returns:
            Dual: A Dual number of the inverse tangent.
        """
        if np.abs(self.real) < np.pi/2:
            return Dual(np.arctan(self.real), self.dual/(1 + self.real**2))
        else:
            raise Exception(f"Inverse tangent undefined outside of range (-\u03C0/2, \u03C0/2)")
    
    @implement(np.tanh)
    def tanh(self):
        """
        Computes the hyperbolic tangent of the Dual number.

        Returns:
            Dual: A Dual number of the hyperbolic tangent.
        """
        return Dual(np.tanh(self.real), self.dual*(1/np.cosh(self.real))**2)
    
    @implement(np.arctanh)
    def arctanh(self):
        """
        Computes the inverse hyperbolic tangent of the Dual number. Requires real-valued input.

        Returns:
            Dual: A Dual number of the inverse hyperbolic tangent.
        """
        if np.abs(self.real) < 1:
            return Dual(np.arctanh(self.real), self.dual/(1 - self.real**2))
        else:
            raise Exception("Inverse hyperbolic tangent undefined outside of range (-1,1).")
    
    @implement(mp.cot)
    def cot(self):
        """
        Computes the cotangent of the Dual number.

        Returns:
            Dual: A Dual number of the cotangent.
        """
        return Dual(1/np.tan(self.real), -self.dual/np.sin(self.real)**2)

    @implement(mp.acot)
    def arccot(self):
        """
        Computes the inverse cotangent of the Dual number.

        Returns:
            Dual: A Dual number of the inverse cotangent.
        """
        return Dual(float(mp.acot(self.real)), -self.dual/(1+self.real**2))

    @implement(mp.coth)
    def coth(self):
        """
        Computes the hyperbolic cotangent of the Dual number.

        Returns:
            Dual: A Dual number of the hyperbolic cotangent.
        """
        return Dual(1/np.tanh(self.real), -self.dual/(np.sinh(self.real)**2))
    
    def log(self):
        """
        Computes the natural logarithm of the Dual number.

        Returns:
            Dual: A Dual number of the natural logarithm.
        """
        if self.real <=0:
            raise Exception("Logarithm is undefined for non-positive real numbers.")
        return Dual(np.log(self.real), self.dual/self.real)

    def exp(self):
        """
        Computes the exponential of the Dual number.

        Returns:
            Dual: A Dual number of the exponential.
        """
        return Dual(np.exp(self.real), self.dual*(np.exp(self.real)))
        
    def partial(self, func, *args):
        """
        Calculates partial derivatives of function 'func' with respect to a Dual number.

        The Dual number has a real part equal to whatever value, and the dual part is set to one.
        All other variables are assumed to be Dual numbers and have their dual parts set to zero.

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
        
class Collection():
    """
    A class to implement collections of Dual numbers.

    Attributes:
        elements: A collection of Dual numbers
    """
    def __init__(self, elements):
        """
        Initialises Collection with a list of Dual numbers.

        Parameters:
            elements: A collection of Dual numbers
        """
        self.elements = list(elements)

    def __getattr__(self, attr):
        """
        Allows Collection to use methods from Dual class to implement mathematical operations defined therein on each element in the collection.

        Parameters:
            attr (str): The name of the method being called. 
        
        Returns:
            method (function): A function that applies the method to each element in the collection and returns a new Collection that has been operated on.
        """
        def method(*args, **kwargs):
            return Collection([getattr(element, attr)(*args, **kwargs) for element in self.elements])
        return method
    
    def __array_ufunc__(self, ufunc, method, inputs, *args, **kwargs):
        """
        Allows NumPy universal functions (ufuncs) to operate over the Collection.

        Parameters:
            ufunc (universal function): The universal function being called.
            method (str): The method of the ufunc. Currently, only "__call__" is implemented.
            inputs (tuple): What is passed to the ufunc.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Collection: A Collection of the results of the applied ufunc.
        """
        if method == "__call__":
            return Collection([ufunc(element) for element in self.elements])
        raise NotImplementedError(f"Handling for ufunc method {method} is not implemented.")
        
    def __repr__(self):
        """
        String representation of the Collection.

        Returns:
            string: The formatted string representation of the Collection.
        """
        return f"Collection({self.elements})"
    
    def __len__(self):
        """
        Returns length of Collection.
        """
        return len(self.elements)
    
    def __eq__(self, x):
        """
        Checks equality of Collections.

        Parameters:
            x (Collection): The other Collection.
        """
        if isinstance(x, Collection):
            if len(self.elements) != len(x.elements):
                return False
            else:
                b = all(s == t for s, t in zip(self.elements, x.elements))
                return b
        else:
            return False
    
    def __ne__(self, x):
        """
        Checks inequality of Collections.

        Parameters:
            x (Collection): The other collection.
        """
        if isinstance(x, Collection):
            if len(self.elements) != len(x.elements):
                return True
            else:
                b = all(s != t for s, t in zip(self.elements, x.elements))
                return b
        else:
            return True

    def __getitem__(self, idx):
        """
        Returns Dual number within Collection at given index.

        Parameters:
            idx (int): The index of the element.
        
        Returns:
            element (Dual): The Dual number at the given index.
        """
        element = self.elements[idx]
        return element
    
    def __setitem__(self, idx, element):
        """
        Modifies Dual number within Collection at given index to a given element.

        Parameters:
            idx (int): The index of the element to be modified.
            value (Dual): The new Dual value of the element.
        """
        if isinstance(element, Dual):
            self.elements[idx] = element
        else:
            raise Exception("A Collection is meant to only hold Dual numbers.")
        
    def append(self, element):
        """
        Appends a Dual number element to a Collection.

        Parameters:
            element (Dual): The Dual number to be appended.
        """
        if isinstance(element, Dual):
            self.elements.append(element)
        else:
            raise Exception("A Collection is meant to only hold Dual numbers.")
    
    def __add__(self, x):
        """
        Adds two Collections, a Collection and a Dual, or a Collection and a real number.

        Parameters:
            x (Collection, Dual, int, float): The other Collection, a Dual number, or a real number.

        Returns:
            Collection: A Collection of the sum.
        """
        if isinstance(x, Collection):
            return Collection([s + t for s, t in zip(self.elements, x.elements)])
        else:
            return Collection([s + x for s in self.elements])
        
    def __radd__(self, x):
        """
        Reverse additiion: adds a Dual number or a real number to a Collection.

        Parameters:
        x (Dual, int, float): The Dual or real number.

        Returns:
            Collection: A Collection of the sum.
        """
        return Collection([s + x for s in self.elements])
    
    def __sub__(self, x):
        """
        Subtracts a Collection, a Dual number, or a real number from a Collection.
        
        Parameters:
        x (Collection, Dual, int, float): The other Collection, a Dual number,or a real number.

        Returns:
            Collection: A Collection of the subtraction.
        """
        if isinstance(x, Collection):
            return Collection([s - t for s, t in zip(self.elements, x.elements)])
        else:
            return Collection([s - x for s in self.elements])
        
    def __rsub__(self, x):
        """
        Reverse subtraction: subtracts a Collection from a Dual number or a real number.

        Parameters:
        x (Dual, int, float): The Dual number or the real number.

        Returns:
            Collection: A Collection of the subtraction.
        """
        return Collection([x - s for s in self.elements])
    
    def __mul__(self, x):
        """
        Multiplies two Collections, a Dual number and a Collection, or a real number and a Collection.
        
        Parameters:
        x (Collection, Dual, int, float): The other Collection, a Dual number. or a real number.

        Returns:
            Collection: A Collection of the multiplication.
        """
        if isinstance(x, Collection):
            return Collection([s * t for s, t in zip(self.elements, x.elements)])
        else:
            return Collection([s * x for s in self.elements])
        
    def __rmul__(self, x):
        """
        Reverse multiplication: multiplies a Dual number or a real number with a Collection.

        Parameters:
        x (Dual, int, float): The Dual number or the real number.

        Returns:
            Dual: A Collection of the multiplication.
        """
        return Collection([s * x for s in self.elements])
    
    def __truediv__(self, x):
        """
        Divides a Collection with another Collection, a Dual number, or a real number.

        Parameters:
        x (Collection, Dual, int, float): The other Collection, a Dual number, or a real number.

        Returns:
            Collection: A Collection of the division.
        """
        if isinstance(x, Collection):
            if any(t.real == 0 for t in x.elements):
                raise ZeroDivisionError("A denominator is zero.")
            return Collection([s / t for s, t in zip(self.elements, x.elements)])
        elif isinstance(x, Dual):
            if x.real == 0:
                raise ZeroDivisionError("Denominator is zero")
            return Collection([s / x for s in self.elements])
        else:
            return Collection([s / x for s in self.elements])
    
    def __rtruediv__(self, x):
        """
        Reverse division: divides a Dual number or a real number with a Collection.

        Parameters:
        x (Dual, int, float): The Dual number or the real number.

        Returns:
            Collection: A Collection of the division.
        """
        if any(t.real == 0 for t in self.elements):
            raise ZeroDivisionError("A denominator is zero.")
        return Collection([x/s for s in self.elements])
    
    def __floordiv__(self, x):
        """
        Divides a Collection with another Collection, a Dual number, or a real number, returning the floor.

        Parameters:
        x (Collection, Dual, int, float): The other Collection, a Dual number, or a real number.

        Returns:
            Collection: A Collection of the floor division.
        """
        if isinstance(x, Collection):
            if any(t.real == 0 for t in x.elements):
                raise ZeroDivisionError("A denominator is zero.")
            return Collection([s // t for s, t in zip(self.elements, x.elements)])
        elif isinstance(x, Dual):
            if x.real == 0:
                raise ZeroDivisionError("Denominator is zero")
            return Collection([s // x for s in self.elements])
        else:
            if x == 0:
                raise ZeroDivisionError("Denominator is zero")
            return Collection([s // x for s in self.elements])
    
    def __rfloordiv__(self, x):
        """
        Reverse floor division: divides a Dual number or a real number with a Collection, returning the floor.

        Parameters:
        x (Dual, int, float): The Dual number or the real number.

        Returns:
            Collection: A Collection of the floor division.
        """
        if any(t.real == 0 for t in self.elements):
            raise ZeroDivisionError("A denominator is zero.")
        return Collection([x // s for s in self.elements])
    
    def __pow__(self, x):
        """
        Allows for element-wise raising a Dual number to the power of another Dual number or a real number.

        Parameters:
            x (Collection, Dual, int, float): The other Collection, a Dual number, or a real number.
        
        Returns:
            Collection: A Collection of the power.
        """
        if isinstance(x, Collection):
            return Collection([s**t for s, t in zip(self.elements, x.elements)])
        else:
            return Collection([s**x for s in self.elements])
        
    def __rpow__(self, x):
        """
        Reverse power: allows for element-wise raising a Dual number or a real number to a Collection of Dual numbers.

        Parameters:
            x (Dual, int, float): The Dual number or the real number.
        """
        return Collection([x**s for s in self.elements])

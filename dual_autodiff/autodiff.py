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



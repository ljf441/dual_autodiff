.. dual_autodiff documentation master file, created by
   sphinx-quickstart on Wed Nov 13 23:36:28 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

dual_autodiff documentation
===========================

This package implements dual numbers, which are numbers of the form a + b \epsilon where 'a' is a real number and 'b' is the dual part with the property that '\epsilon^2 = 0'.
Dual numbers are useful for automatic differentiation and numerical analysis.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   dual_autodiff.ipynb

Dual Class
==========

.. autoclass:: dual_autodiff.Dual
   :members:
   :undoc-members:
   :show-inheritance:

Instance Methods
================

.. automethod:: dual_autodiff.Dual.__add__
.. automethod:: dual_autodiff.Dual.__sub__
.. automethod:: dual_autodiff.Dual.__mul__
.. automethod:: dual_autodiff.Dual.__truediv__
.. automethod:: dual_autodiff.Dual.__pow__
.. automethod:: dual_autodiff.Dual.__repr__

Installation
================

Ensure you have Python 3.10 or higher. Install the package and its dependencies with:

.. code-block:: bash

    pip install -e .


Usage
================

Here's a quick example of how to use the package:

.. code-block:: python

    # import the package
    import dual_autodiff as df

    # create dual numbers
    x = df.Dual(2, 1)
    y = df.Dual(3, 2)

    # perform arithmetic and trigonometric operations
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    e = x**y
    f = x.sin()
    g = x.cos()
    h = x.tan()
    i = x.log()
    j = x.exp()
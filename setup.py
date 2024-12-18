from setuptools import setup, find_packages

setup(
    name='dual_autodiff',
    version='0.0.1',
    packages=find_packages(include=["dual_autodiff", "dual_autodiff.*"]),
    exclude_package_data={"": ["__pycache__"]},
    package_data={"dual_autodiff": ["*.py"]},
)

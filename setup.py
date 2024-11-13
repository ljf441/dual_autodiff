from setuptools import setup, find_packages

setup(
    name='dual_autodiff',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'jupyter',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'dual_autodiff=dual_autodiff.cli:main',
        ]
    },
)

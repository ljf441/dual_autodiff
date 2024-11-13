from setuptools import setup, find_packages

setup(
    name='autodiff',
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
            'autodiff=autodiff.cli:main',
        ]
    },
)

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../dual_autodiff'))


project = 'dual_autodiff'
copyright = '2024, Laura Just Fung'
author = 'Laura Just Fung'
release = 'beta'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary', 'sphinx.ext.napoleon', 'sphinx_autodoc_typehints', 'sphinx.ext.viewcode', "myst_nb"]

templates_path = ['_templates']
exclude_patterns = []
master_doc = 'index'

autodoc_default_flags = ['members', 'undoc-members', 'show-inheritance']

nbsphinx_execute = 'always'
nbsphinx_allow_errors = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

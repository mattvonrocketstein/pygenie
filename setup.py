#!/usr/bin/env python
""" setup.py for pygenie
"""
from distutils.core import setup

setup(
    name         ='pygenie',
    version      = '.1',
    description  = 'pygenie: a tool for analyzing cyclomatic complexity',
    author       = 'davin stanek',
    url          = 'http://svn.traceback.org/python/cyclic_complexity/',
    py_modules   = ['pygenie'],
    entry_points = {},
)

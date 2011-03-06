#!/usr/bin/env python
""" setup.py for pygenie
"""

import os
from setuptools import setup, find_packages

try:
    from setuptools import setup, find_packages
    have_setuptools = True
except ImportError:
    from distutils.core import setup
    def find_packages():
        return [
            'pygenie',
        ]
    have_setuptools = False
try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

if have_setuptools:
    add_keywords = dict( entry_points = \
                         { 'console_scripts': \
                           ['pygenie = pygenie:main', \
                            ]
                           }, )
else:
    add_keywords = dict( scripts = ['pygenie'], )

setup(
    name         ='pygenie',
    version      = '.1',
    description  = 'pygenie: a tool for analyzing cyclomatic complexity',
    author       = 'davin stanek',
    url          = 'http://svn.traceback.org/python/cyclic_complexity/',
    package_dir = {'': 'lib'},
    packages     = find_packages('lib'),
    py_modules   = ['pygenie'],
    cmdclass = {'build_py': build_py},
    **add_keywords
)

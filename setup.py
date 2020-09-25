#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:41:00 2020

@author: isapoetzsch
"""

from setuptools import setup, find_packages
 
setup(name='excel2sbol',
      version='0.1.0-alpha',
      url='https://github.com/SynBioDex/Excel-to-SBOL/tree/master/excel2sbol',
      license='BSD 3-clause',
      author='',
      author_email='',
      description='convert excel templates into sbol',
      packages=find_packages(),
      long_description=open('README.md').read(),
      zip_safe=False)
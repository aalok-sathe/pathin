#!/usr/bin/env python3

from distutils.core import setup
from setuptools import setup as setup_

setup_(name='pathin', install_requires=['click>=7.1.1'])

setup(name='pathin',
      version='0.1',
      description='Utility to conveniently add to PATH',
      author='Aalok Sathe',
      author_email='aalok-sathe@acm.org',
      url='https://github.com/aalok-sathe/pathin.git',
      scripts=['pathin'])

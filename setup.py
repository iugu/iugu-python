# -*- coding: utf-8 -*-

try:
    from distutils.core import setup
except ImportError:
    from setuptools import setup

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'iugu'))
from version import __version__

setup(
  name='iugu',
  version= __version__,
  author='Felipe Tomaz, Arthur Furlan',
  author_email='gmail@felipetomaz.com, afurlan@afurlan.org',
  packages=['iugu'],
  scripts=[],
  url='https://github.com/iugu/iugu-python',
  license='MIT',
  description='The Iugu provides a Python REST APIs to create, process and manage payments.',
  long_description="""
    The Iugu provides a Python REST APIs to create, process and manage payments.

    http://iugu.com/referencias/api - API Reference
  """,
  install_requires=['requests'],
  classifiers=[
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ],
  keywords=['iugu', 'rest', 'payment']
)
#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='sidik',
      version='0.1',
      packages=find_packages(),
      package_data={'sidik': ['bin/*.*', 'static/*.*', 'templates/*.*']},
      exclude_package_data={'sidik': ['bin/*.pyc']},
      scripts=['sidik/bin/manage.py'])

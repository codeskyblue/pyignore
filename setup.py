from __future__ import print_function

import pyignore

try: from distutils.core import setup
except ImportError: from setuptools import setup

setup(
      name='pyignore',
      version=pyignore.__version__,
      license="MIT",
      description='parse .gitignore file',

      author='codeskyblue',
      author_email='codeskyblue@gmail.com',
      url='http://github.com/codeskyblue/pyignore',

      py_modules=['pyignore'],
      install_requires=[],
      )

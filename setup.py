import os
import sys
import setuptools

import jsonpare

_DESCRIPTION = \
      """\
A very simple utility to decode/unwind JSON to JSON (or STDOUT) from the command-line.
"""

_APP_PATH = os.path.dirname(jsonpare.__file__)

with open(os.path.join(_APP_PATH, 'resources', 'README.rst')) as f:
      long_description = f.read()

with open(os.path.join(_APP_PATH, 'resources', 'requirements.txt')) as f:
      install_requires = [s.strip() for s in f.readlines()]

setuptools.setup(name='jsonpare',
      version=jsonpare.__version__,
      description=_DESCRIPTION,
      long_description=long_description,
      classifiers=[],
      keywords='json commandline command-line',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='https://github.com/dsoprea/JsonPare',
      license='GPL 2',
      packages=setuptools.find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      scripts=[
            'jsonpare/resources/scripts/jp',
      ],
      install_requires=install_requires,
      entry_points="",
)

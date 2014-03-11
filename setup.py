from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='jsonpare',
      version=version,
      description="A very simple utility to decode and unwrap a JSON string from the command-line.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='json commandline command-line',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='',
      license='GPL 2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      scripts=['scripts']
      install_requires=[

      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

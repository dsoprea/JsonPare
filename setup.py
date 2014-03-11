from setuptools import setup, find_packages
import sys, os

setup(name='jsonpare',
      version='0.1.0',
      description="A very simple utility to decode and unwind JSON into JSON from the command-line.",
      long_description="",
      classifiers=[],
      keywords='json commandline command-line',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='',
      license='GPL 2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      scripts=['scripts/js']
      install_requires=[],
      entry_points="",
      )

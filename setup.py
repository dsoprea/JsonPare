from setuptools import setup, find_packages
import sys, os

setup(name='jsonpare',
      version='0.2.8',
      description="A very simple utility to decode and unwind JSON into JSON from the command-line.",
      long_description="A very simple utility to decode and unwind JSON into JSON from the command-line.",
      classifiers=[],
      keywords='json commandline command-line',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='https://github.com/dsoprea/JsonPare',
      license='GPL 2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      scripts=['scripts/jp'],
      install_requires=[],
      entry_points="",
)

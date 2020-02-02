from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='pySearchErr',
      version='0.1.3',
      description='Detects Python3 exception and searches for the error on Google automatically',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/JING1201/SwampHacks2020',
      author='jlionwg',
      license='MIT',
      packages=['pySearchErr'],
      scripts=['bin/pySearchErr'],
      zip_safe=False)
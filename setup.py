from setuptools import setup, find_packages
from codecs import open
from os import path
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name='pyzure-documentdb',
	version='0.1.0.dev3',
	author='Don Kim',
	author_email='dgkim5360@gmail.com',
	packages=['pyzure_docdb'],
	description='a python wrapper for the python client of Azure DocumentDB',
	long_description=long_description,
	url='https://github.com/dgkim5360/pyzure-documentdb',
	keywords='azure documentdb',
	license='MIT',
	install_requires=[
		'pydocumentdb',
	]
)

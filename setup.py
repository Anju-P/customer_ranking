# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in customer_ranking/__init__.py
from customer_ranking import __version__ as version

setup(
	name='customer_ranking',
	version=version,
	description='Customer Ranking by Sales_Collection',
	author='Anju Prasannan',
	author_email='anjuprasannan321@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

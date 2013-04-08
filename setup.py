# -*- coding: utf-8 -*-
import os

from setuptools import setup


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='dj-mongo-database-url',
	version='0.1',
	url='https://github.com/RyanBalfanz/django-mongo-database-url',
	# license='BSD',
	author='Ryan Balfanz',
	author_email='ryan@ryanbalfanz.net',
	description='Use MongoDB Database URLs in your Django Application.',
	long_description=README,
	py_modules=['dj_mongo_database_url'],
	zip_safe=False,
	include_package_data=True,
	platforms='any',
	classifiers=[
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		# 'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
		'Topic :: Software Development :: Libraries :: Python Modules'
	]
)

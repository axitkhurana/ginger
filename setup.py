#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='ginger',
    version='1.0',
    description="",
    author="Akshit Khurana",
    author_email='axitkhurana@gmail.com',
    url='',
    packages=find_packages(),
    package_data={'ginger': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# wight load testing
# https://github.com/heynemann/wight

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Bernardo Heynemann heynemann@gmail.com

from setuptools import setup, find_packages
from wight import __version__

tests_require = [
    'nose',
    'coverage',
    'yanc',
    'preggy==0.5.11',
    'mock',
    'tox',
    'ipdb',
    'sh',
    'factory_boy',
    'coveralls',
    'pexpect-u',
    'turq'
]

setup(
    name='wight-cli',
    version=__version__,
    description='wight is a load testing scheduling and tracking tool.',
    long_description='''
wight is a load testing scheduling and tracking tool.

This package contains the client part of wight. If your are looking for the whole package, please se at https://pypi.python.org/pypi/wight/
''',
    keywords='test testing load performance profile profiling',
    author='Márcio Duarte',
    author_email='maethorin@gmail.com',
    url='http://github.com/maethorin/wight-cli/',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing'
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'argparse',
        'cement',
        'derpconf==0.4.7',
        'requests',
        'prettytable',
        'colorama',
        'python-dateutil',
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            'wight=wight.cli:main',
        ],
    },
)

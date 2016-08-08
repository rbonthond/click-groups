#!/usr/bin/env python

from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='click-aliases',
    version='0.1',
    description='Enable command groups for Click',
    long_description=readme,
    author='Robbin Bonthond',
    author_email='robbin@bonthond.com',
    url='https://github.com/rbonthond/click-groups',
    license='MIT',
    packages=['click_groups'],
    install_requires=[
        'click',
    ],
    extras_require={
        'dev': [
            'flake8',
            'flake8-import-order',
            'tox-travis',
            'pytest',
            'pytest-cov',
            'coveralls',
            'wheel',
        ]
    }
)

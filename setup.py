#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


from gsclient.main import version


setup(
    name='gsclient',
    version=version,
    description='GrooveShark audio streaming client',
    long_description=open('README').read(),
    author='Andrew Drake',
    author_email='',
    url='https://github.com/drakedevel/gsclient',
    data_files=[
        'README',
        'LICENSE',
    ],
    packages=[
        'gsclient'
    ],
    entry_points={
        'console_scripts': [
            'gsclient = gsclient.main:main'
        ]
    },
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ),
)

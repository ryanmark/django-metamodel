#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="django-meta",
    version="1.1.0",

    packages=find_packages(),
    install_requires=[
        "django>=1.4"
    ],

    author="Ryan Mark",
    author_email="ryan@mrk.cc",
    description="Add arbitrary data to your django users. This app adds `user.meta` which acts like a dictionary and stores whatever the hell you want. And you can add `.meta` to any of your models.",
    url="http://github.com/ryanmark/django-meta/",
    license="MIT",
    keywords=['Development Status :: 4 - Beta',
              'License :: OSI Approved :: MIT License',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Topic :: Internet',
              ],
)

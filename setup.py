from setuptools import setup, find_packages


setup(
    name="meta",
    version="1.0.1",

    packages=find_packages(),
    author="Ryan Mark",
    author_email="ryan@mrk.cc",
    description="Add arbitrary data to your django users. This app adds `user.meta` which acts like a dictionary and stores whatever the hell you want. But you could add `.meta` to any of your models.",
    url="http://github.com/ryanmark/django-meta/",
    license="MIT",
    install_requires=["django>=1.4", ],
)

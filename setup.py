from setuptools import setup, find_packages

setup(
    name="django-metamodel",
    packages=find_packages(),
    version="1.1.0",
    author="Ryan Mark",
    author_email="ryan@mrk.cc",
    description="Add arbitrary data to your django users. This app adds `user.meta` which acts like a dictionary and stores whatever the hell you want. But you could add `.meta` to any of your models.",
    url="http://github.com/ryanmark/django-metamodel/",
    license="MIT",
    install_requires=["django>=1.4", ],
)

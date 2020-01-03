#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re
import pathlib

from setuptools import setup

_parent = pathlib.Path(__file__).parent
_readme = (_parent / "README.rst").read_text().strip()
_readme = re.sub("^.. start-badges.*^.. end-badges", "", _readme, re.M | re.S)
_changes = (_parent / "CHANGELOG.rst").read_text().strip()
_changes = re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", _changes)

setup(
    name="marshmallow-union",
    version="0.1.13",
    description="Union fields for marshmallow.",
    license="MIT",
    long_description=_readme + "\n" + _changes,
    long_description_content_type="text/rst",
    author="Adam Boche",
    author_email="adamboche@users.noreply.github.com",
    url="https://github.com/adamboche/python-marshmallow-union",
    package_dir={"": "src"},
    py_modules=["marshmallow_union"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Utilities",
    ],
    install_requires=[
        "marshmallow~=3.0",
    ],
)

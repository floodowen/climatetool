#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# build command
setup(
    name="climate",
    version="0.0.1",
    author="Owen Flood",
    author_email="owen.flood@columbia.edu",
    license="GPLv3",
    description="A package for comparing climate trends",
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
        "console_scripts": ["climatetool = climatetool.__main__:main"]
    },
)

'''
Descripttion: 
version: 
Author: p.p.
Date: 2022-01-08 20:49:51
LastEditors: p.p.
LastEditTime: 2022-01-08 21:11:09
'''
"""Setup file for dictobject"""

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pydictobject',
    version='v1.05.1',
    description='pydictobject - a dictionary that is accessible like an object',
    packages=['pydictobject'],
    author='Peter Harris',
    author_email='pdrharris@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/pdrharris/pydictobject',
    download_url='https://github.com/pdrharris/pydictobject/archive/1.05.tar.gz',
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

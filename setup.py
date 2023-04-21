from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'outlier detection'
LONG_DESCRIPTION = 'A python package to detect outliers in a dataset'


# Setting up
setup(
    name="Outlyzer",
    version=VERSION,
    author="Devendra Parihar",
    author_email="devendraparihar340@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'love', 'match', 'percentage', 'calculator', 'lovematch'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
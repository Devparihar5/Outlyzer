from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Outlier detection'
with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

# Setting up
setup(
    name="Outlyzer",
    version=VERSION,
    author="Devendra Parihar",
    author_email="devendraparihar340@gmail.com",
    url='https://github.com/Devparihar5/Outlyzer',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['numpy', 'scipy', 'pandas', 'matplotlib'],
    keywords=['outliers', 'outlier-detection', 'data-science', 'machine-learning', 'statistics', 'zscore', 'iqr', 'visualization'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Outlier detection'
LONG_DESCRIPTION = '''

A Python package to detect outliers in a dataset

Outlyzer: A Python library for outlier detection

Outlyzer is a Python library that provides various methods for detecting outliers in a dataset. It includes implementation of Z-score, IQR, and Mahalanobis distance methods for identifying outliers, as well as visualization-based methods using scatter plots, box plots, and other types of visualizations.

Usage:
    - Import the desired method from the library, e.g.:
        from Outlyzer.zscore import detect_outliers_zscore
        from Outlyzer.iqr import detect_outliers_iqr

    - Pass your dataset or data series to the respective function, e.g.:
        outliers_zscore = detect_outliers_zscore(data)
        outliers_iqr = detect_outliers_iqr(data)

    - The functions will return a boolean array indicating whether each data point is an outlier (True) or not (False).

'''

# Setting up
setup(
    name="Outlyzer",
    version=VERSION,
    author="Devendra Parihar",
    author_email="devendraparihar340@gmail.com",
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

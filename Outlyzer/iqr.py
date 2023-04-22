# iqr.py

import numpy as np

def detect_outliers_iqr(data, multiplier=1.5):
    """
    Detects outliers in data using the Interquartile Range (IQR) method.
    
    Args:
        data (numpy.ndarray): Input data as a NumPy array.
        multiplier (float): Multiplier for IQR. Data points below Q1 - multiplier * IQR
                           and above Q3 + multiplier * IQR are considered as outliers.
                           Default is 1.5.
    
    Returns:
        numpy.ndarray: Boolean array with True for outlier data points and False otherwise.
    """
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - multiplier * iqr
    upper_bound = q3 + multiplier * iqr
    outliers = (data < lower_bound) | (data > upper_bound)
    return outliers

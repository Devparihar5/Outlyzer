# zscore.py

import numpy as np

def detect_outliers_zscore(data, threshold=3):
    """
    Detects outliers in data using the Z-score method.
    
    Args:
        data (numpy.ndarray): Input data as a NumPy array.
        threshold (float): Threshold value for Z-score. Data points with Z-scores above
                          this threshold are considered as outliers. Default is 3.
    
    Returns:
        numpy.ndarray: Boolean array with True for outlier data points and False otherwise.
    """
    z_scores = (data - np.mean(data)) / np.std(data)
    outliers = np.abs(z_scores) > threshold
    return outliers


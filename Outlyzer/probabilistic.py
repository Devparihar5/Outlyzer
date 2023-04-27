<<<<<<< HEAD
from scipy.stats import norm
import numpy as np

def detect_outliers_probabilistic(data, alpha=0.05):
    """
    Detect outliers using probabilistic and statistical modeling method.
    
    Parameters:
        - data (numpy array or pandas Series): Input data
        - alpha (float, optional): Significance level for statistical tests (default=0.05)
        
    Returns:
        - outliers (list): List of outlier indices
    """
    mu, std = norm.fit(data)
    z_scores = (data - mu) / std
    p_values = 2 * (1 - norm.cdf(np.abs(z_scores)))
    outliers = np.where(p_values < alpha)[0]
    return outliers.tolist()
=======
from scipy.stats import norm
import numpy as np

def detect_outliers_probabilistic(data, alpha=0.05):
    """
    Detect outliers using probabilistic and statistical modeling method.
    
    Parameters:
        - data (numpy array or pandas Series): Input data
        - alpha (float, optional): Significance level for statistical tests (default=0.05)
        
    Returns:
        - outliers (list): List of outlier indices
    """
    mu, std = norm.fit(data)
    z_scores = (data - mu) / std
    p_values = 2 * (1 - norm.cdf(np.abs(z_scores)))
    outliers = np.where(p_values < alpha)[0]
    return outliers.tolist()
>>>>>>> master

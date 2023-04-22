from sklearn.decomposition import PCA
from sklearn.linear_model import RANSACRegressor
import numpy as np

def detect_outliers_linear_regression(data):
    """
    Detect outliers using linear regression models (PCA, LMS) method.
    
    Parameters:
        - data (numpy array or pandas DataFrame): Input data
        
    Returns:
        - outliers (list): List of outlier indices
    """
    pca = PCA(n_components=1)
    principal_components = pca.fit_transform(data)
    residuals = data - pca.inverse_transform(principal_components)
    
    model = RANSACRegressor()
    model.fit(principal_components, residuals)
    outliers = np.where(model.inlier_mask_ == False)[0]
    return outliers.tolist()

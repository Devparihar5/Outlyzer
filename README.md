# Outlyzer -A Python package to detect outliers in a dataset


Outlyzer is a Python library that provides various methods for detecting outliers in a dataset. It includes implementation of Z-score, IQR, and Mahalanobis distance methods for identifying outliers, as well as visualization-based methods using scatter plots, box plots, and other types of visualizations.


## Installation
You can install Outlyzer using pip:
```
pip install outlyzer
```


Usage:

    - Import the desired method from the library, e.g.:
        from Outlyzer.zscore import detect_outliers_zscore        
        from Outlyzer.iqr import detect_outliers_iqr

    - Pass your dataset or data series to the respective function, e.g.:
        outliers_zscore = detect_outliers_zscore(data)
        outliers_iqr = detect_outliers_iqr(data)
    
    The functions will return a boolean array indicating whether each data point is an outlier (True) or not (False).


## 
<p align="center">
  <a href="https://star-history.com/#devparihar5/Outlyzer&Date">
    <img src="https://api.star-history.com/svg?repos=Devparihar5/Outlyzer&type=Date" alt="Star History Chart">
  </a>
</p>

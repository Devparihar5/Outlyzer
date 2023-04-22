#create a sample dataset
import numpy as np
import pandas as pd
#import the breast cancer dataset
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
print(df.shape)
# #check the least squares method
# from Outlyzer.least_squares import detect_outliers_linear_regression

# dt = detect_outliers_linear_regression(df)
# print(dt)

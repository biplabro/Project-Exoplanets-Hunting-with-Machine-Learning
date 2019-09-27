# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values #[all rows, columns-1]all values
y = dataset.iloc[:,3].values

#taking care of missing data
#from sklearn.impute import simpleImputer
from sklearn.impute import SimpleImputer
#imputer object is created below
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean') #axis argument is deprecated in this version, Imputer is replaced by simpleImputer
#data fed to imputer below
imputer.fit(X[:, 1:3]) # Leftmost ':' represents whole column. '1' represents starting column. rightmost column '3' represents boundary; column 1& 2 is required
# transform method applied below
X[:, 1:3] = imputer.transform(X[:, 1:3])

# Feature Scaling


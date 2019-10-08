# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values #[all rows, columns-1]all values
dfX = pd.DataFrame(X) # dataframe created since object import is not supported in anaconda 2019.07
y = dataset.iloc[:,3].values
dfy = pd.DataFrame(y)

#taking care of missing data
#from sklearn.impute import simpleImputer
from sklearn.impute import SimpleImputer
#imputer object is created below
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean') #axis argument is deprecated in this version, Imputer is replaced by simpleImputer
#data fed to imputer below
imputer.fit(X[:, 1:3]) # Leftmost ':' represents whole column. '1' represents starting column. rightmost column '3' represents boundary; column 1& 2 is required
# transform method applied below
X[:, 1:3] = imputer.transform(X[:, 1:3])
dfX1 = pd.DataFrame(X)

# Encoding categorical data (assign numbers to Words)
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
dfX2 = pd.DataFrame(X)
from sklearn.preprocessing import OneHotEncoder 
#Creating Dummy Var.s for each of the countries
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
dfX3 = pd.DataFrame(X)
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
dfy3 = pd.DataFrame(y)

#splitting the dataset into training & test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#Feature scaling: putting variables in the same range despite their original values
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
 





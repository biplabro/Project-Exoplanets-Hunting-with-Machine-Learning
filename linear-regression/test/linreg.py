#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline			#for jupyter notebook

#input dataset
dataset = pd.read_csv('student_scores.csv')

#print dataset specs
print (dataset.shape)
print (dataset.head())
print (dataset.describe())

#plot the input data
dataset.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show()

#wrap data as row/column in x,y
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

#training set specs
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#linear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#debug output
print(regressor.intercept_)
print(regressor.coef_)

#prediction
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print (df)

#reference: 
#https://stackabuse.com/linear-regression-in-python-with-scikit-learn/

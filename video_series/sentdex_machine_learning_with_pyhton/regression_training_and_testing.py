import pandas as pd 
import quandl
import math
import numpy as np 
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close','Adj. Volume']]


df['HL_PCT'] = (df['Adj. High'] - df ['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'

df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
#print(df.head())

# Scaling is often used on features, and the goal is to get them somewhere
# in the range of -1 to +1. This helps with accuracy and processing speed.
# Sometimes it makes sense to not use it, however. We will also use cross
# validation to split between training and testing samples of data. We 
# are not to support vector machines, but you can use them on regression
# so let's use it here. 

# Generally, features will be a X and labels a y

# Fairly obvious
X = np.array(df.drop(['label'],1))
y = np.array(df['label'])

# Now to preprocesses our features
# To use with future values in real time, you would have to scale the incoming
# data and scale it alongside the training data. So if, for example, you were
# trying to engage in HFT you would most likely want to skip the preprocessing step
X = preprocessing.scale(X)
y = np.array(df['label'])
# Check to make sure length is the same!
print(len(X), len(y))

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression()
# Train
clf.fit(X_train, y_train)
# Test
accuracy = clf.score(X_test, y_test)

print(accuracy)

# Let's say we want to use support vector regression, you would only have to change
# LinearRegression() to svm.SVR(). No other code would change

# !! When you pull up the documentation of an algorithm, one of the most important
# things to look for is threading options. n_jobs is what you are looking for. You 
# can normally set n_jobs = -1 to run however many jobs are possible with your processor!!



# Pickling doesn't really have anything to do with regression, but it is a good 
# thing to have at your disposal to save time with things like not having to 
# train your classifiers everytime you want to use them.

# What is pickling? It is "serialization" of any python object (dicitonary, list, etc.)
# and in this case it is a classifier. Pickles are like a file: you can open it,
# save it, read it, etc. In this example where would we want to pickle the classifier?
# Right after we train it, because that is the most tedious step.
# Remember, we now live in a time where you can go online and spin up a server
# very cheaply. So if your computer is relatively slow, spinning up GPU clusters
# makes a lot of sense. 

import pandas as pd 
import quandl
import math
import datetime
import numpy as np 
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot')

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close','Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df ['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'

df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)
y = np.array(df['label'])
print(len(X), len(y))

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression()
clf.fit(X_train, y_train)
###
with open('linearregression.pickle', 'wb') as f:
	# This puts (dumps) the classifier into the file
	pickle.dump(clf, f)

# To use the classifier you do something like
pickle_in = open('linearregression.pickle', 'rb')
clf = pickle.load(pickle_in)
# After you do this once, you could now comment out the two previous lines
# and simply read the pickle from the file
###

accuracy = clf.score(X_test, y_test)

forecast_set = clf.predict(X_lately)

print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day


for i in forecast_set:
	next_date = datetime.datetime.fromtimestamp(next_unix)
	next_unix += one_day
	df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)

plt.xlabel('Date')
plt.ylabel('Price')
plt.show()


'''
When you have more than 2 groups, there are two methods of svm
OVR (one vs rest)
OVO (one vs one)

OVR treats all other groups as rest, run it for each group
Usually a little more processing for OVO but more balanced
'''

import numpy as np 
from sklearn import preprocessing, cross_validation, neighbors, svm
import pandas as pd 

df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = svm.SVC()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
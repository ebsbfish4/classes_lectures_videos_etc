'''
First classification algorithm we are going to look at is k nearest neighbors.
You want to use an odd number because otherwise votes could be tied. You 
can also model confidence bassed on what percentage of the votes, but
this will be different from the accuracy of the model. You can do this with
things like euclidean distance. This takes a long time to run on large datasets.
Things like SVM are much more efficient on large datasets. But even if you are working
with up to a GB of data, it can still operate pretty quickly by threading.

Included K-nearest neighbors application video

We will use scikit learn to work with this.
'''

import numpy as np 
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd 

df = pd.read_csv('breast-cancer-wisconsin.data')

# The reason we use -99999 is that most algorithms will recognize it
# as an outlier. A lot of real world data is missing a lot of values.
df.replace('?', -99999, inplace=True)

# What would some useless data be? Id for example

df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['class'],1))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,2,2,2,3,2,1]])

prediction = clf.predict(example_measures)
print(prediction)



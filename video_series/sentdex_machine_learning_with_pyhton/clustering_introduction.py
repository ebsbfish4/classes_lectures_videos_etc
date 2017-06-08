'''
Two major forms of clustering - Flat and Hierarchical
Flat - You tell the machine how many groups you want there to be
Hierarchical - The machine decides how many groups there should be 

K-means:
The only parameter you impose is K (number of groups)
K-means works by taking the entire dataset and randomly choosing centroids
After you choose you classify each data point by which centroid it is closest to
Take all the data points in each group and find the mean (center point) and
set those as the new centroids. Rinse and repeat. Keep repeating until the 
centroids are completely done moving. The one downside to k-means is that it
generally wants to cluster in close to similar sized groups because of 
adherence to distance. Mickey Mouse data example. You can change kernels but
it is difficult to fully address this problem. 
'''
import matplotlib.pyplot as plt 
from matplotlib import style
style.use('ggplot')
import numpy as np 
from sklearn.cluster import KMeans 

X = np.array([[1,2], [1.5, 1.8], [5, 8], [8, 8],[1,0.6],[9,11]])

# plt.scatter(X[:,0], X[:,1], s=150, linewidth=5)
# plt.show() 

clf = KMeans(n_clusters=2)
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_

colors = ["g.","r.","c.","b.","k.","o."]

for i in range(len(X)):
	plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=25)

plt.scatter(centroids[:,0], centroids[:,1], marker='x', s=150, linewidth=5)
plt.show()
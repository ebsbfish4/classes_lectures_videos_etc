'''
Also included next video writing our own....
Also included applying our K Nearest Neighbors...
Also included final thoughts on...

Our function has about the same performance on accuracy as 
scikitlearn k nearest neighbors, but theres runs faster because
it uses threading. Because testing k nearest neighbors involves 
each point being its own seperate data, you can thread it heavily.
it also does better because it uses the concept of radius to only 
test against points withoin a certain radius.
'''

from math import sqrt
import numpy as np
import warnings
from collections import Counter
import pandas as pd
import random

# [[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
# plt.scatter(new_features[0], new_features[1], s=100)
# plt.show()

def k_nearest_neighbors(data, predict, k=3):
	if len(data) >= k:
		warnings.warn('K is set to value less than total voting groups. Idiot!')

	distances = []
	for group in data:
		for features in data[group]:
			# this would work but numpy has an even more simple version
			# euclidean_distance = np.sqrt(np.sum((np.array(features) - np.array(predict))**2))
			# This way is faster
			euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
			distances.append([euclidean_distance, group])

	votes = [i[1] for i in sorted(distances)[:k]]
	vote_result = Counter(votes).most_common(1)[0][0]
	confidence = Counter(votes).most_common(1)[0][0] / k
	# print(vote_result, confidence)
	# print(Counter(votes).most_common(1))
	return vote_result, confidence


accuracies = []

for i in range(5):


	df = pd.read_csv("breast-cancer-wisconsin.data")
	df.replace('?', -99999, inplace=True)
	df.drop(['id'], 1, inplace=True)
	full_data = df.astype(float).values.tolist()

	random.shuffle(full_data)
	test_size = 0.2
	train_set = {2:[], 4:[]}
	test_set = {2:[], 4:[]}
	train_data = full_data[:-int(test_size*len(full_data))]
	test_data = full_data[-int(test_size*len(full_data)):]

	for i in train_data:
		train_set[i[-1]].append(i[:-1])

	for i in test_data:
		test_set[i[-1]].append(i[:-1])

	correct = 0
	total = 0 

	for group in test_set:
		for data in test_set[group]:
			vote, confidence = k_nearest_neighbors(train_set, data, k=5)
			if group == vote:
				correct += 1
			total += 1

	# print('Accuracy: {}'.format(correct/total))

	accuracies.append(correct/total)

print(sum(accuracies)/len(accuracies))





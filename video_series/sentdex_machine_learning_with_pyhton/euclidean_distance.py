'''
Everything in K-nearest neighbors hinges on euclidean distance. It is the
square root of the sum over all the dimensions of one point subtracted from
another point squared.
'''
from math import sqrt

plot1 = [1,3]
plot2 = [2,5]

euclidean_distance = sqrt( (plot1[0]-plot2[0])**2 + (plot1[1]-plot2[1])**2)

print(euclidean_distance)


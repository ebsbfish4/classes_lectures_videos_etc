#! python3

from matplotlib import pyplot as plt




x = [5,6,7,8]
y = [7,3,8,3]
plt.plot(x,y)

plt.title('Epic Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()

# A more realistic thing would be to have two functions generating
# the lists. A common error will say that x and y must have the same
# first dimension. This just means that they must have the same number
# of items in the list.

# You can use styles to save specific formats of charts. This helps
# make quick, good looking charts.


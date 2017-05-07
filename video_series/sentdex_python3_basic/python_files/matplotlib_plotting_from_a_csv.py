#! python3

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

# It is better to be able to use numpy to import files, because these
# are the types that mare most useful in data manipulation

# Numpy allows you to use arrays, which you cannot really use in regular
# python. This is useful, but when you try to do certain things with
# an array that you could do with python lists it will not work. You
# will have to convert back and forth between types. 

x,y = np.loadtxt('exampleFile.csv',
                 unpack = True,
                 delimiter = ',')


plt.plot(x,y)

plt.title('Epic Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()

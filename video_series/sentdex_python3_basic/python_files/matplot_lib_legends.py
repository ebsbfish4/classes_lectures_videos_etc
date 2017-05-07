#! python3

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5,6,7,8]
y = [7,3,8,3]

x2 = [5,6,7,8]
y2 = [6,7,2,6]

plt.plot(x,y,'g', linewidth=5, label='Line 1')
plt.plot(x2,y2,'c',linewidth=10, label='Line 2')

plt.title('Epic Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.grid(True, color='k')


plt.show()

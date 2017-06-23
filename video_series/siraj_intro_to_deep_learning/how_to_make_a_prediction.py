"""
Machine learning defines outcome first and then learns how to get there

Many-layer deep neural networks are called deep learning

Machine learning classified into 3
Supervised, Unsupervised, Reinforcement learning

Reinforcement learing is linked to the idea of learning through
trial and error
"""

import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt 

df = pd.read_fwf('brain_body.txt')

x_values = df[['Brain']]
y_values = df[['Body']]

body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.show()



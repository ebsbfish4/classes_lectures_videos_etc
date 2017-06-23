'''
Use tensorflow to classify housing prices

Google created tensorflow to scale well and be reliable. Google search uses tensorflow.
'''

import pandas as pd # Work with data as tables
import numpy as np # use number matrices
import matplotlib.pyplot as plt 
import tensorflow as tf 

#Load the data

df = pd.read_csv('housing_data.csv')
df = df.drop(['index', 'price', 'sq_price'], axis=1)
df = df[0:10]

#Step 2 - add labels
# 1 is good, zero is a bad buy
df.loc[:, ('y1')] = [1,1,1,0,0,1,0,1,1,1]
#y2 is negation of y1
df.loc[:, ('y2')] = df['y1'] == 0
df.loc[:, ('y2')] = df['y2'].astype(int)

#Step 3 - Prepare data for tensorflow
#In general, we will convert into to tensors
#tensors are a generic version of vectors and matrices
#vector - list of numbers (1d tensor)
#matrix si a list of list of numbers (2d tensor)
# list of list of list of numbers (3d tensor)
# .....
#tensors are how we represent data in tensorflow

#Convert features to input tensor
inputX = df.loc[:, ['area', 'bathrooms']].as_matrix()
#convert labels to input tensor
inputY = df.loc[:, ['y1', 'y2']].as_matrix()

#Step 4 - write out our hyperparameters
learning_rate = 0.000001
training_epochs = 2000
display_step = 50
n_samples = inputY.size

#Step5 - Create our computation graph/neural network
#for feature input tensors, none means any number of examples
#placeholders are gateways for data in our computation graph
x = tf.placeholder(tf.float32, [None,2])

#create weights
#2x2 float matrix that will keep updating through training process
#training process
#variables in tf hold and update parameters
#in memory buffers containing tensors
W = tf.Variable(tf.zeros([2,2]))

#add biases (example is b in y = mx + b)
b = tf.Variable(tf.zeros([2]))

#multiply our weights by our inputs, first calculation
#weights are how we govern how data flows in our computation graph
#multiply input by weights and add biases
y_values = tf.add(tf.matmul(x, W), b)

#apply softmax to value we just created
#softmax is our activation function
#normalizes our value (takes our value )
y = tf.nn.softmax(y_values)

#feed in a matrix of labels
y_ = tf.placeholder(tf.float32, [None,2])

#Step 6 - perform training
#create our cost function, mean squared error
#reduce sum computes the sum of elements across dimensions of a tensor
cost = tf.reduce_sum(tf.pow(y_ - y, 2))/(2*n_samples)
#gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

#initialize variables and tensorflow sessions
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

#training loop
for i in range(training_epochs):
	sess.run(optimizer, feed_dict={x: inputX, y_: inputY})

	#write out logs of training
	if (i) % display_step == 0:
		cc = sess.run(cost, feed_dict={x: inputX, y_: inputY })
		print('Step:', i, 'Cost:', sess.run(cost, feed_dict={x: inputX, y_: inputY}))


print('Optimization finished!')
training_cost = sess.run(cost, feed_dict={x: inputX, y_: inputY})
print('Training cost=', training_cost, 'W=', sess.run(W), 'b=', sess.run(b))

sess.run(y, feed_dict={x: inputX})
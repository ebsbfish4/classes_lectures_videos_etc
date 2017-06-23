'''
Each neuron has a job of
1. receive signal
2. analyze signal
3. pass information along

'''

import numpy as np

class NeuralNetwork():
	def __init__(self):
		np.random.seed(1)

		self.synaptic_weights = 2*np.random.random((3,1)) - 1

	def __sigmoid(self, x):
		return 1/(1 + np.exp(-x))

	def predict(self, inputs):
		return self.__sigmoid(np.dot(inputs, self.synaptic_weights))

	def train(self, training_set_inputs, training_set_outputs, number):
		for iteration in range(number):
			output = self.predict(training_set_inputs)

			error = training_set_inputs - output

			adjustment = np.dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

	def __sigmoid_derivative(self, x):
		return x * (1-x)



if __name__ == '__main__':

	neural_network = NeuralNetwork()

	print('Random starting synaptic weights:')
	print(neural_network.synaptic_weights)

	training_set_inputs = np.array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])
	training_set_outputs = np.array([[0,1,1,0]]).T

	neural_network.train(training_set_inputs, training_set_outputs, 10000)

	print('New synaptic weights:')
	print(neural_network.synaptic_weights)

	print('predicting:')
	print(neural_network.predict([1,0,0]))

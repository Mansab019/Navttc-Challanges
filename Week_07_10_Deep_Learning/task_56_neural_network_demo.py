# Task 56 - Neural Networks from Scratch
# Reference: https://www.analyticsvidhya.com/blog/2020/07/neural-networks-from-scratch-in-python-and-r

import numpy as np

# Sigmoid activation
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Simple Neural Network (1 hidden layer)
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.W1 = np.random.randn(input_size, hidden_size)
        self.W2 = np.random.randn(hidden_size, output_size)

    def forward(self, X):
        self.z1 = np.dot(X, self.W1)
        self.a1 = sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2)
        self.a2 = sigmoid(self.z2)
        return self.a2

    def backward(self, X, y, lr=0.1):
        m = X.shape[0]
        dz2 = self.a2 - y
        dW2 = np.dot(self.a1.T, dz2) / m
        dz1 = np.dot(dz2, self.W2.T) * sigmoid_derivative(self.a1)
        dW1 = np.dot(X.T, dz1) / m
        self.W1 -= lr * dW1
        self.W2 -= lr * dW2

    def train(self, X, y, epochs=1000):
        for i in range(epochs):
            output = self.forward(X)
            self.backward(X, y)
            if i % 200 == 0:
                loss = np.mean((y - output) ** 2)
                print(f"Epoch {i}, Loss: {loss:.4f}")

# XOR problem
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

nn = NeuralNetwork(2, 4, 1)
nn.train(X, y, epochs=1000)

print("\nPredictions:")
print(nn.forward(X))

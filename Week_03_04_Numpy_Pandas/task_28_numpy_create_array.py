# Task 28 - Create Numpy Arrays
# Reference: https://www.w3schools.com/python/numpy_creating_arrays.asp

import numpy as np

# From Python list
arr = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr)

# 2D Array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2d)

# Built-in methods
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
eye = np.eye(3)
arange = np.arange(0, 20, 2)
linspace = np.linspace(0, 1, 5)

print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Identity:\n", eye)
print("Arange:", arange)
print("Linspace:", linspace)

# Random arrays
rand = np.random.rand(3, 3)
randint = np.random.randint(1, 100, (3, 3))
print("Random:\n", rand)
print("Random Int:\n", randint)

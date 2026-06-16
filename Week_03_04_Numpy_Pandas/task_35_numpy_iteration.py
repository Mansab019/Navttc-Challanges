# Task 35 - Numpy Array Iteration
# Reference: https://www.w3schools.com/python/numpy_array_iterating.asp

import numpy as np

arr1d = np.array([1, 2, 3])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# 1D iteration
for x in arr1d:
    print(x)

# 2D iteration
for row in arr2d:
    print(row)

# Element by element in 2D
for row in arr2d:
    for val in row:
        print(val)

# nditer - best way
for val in np.nditer(arr2d):
    print(val)

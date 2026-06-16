# Task 37 - Numpy Array Splitting
# Reference: https://www.w3schools.com/python/numpy_array_split.asp

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# Split into 3
result = np.array_split(arr, 3)
print("Split into 3:", result)

# Split into unequal parts
result = np.array_split(arr, 4)
print("Split into 4:", result)

# 2D splitting
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
result = np.array_split(arr2d, 2)
print("2D Split:\n", result)

# hsplit and vsplit
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("HSplit:\n", np.hsplit(a, 2))
print("VSplit:\n", np.vsplit(a, 2))

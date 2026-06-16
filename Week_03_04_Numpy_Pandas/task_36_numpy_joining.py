# Task 36 - Numpy Array Joining
# Reference: https://www.w3schools.com/python/numpy_array_join.asp

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Concatenate 1D
joined = np.concatenate((a, b))
print("Concatenated:", joined)

# Concatenate 2D
a2d = np.array([[1, 2], [3, 4]])
b2d = np.array([[5, 6], [7, 8]])

row_join = np.concatenate((a2d, b2d), axis=0)  # row-wise
col_join = np.concatenate((a2d, b2d), axis=1)  # col-wise
print("Row join:\n", row_join)
print("Col join:\n", col_join)

# Stack
stacked = np.stack((a, b), axis=0)
print("Stacked:\n", stacked)

hstack = np.hstack((a, b))
vstack = np.vstack((a, b))
print("HStack:", hstack)
print("VStack:\n", vstack)

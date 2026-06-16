# Task 30 - Numpy Array Slicing
# Reference: https://www.w3schools.com/python/numpy_array_slicing.asp

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])    # [2 3 4 5]
print(arr[::2])    # every 2nd element
print(arr[::-1])   # reverse

# 2D slicing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0:2, 1:3])   # rows 0-1, cols 1-2
print(arr2d[:, 1])        # all rows, col 1
print(arr2d[1, :])        # row 1, all cols

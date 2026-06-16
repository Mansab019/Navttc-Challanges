# Task 29 - Numpy Array Indexing
# Reference: https://www.w3schools.com/python/numpy_array_indexing.asp

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Basic indexing
print(arr[0])    # 10
print(arr[-1])   # 50
print(arr[1] + arr[2])  # 50

# 2D indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0, 0])   # 1
print(arr2d[1, 2])   # 6
print(arr2d[2, -1])  # 9

# Logical/Boolean selection
arr = np.array([1, 2, 3, 4, 5, 6])
bool_arr = arr > 3
print("Boolean mask:", bool_arr)
print("Filtered:", arr[bool_arr])
print("Direct filter:", arr[arr % 2 == 0])

# Task 39 - Numpy Array Sorting
# Reference: https://www.w3schools.com/python/numpy_array_sort.asp

import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

# Sort ascending
print("Sorted:", np.sort(arr))

# Sort descending
print("Descending:", np.sort(arr)[::-1])

# 2D sort (sorts each row)
arr2d = np.array([[3, 1, 2], [9, 4, 7]])
print("2D Sorted:\n", np.sort(arr2d))

# argsort - returns indices that would sort the array
arr = np.array([30, 10, 50, 20])
print("Argsort:", np.argsort(arr))

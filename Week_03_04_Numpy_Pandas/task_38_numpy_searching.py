# Task 38 - Numpy Array Searching
# Reference: https://www.w3schools.com/python/numpy_array_search.asp

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 3, 2, 1])

# where()
result = np.where(arr == 4)
print("Indices where value is 4:", result)

result = np.where(arr > 3)
print("Indices where value > 3:", result)

# searchsorted (binary search on sorted array)
sorted_arr = np.array([1, 2, 3, 4, 5])
idx = np.searchsorted(sorted_arr, 3)
print("Insert position for 3:", idx)

# Find min/max index
print("Index of max:", np.argmax(arr))
print("Index of min:", np.argmin(arr))

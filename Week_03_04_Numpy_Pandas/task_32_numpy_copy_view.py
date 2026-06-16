# Task 32 - Numpy Array Copy vs View
# Reference: https://www.w3schools.com/python/numpy_copy_vs_view.asp

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# View - changes affect original
view = arr.view()
view[0] = 99
print("Original after view change:", arr)  # affected

# Copy - changes don't affect original
arr2 = np.array([1, 2, 3, 4, 5])
copy = arr2.copy()
copy[0] = 99
print("Original after copy change:", arr2)  # not affected

# Check ownership
print("View owns data:", view.base is arr)
print("Copy owns data:", copy.base is None)

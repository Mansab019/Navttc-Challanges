# Task 31 - Numpy Data Types
# Reference: https://www.w3schools.com/python/numpy_data_types.asp

import numpy as np

# Check dtype
arr = np.array([1, 2, 3])
print("Default dtype:", arr.dtype)

arr_float = np.array([1.1, 2.2, 3.3])
print("Float dtype:", arr_float.dtype)

arr_str = np.array(['a', 'b', 'c'])
print("String dtype:", arr_str.dtype)

# Specify dtype
arr = np.array([1, 2, 3], dtype='float64')
print("Specified float:", arr)

arr = np.array([1.9, 2.8, 3.7], dtype='int32')
print("Specified int (truncated):", arr)

# Type casting
arr = np.array([1, 2, 3])
arr_float = arr.astype('float64')
print("Casted to float:", arr_float)

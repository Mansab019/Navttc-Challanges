# Task 33 - Numpy Array Shape
# Reference: https://www.w3schools.com/python/numpy_array_shape.asp

import numpy as np

arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("1D shape:", arr1d.shape)   # (5,)
print("2D shape:", arr2d.shape)   # (2, 3)
print("3D shape:", arr3d.shape)   # (2, 2, 2)

print("ndim 1D:", arr1d.ndim)
print("ndim 2D:", arr2d.ndim)
print("size:", arr2d.size)

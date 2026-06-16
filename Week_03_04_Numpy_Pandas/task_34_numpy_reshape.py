# Task 34 - Numpy Array Reshaping
# Reference: https://www.w3schools.com/python/numpy_array_reshape.asp

import numpy as np

arr = np.arange(1, 13)
print("Original:", arr)

# Reshape to 2D
arr2d = arr.reshape(3, 4)
print("3x4:\n", arr2d)

# Reshape to 3D
arr3d = arr.reshape(2, 3, 2)
print("2x3x2:\n", arr3d)

# Flatten back to 1D
flat = arr2d.flatten()
print("Flattened:", flat)

# -1 lets numpy calculate dimension automatically
auto = arr.reshape(4, -1)
print("4x?:\n", auto)

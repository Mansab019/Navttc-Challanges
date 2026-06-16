# Task 40 - Numpy Random
# Reference: https://www.w3schools.com/python/numpy_random.asp

import numpy as np

# Random float between 0-1
print(np.random.rand())

# Random array
print(np.random.rand(3, 3))

# Random integer
print(np.random.randint(1, 100))

# Random choice
arr = np.array([1, 2, 3, 4, 5])
print(np.random.choice(arr))

# Shuffle
np.random.shuffle(arr)
print("Shuffled:", arr)

# Seed for reproducibility
np.random.seed(42)
print(np.random.rand(3))

# Normal distribution
normal = np.random.normal(loc=0, scale=1, size=5)
print("Normal dist:", normal)

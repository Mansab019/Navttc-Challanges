# Task 50 - Standard Deviation
# Reference: https://www.w3schools.com/python/python_ml_standard_deviation.asp

import statistics
import numpy as np

data = [10, 20, 30, 40, 50, 60, 70]

# Standard Deviation
std = statistics.stdev(data)
print(f"Standard Deviation: {std}")

# Variance
variance = statistics.variance(data)
print(f"Variance: {variance}")

# Using NumPy
np_std = np.std(data)
np_var = np.var(data)
print(f"NumPy Std Dev: {np_std}")
print(f"NumPy Variance: {np_var}")

# What it means
print("\n--- Interpretation ---")
print(f"Mean: {np.mean(data)}")
print(f"Most values fall within {np.mean(data) - np_std:.2f} and {np.mean(data) + np_std:.2f}")

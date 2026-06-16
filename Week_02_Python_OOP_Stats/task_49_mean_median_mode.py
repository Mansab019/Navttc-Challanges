# Task 49 - Mean, Median and Mode
# Reference: https://www.w3schools.com/python/python_ml_mean_median_mode.asp

import statistics
import numpy as np
from scipy import stats

data = [10, 20, 30, 20, 40, 50, 20, 60]

# Mean
mean = statistics.mean(data)
print(f"Mean: {mean}")

# Median
median = statistics.median(data)
print(f"Median: {median}")

# Mode
mode = statistics.mode(data)
print(f"Mode: {mode}")

# Using NumPy for mean
np_mean = np.mean(data)
print(f"NumPy Mean: {np_mean}")

# Using SciPy for all three
sp_mode = stats.mode(data)
print(f"SciPy Mode: {sp_mode.mode}")

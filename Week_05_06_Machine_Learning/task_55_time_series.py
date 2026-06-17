# Task 55 - Time Series Analysis
# Reference: https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample time series data
np.random.seed(42)
dates = pd.date_range(start='2024-01-01', periods=100, freq='D')
values = np.cumsum(np.random.randn(100)) + 50

ts = pd.Series(values, index=dates)
print("Time Series Head:\n", ts.head())

# Basic stats
print("\nMean:", ts.mean())
print("Std:", ts.std())

# Rolling average (moving average)
rolling_mean = ts.rolling(window=7).mean()

# Resample to weekly
weekly = ts.resample('W').mean()
print("\nWeekly Resampled:\n", weekly.head())

# Plot
plt.figure(figsize=(10, 5))
plt.plot(ts, label='Daily', alpha=0.5)
plt.plot(rolling_mean, label='7-Day Rolling Mean', color='red')
plt.title('Time Series Analysis')
plt.legend()
plt.savefig('Week_05_06_Machine_Learning/time_series_plot.png')
plt.show()

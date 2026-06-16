# Task 43 - Pandas Series
# Reference: https://www.w3schools.com/python/pandas_series.asp

import pandas as pd

# Create Series
s = pd.Series([10, 20, 30, 40, 50])
print(s)

# Custom index
s2 = pd.Series([100, 200, 300], index=["a", "b", "c"])
print(s2)
print(s2["b"])

# From dictionary
data = {"name": "Mansab", "age": 21, "city": "Lahore"}
s3 = pd.Series(data)
print(s3)

# Operations
print(s * 2)
print(s[s > 20])

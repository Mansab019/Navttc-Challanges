# Task 47 - Pandas Data Cleaning
# Reference: https://www.w3schools.com/python/pandas_cleaning.asp

import pandas as pd
import numpy as np

data = {
    "Name": ["Ali", "Sara", None, "Mansab", "Zara"],
    "Age": [21, None, 23, 22, 28],
    "Score": [85, 90, 78, None, 88]
}
df = pd.DataFrame(data)
print("Original:\n", df)

# Check nulls
print("\nNull values:\n", df.isnull())
print("\nNull count:\n", df.isnull().sum())

# Drop rows with nulls
df_dropped = df.dropna()
print("\nAfter dropna:\n", df_dropped)

# Fill nulls
df_filled = df.fillna({"Age": df["Age"].mean(), "Score": 0, "Name": "Unknown"})
print("\nAfter fillna:\n", df_filled)

# Remove duplicates
df2 = pd.DataFrame({"A": [1, 1, 2, 3], "B": [4, 4, 5, 6]})
print("\nDuplicates removed:\n", df2.drop_duplicates())

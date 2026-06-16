# Task 44 - Pandas DataFrame
# Reference: https://www.w3schools.com/python/pandas_dataframes.asp

import pandas as pd

# Create DataFrame
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Mansab"],
    "Age": [21, 25, 23, 22],
    "City": ["Lahore", "Karachi", "Islamabad", "Lahore"],
    "Score": [85, 90, 78, 95]
}

df = pd.DataFrame(data)
print(df)

# Access columns
print(df["Name"])
print(df[["Name", "Score"]])

# Access rows
print(df.loc[0])         # by label
print(df.iloc[1])        # by index

# Info
print(df.shape)
print(df.dtypes)
print(df.describe())

# Task 46 - Pandas Data Analysis
# Reference: https://www.w3schools.com/python/pandas_analyzing.asp

import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Mansab", "Zara"],
    "Age": [21, 25, 23, 22, 28],
    "Score": [85, 90, 78, 95, 88]
}
df = pd.DataFrame(data)

print(df.head())
print(df.tail(2))
print(df.info())
print(df.describe())
print(df["Score"].mean())
print(df["Score"].max())
print(df["Score"].min())
print(df["Age"].value_counts())
print(df["Name"].unique())
print(df["Name"].nunique())

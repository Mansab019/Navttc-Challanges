# Task 45 - Pandas Read CSV
# Reference: https://www.w3schools.com/python/pandas_csv.asp

import pandas as pd

# Create sample data and save as CSV
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Mansab"],
    "Age": [21, 25, 23, 22],
    "Score": [85, 90, 78, 95]
}
df = pd.DataFrame(data)
df.to_csv("sample.csv", index=False)
print("CSV saved!")

# Read CSV
df_read = pd.read_csv("sample.csv")
print(df_read)

# head and tail
print(df_read.head(2))
print(df_read.tail(2))

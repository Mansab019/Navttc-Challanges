# Task 48 - Pandas Data Correlation
# Reference: https://www.w3schools.com/python/pandas_correlations.asp

import pandas as pd

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Score": [40, 50, 55, 65, 70, 80, 85, 95],
    "Sleep_Hours": [8, 7, 7, 6, 6, 5, 5, 4]
}
df = pd.DataFrame(data)

# Correlation matrix
print("Correlation Matrix:\n", df.corr())

# Specific correlation
print("\nStudy Hours vs Score:", df["Study_Hours"].corr(df["Score"]))
print("Sleep Hours vs Score:", df["Sleep_Hours"].corr(df["Score"]))

# Interpretation:
# Close to 1 = strong positive correlation
# Close to -1 = strong negative correlation
# Close to 0 = no correlation

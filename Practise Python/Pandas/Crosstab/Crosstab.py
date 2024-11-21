import pandas as pd

# Create a sample dataframe
data = {
    "Name": ["John", "Mike", "John", "Mike"],
    "Item": ["apple", "car", "banana", "bike"],
    "Quantity": [1, 2, 3, 4],
}
df = pd.DataFrame(data)

# Use the crosstab function to create a cross-tabulation of the Name and Item columns
table_cross = pd.crosstab(df["Name"], df["Item"])
print(table_cross)


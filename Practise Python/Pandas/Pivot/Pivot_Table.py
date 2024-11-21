import pandas as pd

# Create a sample dataframe
data = {
    "Name": ["John", "Mike", "John", "Mike"],
    "Item": ["apple", "car", "banana", "bike"],
    "Quantity": [1, 2, 3, 4],
}
df = pd.DataFrame(data)

# Use the pivot_table function to create a pivot table
table = df.pivot_table(index="Name", columns="Item", values="Quantity", aggfunc="sum")
print(table)


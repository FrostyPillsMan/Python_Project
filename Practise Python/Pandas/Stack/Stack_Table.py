import pandas as pd


# Create a sample dataframe
data = {
    "Name": ["John", "Mike", "John", "Mike"],
    "Item": ["apple", "car", "banana", "bike"],
    "Quantity": [1, 2, 3, 4],
}
df = pd.DataFrame(data)

# Pivot the DataFrame
table = df.pivot_table(index="Name", columns="Item", values="Quantity", fill_value=0)

# Use the stack function to change the shape of pivoted DataFrame
df_stack = table.stack()
# Use the unstack function to change the shape of the stacked DataFrame
df_unstack = df_stack.unstack()

# Display results
print("Original DataFrame:\n", df)
print("\nPivoted Table:\n", table)
print("\nStacked DataFrame:\n", df_stack)
print("\nUnstacked DataFrame:\n", df_unstack)


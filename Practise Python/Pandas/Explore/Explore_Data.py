import pandas as pd

# Create a sample dataframe
data = {
    "Name": ["John", "Mike"],
    "Items": [["apple", "banana", "orange"], ["car", "bike"]],
}
df = pd.DataFrame(data)
# print(df)

# Use the explode function to transform the 'Items' column into multiple rows

df_explode = df.explode("Items")
print(df_explode)


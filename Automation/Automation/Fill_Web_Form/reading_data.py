import pandas as pd

try:
    df = pd.read_csv("fake_data.csv")
    print(df)
except FileNotFoundError:
    print(
        "Error: The file 'fake_data.csv' does not exist."
    )
except pd.errors.ParserError:
    print(
        "Error: There was a problem parsing the CSV file. Ensure it is correctly formatted."
    )

"""
for i in range(0, len(df)):
    for column in df.columns:
        print(column)
        print(df.loc[i, column])
"""


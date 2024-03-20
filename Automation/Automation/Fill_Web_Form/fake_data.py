import pandas as pd
from faker import Faker

# create fake data: Name, Email, Address
fake = Faker()
profiles = [fake.profile() for i in range(10)]

# store fake data in Pandas
df = pd.DataFrame(profiles)
df = df[["Name", "Email", "Address"]]
# selecting specified columns from table data

# create fake data: phone number, comment
contact_number = [fake.phone_number() for i in range(0, 10)]
comments = ["This is good!"] * 10

# store fake data in Pandas
df["Phone number"] = contact_number
df["Comments"] = comments

# export data to csv file
df.to_csv("fake_data.csv", index=False)



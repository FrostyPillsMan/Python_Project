# Scenario 1
animals = {"Cat": 20, "Dog": 35, "Giraffe": 40}
print(isinstance(animals, dict))
# Output --> True

# Scenario 2
# Tuple arg
message = (["WkWk"], (str, int))
print(isinstance(message, (list, tuple)))
print(isinstance(message[1][1], int))
print(isinstance(message[1], dict))
# Output --> True
# Output --> False
# Output --> False
print("\n")


# Scenario 3
def register_username(name, age, email):
    # Checking each data type from user input is correct.
    if not isinstance(name, str):
        return "Name should Not be a string."
    if not isinstance(age, int):
        return "Age should be an integer."
    if not isinstance(email, str):
        return "Email should be a string."

    user_data = {"Name": name, "Age": age, "Email": email}
    return "User registered successfully with data: {}".format(user_data)


# Creating argument for user_registration
user_name = "Adam"
user_age = "Meow"
user_email = "adamtangmch@gmail.com"

register_user = register_username(user_name, user_age, user_email)
print(register_user)

# Output
# Age should be an integer.

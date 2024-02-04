# Scenario 2

import string
import secrets

"""
secrets module

Generate random numbers managing important data
- passwords, account authentication, security tokens
"""


all_alphabets = string.ascii_letters + string.digits + string.punctuation
# print(f"Alphanumeric string: {all_alphabets}")


# Generate password
def generate_password(length=15):
    pwd_combined = "".join(secrets.choice(all_alphabets) for i in range(length))
    return pwd_combined


pwd_result = generate_password()
print(f"Generated Password: {pwd_result}")

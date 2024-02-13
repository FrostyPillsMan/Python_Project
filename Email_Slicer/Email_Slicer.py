import re

user_email = input("Enter your email address : ")

extract_pattern = r"([\w]+)@([\w]+\.[\w]+)"
# Extract the stated email address.
matched_string = re.match(extract_pattern, user_email)
# Checks for matching between extract pattern and the email address.

if matched_string:
    username = matched_string.group(1)
    # Returns the string from first subgroups index
    domain = matched_string.group(2)
    # Returns the string from second subgroups index

    print(f"Extraction of the Username: {username}")
    print(f"Extraction of the Domain: {domain}")

else:
    print("Invalid email address provided.")

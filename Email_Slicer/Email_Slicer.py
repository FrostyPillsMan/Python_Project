import re

user_email = input("Enter your email address : ").lower()

extract_pattern = r"([\w]+)@([\w]+\.[\w]+)"
# extract the stated email address.
matched_string = re.match(extract_pattern, user_email)
# checks for matching between extract pattern and the email address.

username = matched_string.group(1)
# returns the string from first subgroups index
domain = matched_string.group(2)
# returns the string from second subgroups index

print(f"Extraction of the Username: {username}")
print(f"Extraction of the Domain: {domain}")



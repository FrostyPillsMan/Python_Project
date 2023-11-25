import string
import getpass


def get_pass_strength_checker():
    user_password = getpass.getpass("Enter the Password: ")
    pass_strength = 0

    """
    # Checking any values from each character type returns value of "1", with a string function. 

    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in user_password])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in user_password])
    digits = any([1 if c in string.digits else 0 for c in user_password])
    char_space = any([1 if c in string.whitespace else 0 for c in user_password])
    special = any([1 if c in string.punctuation else 0 for c in user_password])
    """

    upper_count = 0
    lower_count = 0
    digit_count = 0
    char_count = 0
    special_count = 0

    for char in list(user_password):
        if char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.digits:
            digit_count += 1
        elif char in string.whitespace:
            char_count += 1
        elif char in string.punctuation:
            special_count += 1

    if len(user_password) > 8:
        pass_strength += 1
    if len(user_password) > 12:
        pass_strength += 1
    if len(user_password) > 17:
        pass_strength += 1
    if len(user_password) > 20:
        pass_strength += 1
    if len(user_password) > 25:
        pass_strength += 1

    if pass_strength == 1:
        print("Weak Password")
    elif pass_strength == 2:
        print("Medium Password")
    elif pass_strength == 3:
        print("Strong Password")
    elif pass_strength == 4:
        print("Very Strong Password")
    elif pass_strength == 5:
        print("Excellent Password")

    print(f"{upper_count} uppercase letters")
    print(f"{lower_count} lowercase letters")
    print(f"{digit_count} digit letters")
    print(f"{char_count} whitespaces letters")
    print(f"{special_count} special letters")
    print(f"{pass_strength} out of 5")


get_pass_strength_checker()


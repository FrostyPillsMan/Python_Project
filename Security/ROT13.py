import string
# import codecs

def rot13_translator():
    lowercase: str = string.ascii_lowercase
    uppercase: str = string.ascii_uppercase

    shift: int = 13

    shift_lowercase: str = lowercase[shift:] + lowercase[:shift]
    shift_uppercase: str = uppercase[shift:] + uppercase[:shift]
    
    translator: dict = str.maketrans(lowercase + uppercase, shift_lowercase + shift_uppercase)
    return translator
    
def rot13(message: str):
    table: dict = rot13_translator()
    return message.translate(table)

def main():
    user_input: str = input("Your Message: ")

    encrypted_message: str = rot13(user_input)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message: str = rot13(encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")


if __name__ == "__main__":
    main()




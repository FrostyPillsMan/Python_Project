sum_odd_digits = 0
sum_even_digits = 0
total = 0

card_number = input("Enter the credit card #: ")
card_number = card_number.replace("-", "").replace(" ", "")
card_number = card_number[::-1]
# reverse the last line of character string and moves to the first character.
print(card_number)


# Example: if credit card number is "123456789", ::2 will give you "13579".
for x in card_number[::2]:
    sum_odd_digits += int(x)
    # convert string to int of sum_odd_digits
    # combine all the digits in the odd places from right to left

# Example : reverse card number: 0987654321
# x = 9(index 1), x = 7(index 3), x = 5(index 5), x =3(index 7)
# These digits will reverse to 3,5,7,9
for x in card_number[1::2]:
    x = int(x) * 2
    # Let's say the number is 9, times 2 is 18
    if x >= 10:
        sum_even_digits += 1 + (x % 10)
        # 18 is then turn to 8 from modulus and add 1 equals to 9
    else:
        sum_even_digits += x
        # number is lesser than 10

total = sum_odd_digits + sum_even_digits

# Checks the total value is divisible evenly by 10.
if total % 10 == 0:
    print("Card is Valid")
else:
    print(" Card is Invalid")

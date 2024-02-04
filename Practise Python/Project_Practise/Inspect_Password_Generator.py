# Scenario 1
import random


lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"
all = lower + upper + numbers + symbols

# Set password length
length = 60

password = "".join(random.sample(all, length))
# Return new list of password elements chosen from sequence.

print(f"Your password is :", {password})



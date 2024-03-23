"""
shortcut of condition statement 

"""

condition = True
x = 1 if condition else 0

print(f"x is {x}\n")
# Output is 1

"""
shortcut of having commas numbers especially 
handling large data sets

"""

num1 = 100_000_00_00
num2 = 100_000_000

total = num1 + num2

print(f"total is {total:,}\n")
# Output is 1,100,000,000

"""
shortcut of File Handling of reading from files

"""

try:
    with open("./Practise/file_name", "r") as f:
        # Open the file of random.text format from Practise folder
        # declare as read file command
        file_contents = f.read()
        # declare variable of file_content == file details report

    words = file_contents.split(" ")
    # declare variable of file details as a list
    word_count = len(words)
    print(f"The word_count is {word_count}")
    print(f"{words}\n")
except FileNotFoundError:
    print("The file 'random.txt' does not exist. ")

# Output is The word_count is 3
# Output is ['user:', 'jinx@reload\npass:', 'LinkotheGym']

"""
shortcut of displaying list of names in index

"""

names = ["Corey", "Chris", "Dave", "Travis"]

for index, name in enumerate(names, start=1):
    print(index, name)
    # Output is list of names with index

"""
shortcut of displaying both list names 
in one statement

"""

names = ["Meow", "Geek", "Wow", "Bruce"]
heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]

for name, hero in zip(names, heroes):
    print(f"\n{name} is actually {hero}")
    # Output is Meow is Spiderman

"""
shortcut of unpacking data 

"""

a, b, *_, d = (1, 2, 3, 4, 5)
# third variable removes 3 and 4 values

print("\n", a, b, d)
# Output is 1 2 5

"""
Shortcut of Class attributes 

"""


class Person:
    pass


person = Person()

person_info = {"first": "Adam", "last": "Levine"}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))

# Output is Adam Levine

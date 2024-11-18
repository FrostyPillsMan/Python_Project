"""
*args = allows you to pass multiple non-key arguments
"""


def add(*nums):
    print(type(nums))
    total_added = sum([num for num in nums])
    return total_added


print(add(1, 2, 3, 4, 5))
print("----------------------------", end="\n")

# Error occurrred
"""def add(nums):
    total_added = sum([num for num in nums])
    return total_added


print(add(1, 2, 3, 4, 5))

# TypeError: add() takes 1 positional argument but 5 were given.
"""

"""
**kwargs = allows you to pass multiple keyword-arguments
"""


def greet(**users):
    for key, value in users.items():
        print(f"{key} => {value}")


def display(**users):
    greet(State="United Kingdom", city="London", users=["Adam", "Aiman", "Jievan"])
    print(type(users))


if __name__ == "__main__":
    display()
    print("----------------------------", end="\n")

"""
Using both *args && **kwargs
"""


def order_pizza(size, *topping, **other):
    print(f"I would love {size} pizza please.".upper())
    for top in topping:
        print(f"--> {top} to the pizza.")
    for _, value in other.items():
        print(f"--> {_} sauce with {value}")


order_pizza("Large", "Pepperoni", "Steak", "Tomato", "Mushroom")

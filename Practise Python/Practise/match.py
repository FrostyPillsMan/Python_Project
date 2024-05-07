from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

try:
    color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
except ValueError as err:
    print(f"{err} is not right colour!")
finally:
    print("Good Choice!")

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")



# Basic Data Types
from typing import List

# The line `from typing import List` is importing the `List` type hint from the `typing` module. This
# Allows us to use the `List` type hint to indicate that a variable is a list.


name: str = "Adam"
cars: list[str] = ["Porsche", "Mclaren"]
employee_id: dict[int, str] = {2039: "Jennifer Blyat", 9043: "Cyka Pizdet"}


print(type(name))
print(type(cars))
print(type(employee_id))
print("------------------------------------------------------------")

# Define Constant Using Final Type
from typing import Final

# The line `from typing import Final` is importing the `Final` type hint from the `typing` module.

PRICE_RATE: Final[int] = 200
# `Final` type hint is used to indicate that a variable is a constant and cannot be reassigned.

# In the code example, `PRICE_RATE` is declared as a constant with the value of 200, and any attempt to reassign it will result in an error.

# Exp: PRICE_RATE = 300
# Error "PRICE_RATE" is declared as Final and cannot be reassigned
print("------------------------------------------------------------")


# Add Multiple Type Hints to One Variable
from typing import Union

# The line `from typing import Union` is importing the `Union` type hint from the `typing` module.

"""
hardware_names: int = "AlienWare"

Output:
Type_Hint.py:26: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
Found 1 error in 1 file (checked 1 source file)
"""


# `Union` type hint allows you to specify that a variable can have multiple possible types.
# In this case, it is used to specify that the `hardware_names` variable can be either an `int` or a `str`.


# Solution
hardware_names: Union[int, str] = "AlienWare"
"""
Success: no issues found in 1 source file
"""
number_list: List[Union[int, float]] = [1, 2, 3.14]
# Success: no issues found in 1 source file

# Problem of "second alternative"
# code --> data : int|float = 2090
# Alternatives syntax for unions requires Python 3.10 or newer

# Solution
# Use from __future__ import annotations act as time travel
"""
    from __future__ import annotations
    data: int | float = 300
"""
print("------------------------------------------------------------")


# Use General Type Hints
from typing import Optional

# The line `a: Optional[int] = 123` is declaring a variable `a` with the type hint `Optional[int]`.
# The `Optional` type hint indicates that the variable can either be of type `int` or `None` similar to Union[int, None].
# In this case, the variable `a` is assigned the value `123`, which is of type `int`.


# Scenario 1
def greet(name: Optional[str]) -> str:
    if name is None:
        return "Hello, stranger!"
    else:
        return f"Hello, {name}!"


print(greet("Alice"))
print(greet(None))


from typing import Any

def process_data(data: Any) -> None:
    # Example function that can handle any type of data
    # but won't have type checking during static analysis
    pass


print("------------------------------------------------------------")


# Type Hints for Functions
def add_numbers(x: int, y: int) -> int:
    return x + y


print(add_numbers(1, 2))

# Scenario 1
"""The line `from typing import Callable` is importing the `Callable` type hint from the `typing` module.
# This allows us to use the `Callable` type hint to indicate that a variable is a callable
object, such as a function/methods.
"""

from typing import Callable

message_Function = Callable[[str, str], str]

def apply_message(message: message_Function, a: str) -> str:
    return message(a, "Goodbye!")

def receive_message(call: str, another_call: str) -> str:
    return call + " " + another_call


message_appear = apply_message(receive_message, "Hello")
print("Message arrival: ", message_appear)
print("------------------------------------------------------------")


# Alias of Type Hints
from typing_extensions import TypeAlias

PostsType: TypeAlias = dict[int, str]

new_posts: PostsType = {1: "Python", 2: "C++", 3: "C"}
print(f"New posts are {new_posts}")

print("------------------------------------------------------------")


# Type Hints for a Class
from typing_extensions import Self


class Shape:
    def set_scale(self, scale: float) -> Self:
        self.scale = scale
        return self


s = Shape()
print(s.set_scale(0.5))
print("------------------------------------------------------------")


# Provide Literals for a Variable
from typing import Literal

shirt_size: Literal["Small", "Medium", "Large"]

weekends = "Medium"  # valid
weekends = "Extra Large"  # not valid

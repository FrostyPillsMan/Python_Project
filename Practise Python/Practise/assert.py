"""Assert

----------------
What is Assert?
--> "Built-in keyword to proactively perform sanity checks to ensure conditions are met. Program will raise error if conditions not spot-on and shown the error to the user.

--> "Commonly used in Debugging and Testing"

-----------------
When to Use?
1. Check if a variable has the correct data type
2. Check if a number is within a certain range
3. Check if  an input matrix has the correct dimensions for a neural network
4. Check if a list, set, or dictionary has a specific element

-----------------
Mistakes To Avoid
1. Using non-debugging tools for debugging.
Exp:
    --> Using "if statements and try/except clauses to perform sanity checks."

2. Using assert statements for non-debugging purposes
Exp:
    --> Assert statements meant for debugging and testing
    --> Error handling meant for try/except clauses

-----------------
Extra Resources
https://geekpython.in/python-assert#:~:text=The%20__debug__%20is,by%20modifying%20the%20PYTHONOPTIMIZE%20variable

"""


"""Scenario1 --> perform sanity check on user data"""


def start_program(data: dict):
    assert isinstance(data, dict), "Invalid JSON"
    assert data, "No data found...."
    pass

    print("loaded successfully!!")


if __name__ == "__main__":
    json_data = {"User": 1213}  # User data
    start_program(data=json_data)
    print(__debug__)
    # Set to True by default

print("##################################################################")

"""Scenario2 --> perform sanity check on """


class Shopping:
    def __init__(self, product, prices):
        self.product = product
        self.price = prices

    def list(self):
        if __debug__:
            if not self.price > 0:
                raise AssertionError("Price should not be 0 or Negative.")
        data = f"{self.product} is worth MYR{self.price}"
        return data

# Equivalent to
# assert self.price > 0, "Price Should not be 0 or Negative."


item_1 = Shopping("Perfume", 250)
print(item_1.list())

item_2 = Shopping("Shampoo", -35)
print(item_2.list())





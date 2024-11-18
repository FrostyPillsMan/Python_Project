from typing import Any

class Car:
    r"""
    A simple class to represent a car.
    """
    ...

    def __init__(self, brand: str, engine: str, year: int) -> None:
        r"""Initialize the car class with the received arguments

        Args:
            brand (str): the car's brand (i.e. BMW, Kia etc.)
            engine (str): it can be dieser or something else
            year (int): the manufacture year of the car
        """
        ...

print(Car.__doc__)


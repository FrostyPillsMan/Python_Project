import dataclasses 
from collections import defaultdict
import itertools

@dataclasses.dataclass(frozen=True)
class Student:
    name: str
    height: int

students = [
    Student(name="Adam", height=170),
    Student(name="Meow", height=180),
    Student(name="Emma", height=190),
    Student(name="Jim", height=195)
]

tallest_student = max(students, key=lambda x: x.height).name
print(tallest_student)

print("------------------------------------------------------------")

stock_prices = [
    ("AAPL", 234.62), ("Yahoo", 105.74), ("AMZN", 435.23),
    ("GOOGL", 1234.56),("Microsoft", 920.94)
]

stock_price = defaultdict(list)
for code, price in stock_prices:
    stock_price[code].append(price)

print("------------------------------------------------------------")

above_170_students = list(itertools.dropwhile(lambda s: s.height<170, students))
print(above_170_students)








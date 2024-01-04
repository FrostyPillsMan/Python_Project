# refactoring code

import time

def calculate_grade(score):
    time.sleep(1)
    if score >=80 : return "A"
    if score >=60 : return "B"
    if score >=40 : return "C"
    if score >=20 : return "D"
    return "F"

calc = calculate_grade(50)
print(calc)
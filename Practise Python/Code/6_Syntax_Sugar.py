from datetime import datetime


us_city = {"New York City": "USA", "Los Angeles City": "LA"}
eu_city = {"London": "UK", "Paris": "FR"}
as_city = {"Malaysia": "MY"}

print("Scenario_1")

# option 1
cities = us_city | eu_city | as_city
print(cities)

# option 2
us_city |= eu_city | as_city
print(us_city)

print("\n")

print("Scenario_2")

today_date = datetime.today()
print(f"Today's date : {today_date}")

# Shortcut on getting today's date
print(f"Today's date : {datetime.now()}")

print("\n")

print("Scenario_3")


def write(code):
    pass


# "Ellipsis" instead of "pass"
def create_game(): 
    ...


class Game_Developer:
    def __init__(self, age, expert): 
        ...


print("\n")

print("Scenario_4")

billionaire = ["Elon Musk", "Warren Buffet", "Jeff Bezos", "Bill Gates"]
billionaire.sort(key=lambda x: len(x))
# ascending order based on total length of name
print(billionaire)

print("\n")

print("Scenario_5")

# Walrus Operator
while (line := input("Press button(stop/start)")) != "stop":
    print(line)
else:
    print("Bravo!!!")

print("\n")

print("Scenario_6")

# Continuous Comparison similar to C/Java

a = 21

if 3 < a < 10:
    print(True)
elif a > 10 < 20:
    print(False)
else:
    print(None)


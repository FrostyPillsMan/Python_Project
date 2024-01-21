"""class House:
    house_prices = 100.29
    
    def __init__(self, living_room):
        self.living_room = living_room
"""
print("------------------------------------------------------------")

class Record:
    adam = {
        "name": "Muhammad Adam",
        "position": "Boss",
        "field": "Finance",
        "asset": 100_00_000,
        "is_manager": False,
    }


adam = Record()

for field, value in Record.adam.items():
    setattr(adam, field, value)

print(adam.__dict__)

change_name = adam.__dict__["name"] = "John Wick"
print("New Name:", change_name)




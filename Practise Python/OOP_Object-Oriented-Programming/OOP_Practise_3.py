class Shop:
    shirt_prices = 12.99

    def __init__(self, tag, colour) -> None:
        self.tag = tag
        self.colour = colour
        self.shirt = Shop.shirt_prices
        Shop.shirt_prices += 3.99


s1 = Shop("Shirt", "Black")
print(s1.shirt)  # 12.99

print(s1.__dict__)
print(s1.__dict__["shirt"])  # 12.99
shirt_display = s1.__dict__["shirt"] = "Shirt", "Red"
print(shirt_display)  # ('Shirt', 'Red')


s2 = Shop("Shirt_1", "White")
print(s2.shirt)  # 16.98

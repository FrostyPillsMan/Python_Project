class Car:
    pass


class Bugatti(Car):
    def __init__(self, model, color):
        self.model = model
        self.color = color


class Mclaren(Car):
    def __init__(self, model, color):
        self.model = model
        self.color = color


class Porsche(Car):
    def __init__(self, model, color):
        self.model = model
        self.color = color


def check_car_type(car_class):
    if issubclass(car_class, Car):
        return f"{car_class} is a Car."
    else:
        return f"{car_class} is not a Car."


# Creating instance for car types
car_validate = check_car_type(Car)
bugatti_car = Bugatti("Bugatti Divo", "Red")
mclaren_car = Mclaren("Mclaren 720S", "Orange")
porsche_car = Porsche("Porsche Macan S", "White")
bottle = check_car_type(int)


print(car_validate)
print(bugatti_car)
print(mclaren_car)
print(porsche_car)
print(bottle)



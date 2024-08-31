print("__repr__ Vs __str__")

class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Defines how str(person) behaves
    def __str__(self):
        return f"Character(name={self.name} age={self.age})"
    
    # Defines how repr(person) behaves
    def __repr__(self):
        return f"Character({repr(self.name)}, {repr(self.age)})"
        
movie_character = Character("Thomas Shelby", 32)

"""
str --> makes things readable to humans/users in general
repr --> makes things readable to developers/programmers
"""

print(str(movie_character))
print(repr(movie_character))
print("\n")

print("Binary Magic Methods")

class Person:
    def __init__(self, name):
        self.name = name

    def __or__(self, other):
        return f"{self.name} | {other}"
    
    def __and__(self, other):
        return f"{self.name} & {other}"
    
    def __xor__(self, other):
        return f"{self.name} ^ {other}"
    
    def __lshift__(self, other):
        return f"{self.name} << {other}"
    
    def __rshift__(self, other):
        return f"{self.name} >> {other}"
    
    def __invert__(self, other):
        return f"~{self.name}"

person = Person("Adam")

print(person | 4)
print(person & 5)
print(person ^ 6)
print(person << 76)
print(person >> 54)
print(person.__str__)
print("\n")

print("super().__init__")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def info(self):
        l, w = self.length, self.width
        print(f"area={l*w} perimeter={2*(l+w)}")

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        # Calling __init__ method from the Rectangle Class
        # Avoid rewrite entire __init__ and reuse its parent class '__init__' method

shape_1 = Rectangle(10, 7)
shape_1.info()

shape_2 = Square(7)
shape_2.info()

print("\n")

print("__getattr__ Vs __getattribute__")

class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    # always run
    # def __getattribute__(self, key):
        # return key

    # only runs if attribute does not exist
    def __getattr__(self, key):
        return key
    
car = Car("Porsche 911", "Gt3 Rs")

print(f"Car: {car.name}")
print(f"Car: {car.model}")
print(f"Car: {car.test}")
print(f"Car: {car.run}")

print("\n")

print("Stopping users from accessing __dict__")

class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    @property
    def __dict__(self):
        return {}
    

movie = Movie("Deadpool & Wolverine", "Shawn Levy", 2024)
print(movie.__dict__)
print(movie.title, movie.director, movie.year)


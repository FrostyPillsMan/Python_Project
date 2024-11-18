class Dad:
    def __init__(self):
        self.eye_color = "black"
        self.hair_color = "black"
        self.city = "Malaysia"

    def swim(self):
        print("I love swimming in the sea")

class Mum:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "black"
        self.city = "Ho Chi Minh City"

    def dance(self):
        print("I can dance")

class Kid(Dad, Mum):
    def __init__(self):
        Mum.__init__(self)


print(Kid.__mro__)

kid = Kid()
print(kid.eye_color)
print(kid.city)
kid.swim()
kid.dance()


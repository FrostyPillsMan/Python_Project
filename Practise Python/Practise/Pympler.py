from pympler import asizeof


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class SavePoint:
    __slots__ = ("a", "b")

    def __init__(self, a, b):
        self.a = a
        self.b = b


point = asizeof.asizeof(Point(10, 20))
print(point)

point = asizeof.asizeof(SavePoint(10, 20))
print(point)


point.z = 16
print(point.z)
# AttributeError: 'int' object has no attribute 'z'

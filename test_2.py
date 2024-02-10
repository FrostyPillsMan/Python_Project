# Non-data Descriptor

import time


class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]


class DeepThought:
    @LazyProperty
    def meaning_of_life(self):
        time.sleep(3)
        return f"Life is an adventure-journey."


my_deep_thought_instance = DeepThought()
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)


"""
https://realpython.com/python-descriptors/#why-use-python-descriptors
https://mathspp.com/blog/pydonts/describing-descriptors#:~:text=Descriptors%2C%20like%20properties%2C%20let%20you,%2C%20setter%2C%20and%20deleter%20methods.
"""



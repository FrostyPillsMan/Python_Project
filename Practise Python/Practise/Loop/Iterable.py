import time

numbers = [10, 12, 15, 18, 20]
fruits = ("apple", "pineapple", "blueberry")
message = "I love Python ❤️"

# Element access using integer indices
print(numbers[0])
print(fruits[2])
print(message[-2])

# Element access using while loop on Sequences-Object
index = 0
numbers = [1, 2, 3, 4, 5]
while index < len(numbers):
    print(numbers[index])
    index += 1

# Element access using Iterator method
values = [10, 20, 30]
iterator = iter(values)
print(next(iterator))
print(next(iterator))
print(next(iterator))

generator1 = (time.sleep(x) for x in range(3))
generator = iter(generator1)
print(next(generator))

def sleep():
    for x in range(3):
        yield time.sleep(x)

generator2 = iter(sleep())
print(next(generator2))


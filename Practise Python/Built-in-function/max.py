# Iterable vs Positional

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
unknown = []

print(f"Maximum number is {max(number)}")
print(max(unknown, default=100))

print("-----------------------------------------------------------------")

# String comparison

animals = ["dog", "cat", "shark"]

print(max(animals))  # shark
print(ord("d"))  # 100
print(ord("c"))  # 99
print(ord("s"))  # 115

print("-----------------------------------------------------------------")

# Keyword arguments

print(max("A", "W", key=str.upper))
print(max("Bandara Kinrara", "Bukit Puchong", key=len))



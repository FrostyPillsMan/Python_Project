a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
# equal(true)

print(id(a), id(b))
# not same identity due to different memory address
print(a is b)
# false

# Checking both have same value and memory addresses
c = [1, 2, 3]
d = c
print(id(c), id(d))

print(c is d)
print(c == d)

# All Identical variables are equal but not all Equal variables are identical




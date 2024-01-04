name = "Adam"
name_1 = "Adam"
print(id(name), id(name_1))

""" 
**Note** 
Caching Can Work Only With Immutable Objects

"""

a = [1, 2, 3]
b = [2, 4, 6]
print(f"a == {id(a)}, b == {id(b)}")

# 2089292625200 2089292625200
# a == 2089292624896, b == 2089292651456




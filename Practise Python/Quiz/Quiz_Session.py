# Getting value of y
x, y, z = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)[2::3]
print(x, y, z)

# Result of a
a = {1, 2, 3} & {4, 5, 6}
print(a)

# Remove value of "milk" inside s
s = {"milk", "cheese", "butter", "buttermilk"}
"""
s.difference_update(["milk"])
s.discard("milk")
s -={"milk"}
s &= {"cheese", "butter", "buttermilk"}

print(s)
"""

# Access list by abstract value of "t"
list = [1, ["a", "b", ["kill", "bat", "cup"], "c"], 3]
print(list[1][2][1][2])

# List Comprehensions method on printing asterisk("*") values
nums = [[val for val in range(num)] for num in range(3)]
for num in nums:
    for val in num:
        if val < 2:
            print("*", end="")

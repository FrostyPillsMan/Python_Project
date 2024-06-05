"""
__Summary__
Closure 
- function which remembers values in its enclosing scope.

(enclosing scope)
- smaller boxes inside a toy box where you keep specific variables.
- You can access and change these variables from within the smaller boxes, 
but you need to use the "nonlocal keyword" to modify variables in the outer scopes.

Rules of Closure
1. There are nested functions
2. The inner function must use variables defined in its outer function
3. The outer function must return the inner function
"""


text = "Distinguish Closures From Nested Functions"
print("\u0332".join(text))

def outer_func():
    leader = "Muhammad Adam Tan"

    def print_leader():
        print(f"Big Boss: {leader}")

    return print_leader()
    # Return the result!

f = outer_func()
# del outer_func

print(type(f))
# No closures occur

# f()
# Muhammad Adam Tan

print("-----------------------------------")
print("Know How to Get the Enclosed Values")

def leader_names():
    leader = "Muhammad Adam Tan"

    def print_leader():
        print(leader)

    return print_leader

f = leader_names()
print(leader_names.__closure__)
# None

print(f.__closure__)
# (<cell at 0x0000020E081D7820: str object at 0x0000020E08203170>,)

# print(f.__closure__[0].cell_contents)

print("-----------------------------------")
print("Implement a Bug-Free Closure")

"""__Problem__"""
def nums_generator():
    funcs = []
    for i in range(3):
        def f():
            return i * 2
        funcs.append(f)
    return funcs

f1, f2, f3 = nums_generator()
print(f"1. {f1()}, 2. {f2()}, 3. {f3()}")
print(f1.__closure__[0].cell_contents)
print(f2.__closure__[0].cell_contents)
print(f3.__closure__[0].cell_contents)

print("-----------------------------------")

def funcs_generator():
    funcs = []
    for i in range(3):
        def f(j = i):
            return j * 2
        funcs.append(f)
    return funcs

f1, f2, f3 = funcs_generator()
print(f"1. {f1()}, 2. {f2()}, 3. {f3()}")
print(f1.__closure__)
print(f2.__closure__)
print(f3.__closure__)

print("-----------------------------------")
print("Use Closures Skillfully")

def names():
    leader = "Jeff Bezos"
    return lambda _: print(leader)

display_names = names()
print(names.__closure__)

print(display_names.__closure__)

# print(display_names.__closure__[0].cell_contents)


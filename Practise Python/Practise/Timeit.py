import timeit
"""
benchmarking and comparing execution times between traditional codes and optimized codes
"""
import profile

# Function 1: Using list comprehension
def func1():
    return [i for i in range(1000)]

# Function 2: Using append method
def func2():
    result = []
    for i in range(1000):
        result.append(i)
    return result


# Measure the execution time of each function
time1 = timeit.timeit(func1, number=1000)
time2 = timeit.timeit(func2, number=1000)

print("Execution time for func1:", time1, "seconds")
print("Execution time for func2:", time2, "seconds")

if time1 < time2:
    print("func1 is faster.")
else:
    print("func2 is faster.")


"""
Problem
TypeError: 'module' object is not callable
------------------------------------------
Solution
Avoid naming the file name similar to module package 
exp. `timeit.py(file)` & `timeit(module)`
"""

print("#"*55)

def do_1():
    list_object = []
    for i in range(100):
        list_object.append(i)

def do():
    [i for i in range(100)]


t = timeit.Timer(setup="from __main__ import do_1", stmt="do_1()")
print(t.timeit())
t = timeit.Timer(setup="from __main__ import do", stmt="do()")
print(t.timeit())

print("#"*55)

# Option 1
"""def sort_names():
    names = ["Adam", "Hariz", "Condom"]
    new_names = []
    for i in names:
        new_names.append(i[::-1])
        return new_names"""

# Option 2
def upp_char(s):
    return s.upper()

def sort_names():
    names = ["Adam", "Hariz", "Condom"]
    map(upp_char, names)


t1 = timeit.Timer(setup="from __main__ import sort_names", stmt="sort_names()")
print(t1.timeit())

print("#"*55)

def fruit():
    fruits_lst = ["apple", "banana", "orange"]
    return ["banana", "apple" in fruits_lst]

def fruit_2():
    fruits_lst = {"apple", "banana", "orange"}
    return {"apple", "banana" in fruits_lst}


t2 = timeit.Timer(setup="from __main__ import fruit", stmt="fruit()")
print(f"Fruit: {t2.timeit()}")

t2 = timeit.Timer(setup="from __main__ import fruit_2", stmt="fruit_2()")
print(f"Fruit_2: {t2.timeit()}")

profile.run("fruit()")


import timeit


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

x = [7, 8, 9, 4, 5, 6, 7, 6, 8, 5, 5]

most = max(set(x), key=x.count)
# The set will remove duplicates, 
# and the key will count from original x, 
# not the set(x).

print(most)


def multiply(x, y):
    try:
        result = x*y
    except ZeroDivisionError:
        print("No number")
    else:
        print("result is ", result)
    finally:
        print("executing operations")
        

answer = multiply(1, 3)
print(answer)

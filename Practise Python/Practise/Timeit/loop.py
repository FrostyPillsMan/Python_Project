import timeit

def whileLoop(n=10000000):
    i = 0
    while i < n:
        i += 1
    return i


def forLoop(n=10000000):
    s = 0
    for i in range(n):
        s += i
    return s


def testLoops():
    print("while loop -->", timeit.timeit(whileLoop, number=1))
    print("for loop -->", timeit.timeit(forLoop, number=1))


if __name__ == "__main__":
    testLoops()



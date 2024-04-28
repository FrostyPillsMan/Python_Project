import multiprocessing
import time
import datetime

def yourfunction(x):
    start = datetime.datetime.now()
    time.sleep(1)
    end = datetime.datetime.now()
    return f"x={x} start at {start}, end at {end}"


if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        data = pool.map(yourfunction, [1, 2, 3, 4, 5, 6, 7])

    for row in data:
        print(row)


# Notes
# __name__ == "__main__" is a must for windows os
# Otherwise, it will runs the loop non-stop


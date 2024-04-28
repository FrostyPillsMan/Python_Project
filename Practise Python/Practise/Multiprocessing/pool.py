from multiprocessing import Pool


def do_something(number, another_number):
    return (number ** 2 + another_number ** 2)

arr_of_num_tuple = [(x, x + 1) for x  in range(0, 10000000)]
num_of_workers = 10

if __name__ == "__main__":
    with Pool(num_of_workers) as w:
        print(w.starmap(do_something, arr_of_num_tuple))


"""
Function
--------
map --> distributing the items across the available worker processes, so that each process executes a portion of the total tasks.
imap --> returns an iterator over the results as they become available.
Benefits:
Useful when dealing with substantial amounts of data
starmap --> similar to map function except requires two parameters for parallel execution.
"""


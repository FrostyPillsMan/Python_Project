import multiprocessing as mp

def my_function(item):
    # Perform some computation on the item
    result = item * 2
    return result

if __name__ == "__main__":
    # Create a pool of worker processes
    pool = mp.Pool(processes=4)

    # Define the iterable of items to process
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Apply the function to the iterable in parallel, using a chunksize of 2
    results = pool.map(my_function, items, chunksize=2)

    print(results)

# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

"""
Choosing an appropriate chunksize can help optimize performance 
by ensuring an even distribution of work across the worker processes.
"""


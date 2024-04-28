import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor
import concurrent.futures

# start the main process
start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping at {seconds} second(s)...")
    time.sleep(1)
    print("Done Sleeping")


# processes = []


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as exe:
        secs = [1, 2, 3, 4, 5, 6, 7]
        results = exe.map(do_something, secs)

        for result in results:
            print(f"List of Task: {result}")
    # for _ in range(10):
    # p = multiprocessing.Process(target=do_something, args=([1.5]))
    # p.start()
    # processes.append(p)

    # for process in processes:
    # process.join()

    # end the main process
    # finish = time.perf_counter()
    # print(f"Finished in {round(finish-start, 2)} seconds(s)")


"""
Problem
if __name__ == '__main__':
    freeze_support()
The "freeze_support()" line can be omitted if the program
is not going to be frozen to produce an executable.

Solution
if __name__ == "__main__"
"""


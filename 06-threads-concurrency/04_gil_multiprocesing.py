from multiprocessing import Process
import time


def crunch_number():
    print(f"Started the count process ...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Finished the count process ...")


if __name__ == "__main__":

    p1 = Process(target=crunch_number)
    p2 = Process(target=crunch_number)

    start_time = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end_time = time.time()

    print(f"Time elapsed while doing the work {(end_time - start_time):.2f} seconds")

# Unlike two threads in one process, two separate CPython processes
# can execute Python bytecode simultaneously on different CPU cores.

# Each process has its own interpreter and GIL. The operating system
# can schedule the processes on separate CPU cores.

from multiprocessing import Process
import time


def cpu_heavy_task(thread_name):
    print(f"Crunching some numbers in thread {thread_name} ...")
    total = 0
    for i in range(10**8):
        total += i
    print(f"Done in thread {thread_name} ✓")


if __name__ == "__main__":

    start_time = time.perf_counter()

    processes = [Process(target=cpu_heavy_task, args=(i + 1,)) for i in range(4)]

    [thread.start() for thread in processes]
    [thread.join() for thread in processes]

    end_time = time.perf_counter()

    print(f"{" - "*5} With Multiprocessing {" - "*5}")
    print(f"Task took a total of {(end_time - start_time):.4f} seconds.")

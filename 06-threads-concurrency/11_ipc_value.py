from multiprocessing import Process, Value


def increment(counter):
    for _ in range(100000):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    counter = Value("i", 0)

    processes = [Process(target=increment, args=(counter,)) for _ in range(4)]

    [p.start() for p in processes]
    [p.join() for p in processes]

    print(f"Final value of counter: {counter.value}")

# Notes:
# By using counter.get_lock(), only one process can enter
# that critical section at a time.

# The other processes wait until the lock is released.
# This prevents race conditions.

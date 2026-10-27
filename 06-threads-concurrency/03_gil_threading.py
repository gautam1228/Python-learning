import threading
import time

# Here, if two threads want access to the same part of memory
# GIL (Global Interpreter Lock) comes into picture,
# it's basically a single massive mutex

# In reality, the GIL is a massive bottleneck.
# Because of it, multiple Python threads can never execute
# Python code at the exact same time on multiple CPU cores.


def brew_drink():
    print(f"{threading.current_thread().name} started brewing ...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing ...")


thread1 = threading.Thread(target=brew_drink, name="Bartender-1")
thread2 = threading.Thread(target=brew_drink, name="Bartender-2")

start_time = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end_time = time.time()

print(f"Time elapsed while doing the work: {(end_time - start_time):.2f} seconds")

# Two threads take just as long (or slightly longer,
# due to context-switching overhead) as running the
# function twice sequentially.

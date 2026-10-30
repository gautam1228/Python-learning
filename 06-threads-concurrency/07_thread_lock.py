import threading

count = 0
lock = threading.Lock()


def churn():
    global count
    for _ in range(100000):
        with lock:
            count += 1


threads = [threading.Thread(target=churn) for _ in range(10)]

[thread.start() for thread in threads]
[thread.join() for thread in threads]

print(f"Counter: {count}")

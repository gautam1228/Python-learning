from multiprocessing import Process, Queue


def queue_data(queue: Queue):
    queue.put("This is dummy data")
    print(f"Data queued for processing")


if __name__ == "__main__":
    queue = Queue()

    process1 = Process(target=queue_data, args=(queue,))
    process1.start()
    process1.join()

    print(f"Data received from the queue: {queue.get()}")

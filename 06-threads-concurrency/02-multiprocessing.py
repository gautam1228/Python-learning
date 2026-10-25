from multiprocessing import Process
import time


def brew_drink(name):
    print(f"Start of {name} drink brewing")
    time.sleep(3)
    print(f"End of {name} drink brewing")


if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_drink, args=(f"Drink maker #{i+1}",)) for i in range(3)
    ]

    # Starting all the processes
    for p in chai_makers:
        p.start()

    # wait for all to complete
    for p in chai_makers:
        p.join()

    print("Completed brewing of all drinks.")

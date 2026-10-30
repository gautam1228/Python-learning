import threading
import time


def boil_egg(wait_time: int):
    print(f"Starting egg boiling ...")
    time.sleep(wait_time)
    print(f"Finished egg boiling ...")


def make_toast(wait_time: int):
    print(f"Starting toasting egg ...")
    time.sleep(wait_time)
    print(f"Finished toasting egg ...")


start_time = time.time()

boil_egg_thread = threading.Thread(target=boil_egg, args=(10,))
make_toast_thread = threading.Thread(target=make_toast, args=(7,))

boil_egg_thread.start()
make_toast_thread.start()

boil_egg_thread.join()
make_toast_thread.join()

end_time = time.time()

print(
    f"{"-"*5} Finished cooking breakfast in {(end_time - start_time):.2f} seconds. {"-"*5}"
)

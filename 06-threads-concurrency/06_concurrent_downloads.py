import threading
import time
import requests


def download_asset(url: str):
    print(f"Starting download from: {url}")
    resp = requests.get(url)
    print(f"Finished downloading from : {url} and received {len(resp.content)} bytes")


def get_images(urls: list[str]):
    threads = []
    for url in urls:
        t = threading.Thread(target=download_asset, args=(url,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == "__main__":

    urls = [
        "https://httpbin.org/image/jpeg",
        "https://httpbin.org/image/png",
        "https://httpbin.org/image/svg",
    ]

    start_time = time.perf_counter()
    get_images(urls)
    end_time = time.perf_counter()

    print(f"Downloading all images took {(end_time - start_time):.6f} seconds")

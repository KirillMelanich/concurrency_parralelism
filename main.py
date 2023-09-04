import time

import httpx


URL = "https://www.google.com/"


def send_request(num: int, url: str):
    print(f'Sending request #{num}')
    response = httpx.get(url)
    print(response.status_code)


def main_sync():
    for i in range(10):
        send_request(i, URL)


if __name__ == '__main__':
    start = time.perf_counter()
    main_sync()

    end = time.perf_counter()

    print("Elapsed:", end - start)


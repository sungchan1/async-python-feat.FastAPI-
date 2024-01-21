from concurrent.futures import ThreadPoolExecutor
import time
import os
import threading
import requests

def fetcher(params):
    session = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://google.com", "https://apple.com"] * 50
    executor = ThreadPoolExecutor(max_workers=10)
    # async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
    #     result = await asyncio.gather(*[fetcher(session, url) for url in urls])
    #     print(result)
    with requests.Session() as session:
        params = [(session, url) for url in urls]
        results = list(executor.map(fetcher, params))
        print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 8.3

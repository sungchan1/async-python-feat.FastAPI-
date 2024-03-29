# https://docs.aiohttp.org/en/stable/
# pip install aiohttp~=3.7.3
import asyncio
import time
import aiohttp


async def fetcher(session, url: str):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10
    async with aiohttp.ClientSession(connector=aiohttp.TCPConne ctor(ssl=False)) as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print("time : ", end - start)

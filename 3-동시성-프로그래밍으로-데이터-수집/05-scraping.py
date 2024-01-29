from bs4 import BeautifulSoup
import aiohttp
import asyncio
from config import get_secret
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# pip install beautifulsoup4

"""
웹 크롤링 : 검색 엔진의 구축 등을 위하여 특정한 방법으로 웹 페이지를 수집하는 프로그램
웹 스크래핑 : 웹에서 데이터를 수집하는 프로그램
"""



async def fetch(session, url):
    headers={
        "X-Naver-Client-Id": get_secret("NAVER_API_ID"),
        "X-Naver-Client-Secret":get_secret("NAVER_API_SECRET")

    }
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        items = result["items"]
        images = [ item['link'] for item in items]
        print(images)


async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    keyword="cat"

    urls = [f"{BASE_URL}?query={keyword}&display=20&start={i*20+1}" for i in range(1,10)]
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        await asyncio.gather(*[fetch(session, url) for url in urls])



if __name__ == "__main__":
    asyncio.run(main())



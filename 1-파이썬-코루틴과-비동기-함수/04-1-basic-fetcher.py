# https://2.python-requests.org/en/master/user/advanced/#id1
# pip install requests
import time

import requests



def fetcher(session: requests.Session, url: str):
    with session.get(url) as response:
        return response.text
def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10

    with requests.Session() as  session:
        result = [fetcher(session, url) for url in urls]
        print(result)






if __name__ =="__main__":
    start= time.time()
    main()
    end = time.time()
    print("time : ", end- start)

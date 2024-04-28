import requests

## .env 사용
import os
from dotenv import load_dotenv

load_dotenv()
## os.getenv("")

NAVER_CLIENT = os.getenv("NAVER_CLIENT")
NAVER_SECRET = os.getenv("NAVER_SECRET")

# 인수로 keyword, start, display를 받아 검색 url을 원하는대로 활용
def call_api(keyword, start, display):
    url = f'https://openapi.naver.com/v1/search/blog.json?query={keyword}&start={start}&display={display}'

    res = requests.get(url, headers={"X-Naver-Client-Id": NAVER_CLIENT,
                                    "X-Naver-Client-Secret": NAVER_SECRET})
    
    return res.json()

if __name__ == '__main__':
    res = call_api("교대역 병원", 1, 100)
    ## 최대 100건씩만 가져올 수 있기 때문에 그 이상을 가져오고 싶다면 여러 건 호출 해야 한다.
    ## e.g.
    # res = call_api("교대역 병원", 101, 100)
    ## 위의 방식을 효율적으로 개선하기 위해 get_paging_call을 구현하자.
    
    for item in res['items']:
        print(item)
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

def get_paging_call(keyword, quantity):
    if quantity > 1100:
        # quantity = 1100
        exit("[ERROR] 최대 요청 가능 횟수는 1100건입니다.")
    ## 1000 - 총 10번
    # // : 몫 구하는 연산
    repeat = quantity // 100
    result = []
    for i in range(repeat):
        start = i * 100 + 1
        ## 100개씩 10번이 최대 가능 횟수이므로 start > 1000이 넘어갈 경우 start를 1000으로 초기화
        if start > 1000:
            start = 1000
        print(f'{i + 1}번 반복 합니다. start: {start}')
        res = call_api(keyword, start, 100)
        result += res['items']
    return result


if __name__ == '__main__':
    res = get_paging_call("교대역 병원", 1100)
    print(res)
    print(len(res))
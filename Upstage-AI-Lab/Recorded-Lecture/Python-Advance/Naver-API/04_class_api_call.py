import requests

## .env 사용
import os
from dotenv import load_dotenv

load_dotenv()
## os.getenv("")

NAVER_CLIENT = os.getenv("NAVER_CLIENT")
NAVER_SECRET = os.getenv("NAVER_SECRET")

class NaverSeachAPI():
    api_url = f"https://openapi.naver.com/v1/search/blog.json"

    def call_api(self, keyword, start=1, display=10):
        url = f'{self.api_url}?query={keyword}&start={start}&display={display}'

        res = requests.get(url, headers={"X-Naver-Client-Id": NAVER_CLIENT,
                                        "X-Naver-Client-Secret": NAVER_SECRET})
        
        return res.json()
    
    def get_paging_call(self, keyword, quantity):
        if quantity > 1100:
            # quantity = 1100
            exit("[ERROR] 최대 요청 가능 횟수는 1100건입니다.")
        ## 1000 - 총 10번
        # // : 몫 구하는 연산
        repeat = quantity // 100

        display = 100
        if quantity < 100:
            display = quantity
            repeat = 1

        result = []
        for i in range(repeat):
            start = i * 100 + 1
            ## 100개씩 10번이 최대 가능 횟수이므로 start > 1000이 넘어갈 경우 start를 1000으로 초기화
            if start > 1000:
                start = 1000
            print(f'{i + 1}번 반복 합니다. start: {start}')
            res = self.call_api(keyword, start=start, display=display)
            result += res['items']
        return result
    
    def blog(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/blog.json"
        return self.get_paging_call(keyword, quantity)
    
    def news(self, keyword):
        self.api_url = "https://openapi.naver.com/v1/search/news.json"
        return self.call_api(keyword)

    def webkr(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/webkr.json"
        return self.get_paging_call(keyword, quantity)

if __name__ == '__main__':
    naver_search_api = NaverSeachAPI()
    res_blog = naver_search_api.blog("교대역", 100)
    res_news = naver_search_api.news("교대역")
    res_blog = naver_search_api.webkr("교대역", 20)
    print(res_blog)
    print(len(res_blog))
    print("*" * 20)
    print(res_news)
    print(len(res_news))
    print("*" * 20)
    print(res_news)
    print(len(res_news))
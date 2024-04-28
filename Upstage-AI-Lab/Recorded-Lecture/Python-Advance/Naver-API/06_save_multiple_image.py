## https://developers.naver.com/docs/serviceapi/search/image/image.md#%EC%9D%B4%EB%AF%B8%EC%A7%80

import requests

## .env 사용
import os.path
from dotenv import load_dotenv

## 이미지 저장
from urllib.request import Request, urlopen
import os

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

            print("total:", res['total'])
        return result
    
    def save_images(self, path, res):
        # path 디렉토리가 없다면 생성
        if not os.path.exists(path):
            os.mkdir(path)

        cnt = 0
        for img in res:
            try:
                image_url = img['link']
                image_byte = Request(image_url, headers={"User-Agent": "Mozilla/5.0"})
                file = open(f'{path}/{cnt}.jpg', 'wb')
                file.write(urlopen(image_byte).read())
                file.close()
            ## 에러 처리
            except Exception as e:
                print(e)
            cnt += 1
    
    def image(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/image"
        return self.get_paging_call(keyword, quantity)

if __name__ == '__main__':
    naver_search_api = NaverSeachAPI()
    keyword = "교대역"
    res_image = naver_search_api.image(keyword, 3)
    print(len(res_image))
    naver_search_api.save_images(keyword, res_image)
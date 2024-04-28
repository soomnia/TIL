import requests

## .env 사용
import os
from dotenv import load_dotenv

load_dotenv()
## os.getenv("")

NAVER_CLIENT = os.getenv("NAVER_CLIENT")
NAVER_SECRET = os.getenv("NAVER_SECRET")

## query=?
### 검색어. UTF-8로 인코딩되어야 합니다.
url = 'https://openapi.naver.com/v1/search/blog.json?query=교대역 맛집&start=1&display=33'

## GET
# res = requests.get(url)

## 인증 실패
# {"errorMessage":"Not Exist Client ID : Authentication failed. (인증에 실패했습니다.)","errorCode":"024"}

## secret 사용하여 인증
res = requests.get(url, headers={"X-Naver-Client-Id": NAVER_CLIENT,
                                 "X-Naver-Client-Secret": NAVER_SECRET})

## 파이썬의 dictionary -> json
# print(res.json())

##
json_data = res.json()

# print(json_data['total'])
# print(json_data['items'])

## url query에 display=? 추가
### 한 번에 표시할 검색 결과 개수(기본값: 10, 최댓값: 100)
print(len(json_data['items']))

## url query에 start=? 추가
### 검색 시작 위치(기본값: 1, 최댓값: 1000)

for item in json_data['items']:
    print(item)

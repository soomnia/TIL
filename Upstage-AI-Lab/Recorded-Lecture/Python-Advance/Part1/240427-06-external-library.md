# 파이썬 라이브러리를 활용한 기초 프로젝트
> 외부 라이브러리 다루기

## pip 사용
- 설치 <br>
`pip install 패키지명`

- 삭제 <br>
`pip uninstall 패키지명`

- 특정 버전으로 설치 <br>
`pip install 패키지명==버전`

- 패키지 버전 업그레이드 <br>
`pip install --upgrade 패키지명`

- 설치된 패키지 확인 <br>
`pip list`

- 패키지 리스트 **파일**로 저장 ⭐️⭐️⭐️ <br>
**`pip list --format=freeze > requirements.txt`**

- 패키지 리스트 설치 <br>
`pip install -r requirements.txt`
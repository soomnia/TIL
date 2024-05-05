# NOTE: - 30+ 개국어 단어 학습 프로젝트 (https://github.com/Kyubyong/wordvectors)

from gensim.models import Word2Vec

# 모델 불러오기
model = Word2Vec.load('./ko/ko.bin')

print("불러온 모델:\n", model)

# 유사한 단어 검색
print("'뉴스'와 유사한 단어 검색:\n", model.wv.most_similar("뉴스"))

# 유사도 검색
print("자동차와 고양이 유사도 검색:\n", model.wv.similarity('자동차', '고양이'))

# 유사도 검색
print("자동차와 버스 유사도 검색:\n", model.wv.similarity('자동차', '버스'))

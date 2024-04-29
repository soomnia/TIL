
# 파이썬 가상환경 구축하기
**[문제 상황]**<br>
* 녹화 강의 TIL/Upstage-AI-Lab/Recorded-Lecture/Python-Advance/01-News-Summary/240427-04-gensim-Word2Vec.py 을 vscode에서 학습 중
* 파이썬 venv 모듈을 통해 만든 가상 환경에 gensim 3.7.3 을 설치하였으나 아래와 같은 오류가 발생
```bash
Traceback (most recent call last):
  ...
    from gensim.models import Word2Vec
  File ".../.venv/lib/python3.11/site-packages/gensim/__init__.py", line 5, in <module>
    from gensim import parsing, corpora, matutils, interfaces, models, similarities, summarization, utils  # noqa:F401
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".../.venv/lib/python3.11/site-packages/gensim/corpora/__init__.py", line 6, in <module>
    from .indexedcorpus import IndexedCorpus  # noqa:F401 must appear before the other classes
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".../.venv/lib/python3.11/site-packages/gensim/corpora/indexedcorpus.py", line 15, in <module>
    from gensim import interfaces, utils
  File ".../.venv/lib/python3.11/site-packages/gensim/interfaces.py", line 21, in <module>
    from gensim import utils, matutils
  File ".../.venv/lib/python3.11/site-packages/gensim/matutils.py", line 24, in <module>
    from scipy.linalg.special_matrices import triu
ImportError: cannot import name 'triu' from 'scipy.linalg.special_matrices' (.../.venv/lib/python3.11/site-packages/scipy/linalg/special_matrices.py)
```
에러 메시지 정황 상, 내가 사용 중인 파이썬 버전(3.11.*) 때문에 <i>**패키지간 의존성 문제**</i>가 생긴 것 아닐까 싶었다. <br>
그래서 단순히(?) gensim을 3.7.3 버전을 설치하는 걸로 끝!이 아니라, python 버전도 적정 버전(현재의 경우 downgrade)이어야 하지 않을까? 생각이 들었다. <br>
그래서 생각한 해결 방안은
1. python 버전을 낮추어 설치하기 --> 이 경우 [pyenv](https://github.com/pyenv/pyenv)를 통해 버전 관리를 하는 것이 좋을 듯
2. python 버전을 원하는 버전으로 가상 환경을 구축할 수 있는지?<br>
    a. **아나콘다**<br>
    b. python venv 모듈

찾아보니 아나콘다로 가상환경을 구축하는 방법이 제일 간단해보여서 기록을 남긴다.
<hr>

## 1. [Anaconda로 구축하기](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#setting-environment-variables)

### STEP 1. 가상 환경 만들기
```bash
conda create -y -n venv_name
```
* `-y` : proceed 질문에 yes로 답변
* `-n` : name

venv_name은 원하는 이름으로 설정!

#### 가상 환경 리스트 조회하기
```bash
conda env list
```
```bash
# conda environments:
#
base                     /opt/anaconda3
venv_name             *  /opt/anaconda3/envs/venv_name

```

### STEP 2. 가상 환경 활성화
```bash
conda activate venv_name
```

```bash
## 프롬프트 앞에 설정한 venv_name으로 변경된 것 확인 가능
(venv_name) soom@soomui-MacBookPro ~ % 
```

### STEP 3. 원하는 버전의 python 설치
```bash
conda install python=3.8.10
```
#### 참고!
[맥OS m1 기준]기본 채널(default)에서는 3.8.10을 설치할 수 없어서<br>
`conda-forge` 채널을 추가해주어야 했다.
```bash
conda config --add channels conda-forge
```
conda-forge 채널에도 3.7.7 버전은 없길래 3.8.10을 설치했는데 해당 버전으로 gensim 사용에 문제 없었다.

잘 설치되었는지 확인 차원에서 python 버전 체크 한 번 해보자
```bash
python -V
```
```bash
Python 3.8.10
```

### STEP 4. pip install
원하는 라이브러리 설치하자. <br>

```bash
pip install gensim==3.7.3
```

3.11 버전대에서 실행 시 오류가 났던 파일을 실행하는데 문제가 없었다 🎉

혹시나 내가 venv 모듈을 사용함에 있어 문제가 있던 것일까.... 싶어서 아나콘다 가상 환경을 몇 개 더 구축해보았는데, 3.9 버전대부터 gensim==3.7.3 을 설치할 때부터 오류가 나는 것을 확인할 수 있었다 🫤

```bash
Collecting gensim==3.7.3
  Using cached gensim-3.7.3.tar.gz (23.4 MB)
  Preparing metadata (setup.py) ... done
Collecting numpy>=1.11.3 (from gensim==3.7.3)
  Using cached numpy-1.26.4-cp39-cp39-macosx_11_0_arm64.whl.metadata (61 kB)
Collecting scipy>=0.18.1 (from gensim==3.7.3)
  Downloading scipy-1.13.0-cp39-cp39-macosx_12_0_arm64.whl.metadata (60 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.6/60.6 kB 2.2 MB/s eta 0:0
     ## 잘 설치되는 듯 하다가....
Downloading wrapt-1.16.0-cp39-cp39-macosx_11_0_arm64.whl (38 kB)
Building wheels for collected packages: gensim
  Building wheel for gensim (setup.py) ... error
  error: subprocess-exited-with-error
  
  × python setup.py bdist_wheel did not run successfully.
  │ exit code: 1
  ╰─> [42 lines of output]
    ## gensim을 사용하기 위해 의존성이 있는 타 라이브러리 설치가 실패하면서...🤡
      [end of output]
  
note: This error originates from a subprocess, and is likely not a problem with pip.
ERROR: Failed cleaning build dir for gensim
Failed to build gensim
ERROR: Could not build wheels for gensim, which is required to install pyproject.toml-based projects
## 최종적으로 설치 실패...!!
```

그래서 내가 venv 모듈을 잘못 사용했다기 보다는... 파이썬 버전으로 인한 이슈였다고 보는 것이 타당한 듯

더 자세하게 확인하려면 gensim 문서를 확인해야겠지만... ~~(사실 처음부터 그랬어야 했지만...)~~

코드 문제보다 이런 류의 문제가 더 골치 아프다 정말로...😇
그래도 결국 원인을 파악(?)해서 뿌듯하긴 하다~

### STEP 5. 가상 환경 비활성화
```bash
conda deactivate
```

```bash
## 프롬프트 앞에 다시 base로 돌아온 것 확인 가능
(base) soom@soomui-MacBookPro ~ %
```

### STEP 6. 가상 환경 삭제
```bash
conda env remove -n venv_name
```



<hr>

## 2. 파이썬 venv 모듈로 구축하기
TODO:
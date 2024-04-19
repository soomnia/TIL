# 리눅스 운영 파트
> 리눅스 쉘과 CLI 명령어 | 기본 명령어 다루기 1, 2


## list
```bash
ls

# long
# 상세 설명
ls -l

# all
ls -a

# 조합해서 사용도 가능
ls -al
ls -a -l

# 특정 확장자 검색
ls *.csv
```
<hr>

## touch
본래 기능: 파일의 수정 시각을 현재 timestamp로 바꾸기

해당 파일이 존재하지 않을 경우, 0 byte 파일이 만들어지는 것을 이용해 파일 생성에도 사용

```bash
touch hello.txt

# hidden file --> -a 로 조회해야 함
touch .hello.txt
```
<hr>

## cat
concatenate: 연쇄시키다 - 연결하다

파일 내용 보는 것에서 그치는 것이 아니라, input(파일) - output(standard out)을 연결함

```bash
# 줄의 맨 뒤에 $ 붙이기 --> 히든 공백을 확인할 수 있음
cat -e hello.txt

# 줄 라인 번호 확인
cat -n hello.txt
```
<hr>

## more
파일 내용 보기

cat처럼 전체 출력이 한번에 되는 것이 아니라<br>
페이지 단위로 스페이스/엔터 키로 이동할 수 있게 현재 터미널의 크기에 맞추어 내용을 출력한다.<br>하지만 뒤로 넘어갈 수만 있고, 앞에 지나간 부분은 볼 수 없다
```bash
more hello.txt
```
<hr>

## less
more의 단점을 개선했다.<br>
<del>개발자들의 고오급 유우머 ㅋ</del> <br>
모든 파일 내용을 메모리에 올리지 않고 보여지는 만큼 분할해서 메모리에 올리므로 속도도 more보다 빠름

* 스페이스: 페이지 단위 이동
* 엔터: 줄 단위 이동
* 방향키: 상하좌우, 페이지 업다운
```bash
less hello.txt
```

<hr>

## rm
remove<br>파일 삭제
```bash
rm hello.txt
```

<hr>

## mkdir
make directory<br>디렉토리 생성

```bash
mkdir dir
mkdir dir/sub
```
### parents 옵션
중간에 존재하지 않는 디렉토리가 있어도 생성할 수 있게 됨

```bash
% mkdir dir/sub
mkdir: dir: No such file or directory
```

```bash
mkdir -p dir2/sub1
```


<hr>

## 디렉토리 삭제
### rmdir
remove directory<br>
#### parents 옵션
자식 디렉토리와 그 부모 디렉토리를 모두 삭제

```bash
## dir의 자식인 sub만 삭제된다
rmdir dir/sub

mkdir -p dir/sub

## 부모인 dir도 함께 삭제된다
rmdir -p dir/sub
```

### rm -r
recursive<br>
rm으로는 디렉토리를 삭제할 수 없지만, `-r` 옵션을 함께 쓰면 하위 디렉토리/파일을 모두 (순환적으로) 지운다<br>

```bash
rm -r dir
```

<hr>

## tree
디렉토리 계층 구조 확인 가능, 별도의 설치가 필요하다.
```bash
# tree 설치
brew install tree

tree
```

<hr>

## cd
change directory<br>
디렉토리 이동

```bash
cd dir/
# . 나 자신
# .. 부모 디렉토리
cd ..
# ~ 홈
cd
cd ~
cd ~/
# - 이전 디렉토리
cd -
```

<hr>

## cp
copy<br>
복사

```bash
cp hello.txt hell.txt
# 동일한 파일명이 존재할 경우 덮어쓰기 되므로 주의!!

# test1을 디렉토리(sub) 안으로 복사
cp test1 sub

# 디렉토리 복제 -r
# 디렉토리 하위 파일들까지 복제됨
cp -r sub sub_c
```

<hr>

## mv
move<br>
이동할 때 사용<br>
rename의 역할을 대신 수행할 수 있기에 대체로 파일명, 디렉토리명을 변경 시 mv를 사용한다.

```bash
% ls
hello.txt
% mv hello.txt hello2.txt
% ls
hello2.txt
```

<hr>

## ln
link<br>
파일 링크

### 소프트/심볼릭 링크
'바로가기' 느낌

```bash
ln -s hello.txt hellosymlink
```

### 하드 링크
```bash
ln hello.txt hellolink
```
### 파일 링크 확인
#### 파일의 inode 확인
```bash
ls -ali
```
* 파일명은 파일의 내용이 아닌, 해당 파일의 위치를 가리키는 포인터 역할<br>
* 하드 링크는 같은 파일을 가리키는 또다른 포인터를 생성하는 것<br>
즉, 파일이 두 개가 생긴 것이 아니고 하나의 파일을 가리키기 때문에 디스크 용량에 변화가 없다.<br>
두 개의 파일 포인터가 하나의 inode를 가리키는 것이고, 이 inode가 실제 데이터값을 가리키는 주소값을 보유함. 그래서 원본/사본의 개념이 아니다.<br>
* 심볼릭 링크는 심볼릭 링크는 또다른 inode를 생성하고 이 inode가 실제 파일 데이터를 가리키는 포인터를 가리키는 포인터로 작용한다

### inode
리눅스 환경에서 파일을 관리하는 구조체<br>
다양한 파일의 속성값을 관리한다. (권한, 사이즈, 수정시간 ...)

```mermaid
flowchart LR;
    txt("hello.txt") --> inode("inode(실제 파일 데이터를 가리키는 주소값 보유)");
    hardlink("하드 링크") --> inode;
    inode --> data("실제 데이터");
```
```mermaid
flowchart LR;
    symlink("심볼릭 링크") --> inode2("inode2");
    inode2 --> txt("hello.txt") --> inode1("inode1");
    inode1 --> data("실제 데이터");
```

```bash
% ln -s hello.txt hellosymlink
% ln hello.txt hellolink
% ls
hello.txt	hellolink	hellosymlink
% ls -ali
total 0
5076795 drwxr-xr-x  5 soom  staff  160  4 18 11:48 .
5076794 drwxr-xr-x  4 soom  staff  128  4 18 11:38 ..
## 같은 inode를 가진 것을 확인할 수 있다.
5077387 -rw-r--r--  2 soom  staff    0  4 18 11:44 hello.txt
5077387 -rw-r--r--  2 soom  staff    0  4 18 11:44 hellolink
## 다른 inode를 가진 것을 확인할 수 있다.
5077544 lrwxr-xr-x  1 soom  staff    9  4 18 11:48 hellosymlink -> hello.txt
```

<hr>

## file
파일 속성 확인
```bash
file hello.txt
```

```bash
% file hello.txt 
hello.txt: empty

# 내용 작성
% nano hello.txt

% file hello.txt 
hello.txt: ASCII text
% file hellolink 
hellolink: ASCII text
% file hellosymlink 
hellosymlink: ASCII text

```

<hr>

## 시스템 종료
```bash
## 재부팅
## sudo 권한이 있을 경우 경고 메시지/재확인 없이 바로 재부팅
reboot

## sudo 권한이 있을 경우 경고 메시지/재확인 없이 바로 시스템 종료
poweroff

# option 과 함께 사용 가능
# 옵션 없이 할 경우 1분 후 종료
shutdown
# 1분 이내 종료를 취소하고 싶다면
shutdown -c
## 바로 종료
shutdown -P now
## 바로 재시작
shut -r now
```
<hr>

## man
manual<br>
도움말

```bash
# man에 대한 매뉴얼 확인 가능
man man

# 페이지 지정 - printf에 대한 매뉴얼 3페이지
man 3 printf

# 정규표현식 사용하여 검색
man -k ^printf
# man quit
q
```

## 파일 편집기 - vi, vim, nano
* vi --> vim(vi-improved)<br>
🍯 vimtutor: vi 학습기

* nano<br>
vi, vim보다 사용이 편한 간결한 편집기

```bash
echo "aaa" > hello.txt
```

```bash
nano hello.txt
```
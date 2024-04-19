# 리눅스 운영 파트
> 리눅스 쉘과 CLI 명령어 | BASH 쉘과 친숙해지기

## 쉘
OS와 통신을 하기 위한 사용자의 유저 프로세스<br>
사용자 명령어 및 프로그램을 실행할 수 있는 공간 | 사용자 인터페이스

사용자의 입력 > [시스템 콜 인터페이스] > 커널에 전달

## shell 종류

Bourne shell 계열은 $ 프롬프트 사용

C shell 계열은 % 프롬프트 사용

Bourne shell > <b>B</b>ourne <b>A</b>gain <b>SH</b>ell (bash)

```bash
# 설치된 shell을 확인할 수 있다
cat /etc/shells
```

### 프롬프트
명령 대기 중임을 보여주는 명령 대기 표시자 ($ | %)

설정은 환경 변수 PS1 에 기록됨(Prompt Statement One)

```bash
echo $PS1
```

```bash
% echo $PS1
%n@%m %1~ %#
```

<hr>

## 기본 CMD

### 출력

```bash
# 출력
echo
```
* `-n` 뉴 라인 제외
* `-e` escape 코드 지원
* `-E` 디폴트, escape 코드 미지원

<hr>

### 리다이렉션
출력 결과물을 다른 장치로 보냄 (output, append, error, merge)

\> >> 2> 2>&
#### 출력 장치 유형
* 장치 번호 1 - 표준 출력 - stdout
* 장치 번호 2 - 에러 출력 - stderr

```bash
# 출력
# 파일로 출력 - hello를 화면에 출력하면서 그 결과를 hello.txt 로 저장
echo "hello" > hello.txt
# 기존 파일을 덮어씀
echo "hello world" > hello.txt

# 기존 파일에 누적
echo "hello again" >> hello.txt

# ls로 조회한 출력 결과물을 file.txt 로 저장
ls > file.txt
# 존재하지 않는 cmd 사용 시, 정상적인 내용은 없으므로 아무런 내용도 기록되지 않음
aaa > file.txt

# 에러 메시지를 출력하고 싶다면, 표준 출력(stdout)이 아닌 stderr(2번)을 사용해야 함. 
## 실패한 에러 메시지를 file.txt 로 저장
aaa 2> file.txt

# 표준 출력과 에러 출력을 같은 파일에 저장하고 싶다면
# 복합적으로 리다이렉션 사용
## /tmp/* 를 조회한 결과를 result.txt로 저장하고 에러 출력을 1번(표준 출력)과 같은 곳에 저장
ls /tmp/* > reulst.txt 2>&1
## 위를 간단히 표현하자면
ls /tmp/* &> result.txt
```

### 입력
* 장치 번호 0 - 입력 장치 - stdin <br>
< <<

```bash
# 표준 입력
echo < hello.txt

cat
# 엔터 키, 종료 시엔 ctrl+D

# Delimeter <<
# 표준 입력으로부터 end 값이 들어올 때까지 입력 (end는 예시임! 다른 단어 써도 됨!)
cat << end

cat << end > hello.txt
# 표준 입력으로 end가 들어올 때까지의 입력 결과를 hello.txt에 저장
```

### 파이프 |
출력값을 프로세스간 전달할 때 사용

```bash
# 파이프 |
# ls -l 출력값 내에서 hello 검색
ls -l | grep hello

# ls -l 출력값 줄 개수 확인
ls -l | wc -l

# 다중 사용 가능
ls -l | grep hello | wc -l

# 출력값 내에서 페이징
cat hello.txt | more
```

<hr>

### history
최근 내역을 $HISTSIZE 만큼 확인할 수 있음. 파일로도 저장 가능하다!

```bash
# 명령어 history
## 저장 개수 확인
echo $HISTSIZE

# 쉴 종료 시 파일에 기록 가능한 사이즈
echo $HISTFILESIZE

# 최근 10개 내역 확인 옵션
history -10

# 히스토리 버퍼 삭제(clear) 옵션
history -c

# 히스토리로 조회한 내역을 실행
## 15번쨰 라인 다시 실행
!15
## 바로 이전 명령어 다시 실행
!!
```

<hr>

## 환경변수 - PATH

어떠한 기능을 수행하기 위해서는 사전 조건들을 어딘가에 저장해두어야 그것을 불러와 사용할 수 있다.

그것이 저장되는 곳이 환경변수!

ls라는 명령어를 쳤을 때

1. 해당 바이너리가 저장된 디렉토리 확인

    이때 하드 디스크 전체를 검색하면 시간이 오래 걸리니, PATH를 중심으로 위치를 검색함
2. 검색됐다면, 실행 권한 확인
    
    SetUID (??) 확인
3. 입력한 사용자 id로 명령어 실행

    해당 명령어의 소유주 권한으로 명령어 실행

동일한 이름의 바이너리가 두 곳 이상에 존재할 경우, PATH에 기록된 순서대로 실행됨


> <img src="https://cdn.oaistatic.com/_next/static/media/apple-touch-icon.59f2e898.png" alt="chatGPT" width="16px" />
> setuid 또는 set user ID는 UNIX 및 UNIX 계열 운영 체제에서 사용되는 보안 기능 중 하나입니다. <br> 이 기능은 실행 파일에 특정 사용자의 사용자 ID(UID)를 설정하여 해당 파일이 해당 사용자의 권한으로 실행되도록 합니다.<br>
> 일반적으로 이러한 기능은 특정 프로그램이 특권(예: root 권한)이 필요한 작업을 수행해야 할 때 사용됩니다. 예를 들어, 파일이 root 사용자의 UID로 설정되어 있으면 해당 파일이 실행될 때 root 권한으로 실행됩니다. <br>
> setuid는 보안 문제를 일으킬 수 있으므로 신중하게 사용해야 합니다. 특히, setuid가 설정된 파일은 보안 취약점으로 이어질 수 있으므로 최소한의 필요성만을 가진 경우에만 사용해야 합니다. 이러한 파일은 권한을 최소한으로 제한하여 실행되어야 하며, 보안 검토를 통해 가능한 모든 취약점이 확인되고 보완되어야 합니다.

<hr>

### which
내가 실행하려는 바이너리가 어디에 저장되어있는지 확인할 수 있다.

```bash
# which - PATH 검색 시 참고
which python
```

<hr>

### env
환경변수 확인 시 사용

```bash
# env와 동일하다
printenv

# 환경변수 설정 > 해당 터미널에만 적용됨
kitty=cat

# 특정 환경변수 확인
echo $kitty

# 전체 적용 -> export + bashrc 파일에 저장하여 영구 반영
export kitty=cat

# 언어 및 언어셋 확인
echo $LANGUAGE
echo $LANG

# 언어 한시적으로 변경
LANGUAGE=kor ls -l

# 영구적으로 변경
export LANGUAGE=kor
```

```bash
# 환경변수 - 지역 설정값 확인 로케일
locale
localectl

# 설정 가능한 모든 로케일 정보 확인
locale -a
```

<hr>

### alias 설정
bash의 장점 중 하나로, 단축 명령어를 사용할 수 있다.

```bash
ls
# 아래 내용을 단축한 것이다.
ls --color=auto

# alias 를 설정해서 쓸 수 있다
alias ..="cd .."
```

<hr>

## 쉘 시작 시퀀스
.profile .bashrc 시작될 때, 종료될 때 시퀀스가 있다. <br>

1. /etc/profile 수행 - 공통 수행 - 환경 설정
2. /etc/profile.d/*.sh 공통 수행
3. /etc/bash.bashrc 공통 수행 - 시스템 alias
4. ~/.profile 수행 - 사용자별 디렉토리 - 시작 프로그램 등
5. ~/.bashrc 수행 - 사용자별 디렉토리 - alias 등
6. ~/.bash_aliases —> 파일이 있다면 추가적으로 수행

## 쉘 스크립트 작성 실행 방식

1. /bin/sh 또는 /bin/bash 를 통해 실행
    
    ```bash
    bash test.sh
    ```
    
2. 실행 퍼미션을 허용 후 직접 실행
    
    ```bash
    chmod +x test.sh
    ./test.sh
    ```
    
### shebang #!
shabang, hashbang<br>
스크립트 언어로 작성된 파일이 실행 가능한 상태로 되게끔 해주는 특별한 주석
```bash
#!/bin/bash
```
```bash
#!/usr/bin/perl
```
```bash
#!/usr/bin/python
```    
위의 shebang을 무시하고 실행하고 싶다면 `-m` 옵션을 사용하면 됨!

```bash
bash -m test.sh
```

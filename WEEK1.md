# 1주차 Python이랑 친해지기

    대부분의 인원이 windows를 쓰고 있는 관계로 windows 환경에서 Python 개발환경을 갖추는 방법에 대해 다루려고 합니다.

~~c9.io 로 개발환경 맞추려고 했으나... 모두에게 해외결제수단이 있는 것이 아니기 때문에...~~


## 왜 Python 인가?
* 초보자들이 접근하기 쉬움
* 지원하는 라이브러리가 방대함
    * 수학/공학용(Scipy, NumPy), 데이터사이언스, 웹개발(Flask) 등등

## 개발환경
* VS Code
* Python 3.6
* Git

### 외부 서비스
* Github(코드 리뷰 목적)
* Heroku(공짜 서버, 실서비스를 만든다는 느낌으로)

## 개발환경 세팅하는 것부터 

### Git 설치하기
https://git-scm.com/downloads 에서 Windows 버전을 다운로드 받고 설치합시다.

### VS Code 설치하기


### Python 설치하기



## Python 맛만 봅시다.

### 자료형

#### 정수형

#### 실수형
1.9999992, 3.3e+10, 3.14e-10

#### 불리언
`True`, `False` 대문자로 나타낸다는 점에서 유의
* cpp : true, false


* 논리연산자
    * cpp : ||(or), &&(and), !(not)
    * python : `or`, `and`, `not`
#### 컨테이너
* 리스트
* 튜플
    * 리스트와는 다르게 요소의 값을 변화시키지 못함
* 딕셔너리
    * 키-값 저장소


#### 파이썬을 배울 수 있는 사이트
* https://www.codecademy.com/courses/learn-python/



## Flask 동작 원리
1. 웹 브라우저, 모바일 앱(HTTP protocol)로 접속
2. 라우트 데코레이터를 통해서 접근하고자 하는 경로에 접근
3. 뷰 함수 호출
3-1. 요청(HTTP request)을 받아서 비즈니스 로직을 처리하고,
3-2. 처리한 결과를 반환
4. 요청을 보낸 쪽으로 응답(HTTP response)

## 여러분이 해야할 것(9/17까지)
* Python 문법 숙지
    * https://www.codecademy.com/courses/learn-python/
* 만들고 싶은 프로젝트(웹개발을 이용해서)를 결정
    * 스터디 진행하는 사람이 코드 리뷰해줌
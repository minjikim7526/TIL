# Django with Python

날짜: 2023년 3월 22일

# Django

- 파이썬 기반 다양한 라이브러리 활용 가능
- 배우기 쉽고 활용 범위가 넓음
- 관리자페이지를 기본으로 제공 - 현재 프로젝트의 디비 구조 파악을 할 수 있음
- 기본 보안 기능 설정되어 있음

## 기본 명령

### python manage.py 명령어

- django-admin startproject
    - 장고프로젝트를 만드는 명령. 웹 서비스를 만들 때마다 한 번 실행함.
- startapp
    - 앱을 새로 만들 때. (앱 : 프로젝트의 기능 단위)
- makemigrations
    - model의 변경 사항이 있을 때.
- migrate
    - 실제 변경 사항을 DB에 반영(선makemigrations, 후migrate)
    - **makemigrations는 장고가 테이블 작업을 수행하기 위한 파일들을 생성하고, 실제 테이블 생성은 migrate가 한다!!**
- runserver
    - 테스트 서버 실행
- sqlmigrate
    - 실행할 SQL명령문 출력. 어떤 명령문을 실행할지 확인할 때 사용, 튜닝이 안된 쿼리나 슬로우쿼리 여부 확인
- showmigrations
- dumpdata : 현재 DB 내용 백업
- loaddata : 백업파일에서 DB로 내용 복구
- flush
- shell
- dbshell
- createsuperuser : 관리자 계정 생성
- changepassword

---

### 가상환경

- 여러 버전, 패키지들을 격리된 환경에서 사용할 수 있도록 도와주는 도구
- **conda**, venv, virtualenv 등이 있음
- 아나콘다 가상환경을 사용하면, 여러 프로젝트를 효과적으로 관리할 수 있고, 프로젝트 간의 충돌을 최소화하여 개발환경을 보다 안정적이고 효율적으로 진행할 수 있음
- Django실습을 위해 mysite 가상환경을 만들었음
- `conda update -n base -c defaults conda` : 아나콘다 최신 버전 업데이트 자주 해줄 것
- **아나콘다 프롬프트에서 ctrl+C = 실행중단**

---

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### 포트번호(네트워크도 길이 있다)

- 네트워크로 통신할 때 포트번호를 각각 지정해두었음
- mysql : 3306
- 웹 : 8000, 8080
- oracle: 1533
- mariaDB : 3310

---

## MVC와 MTV(디자인패턴) - 개발자 면접 때 중요!

### MVC

- 웹 프로그래밍에서 자주 사용되는 디자인 패턴
- Model-View-Controller(DB-Frontend-java)

### MTV

- 장고 디자인 패턴
- Model-Template-View(DB-Python-Front)
- T : index.html

### models.py

- DB의 명세를 관리
- 모델은 클래스로 만드는데
- 클래스의 이름이 테이블의 이름이 되고
- 클래스의 속성들이 컬럼이 됨

### views.py

- 글쓰기, 글보기 등 페이지 하나하나 만들 때 사용
- 클래스, 함수 둘 다 가능

### urls.py

- 어떤 url을 이용해 어떤 view를 동작시킬 지를 결정
- views.py 작업 후 urls.py에도 반영해야 함!

### templates

- html이 들어있는 파일
- 특정 폴더 안에 템플릿 파일들을 모아두고 싶다면 파일 위치를 settings.py에 설정해둬야함

---

## Django개발환경

### config폴더

: 프로젝트 설정 파일과 웹 서비스 실행을 위한 파일들이 있음

- settings.py
- urls.py : 최초 기준 url 파일

---

manage.py : **명령어를 실행**하기 위한 파일(임의로 변경하지 말 것)

---

## [실습] 게시판노트 앱 만들기

### 1. 기능 추가를 위해 앱을 생성

- 기능 추가 후 url설정도 해야함
- config폴더-urls.py수정
- views.py작성

---

url만들고 - 기능 만들고 - 매칭 시켜준다 (반복)

---

### 2. URL분리

- 프로젝트 짜임새를 고려하여 URL 매핑 관리를 한다.

```python
# config/urls.py
from django.urls import path, **include**
~~~
urlpatterns = [
	path(~~),
	path('bbsnote/', **include('bbsnote.urls'**))

# bbsnote/urls.py
****from django.urls.import path
**from . import views

urlpatterns = [
	path('', views.index),
]
```

---

### 3. 게시판 모델 만들기

- 모델은 “클래스”로 구현해야함!(함수X)
- `class Board(models.Model):` : 괄호 안에 상속(models에 있는 Model로부터 상속받겠다)
- settings.py에 앞으로 내가 만든 모델 체크하라고 했음
    
    INSTALLED_APPS = [ 'bbsnote.apps.BbsnoteConfig']
    

---

class 안에서 이 인스턴스를 호출했을 때 기본적으로 보이고 싶은 값을 세팅함

```python
# 게시판 목록에서 제목만 보이게
class Board(models.Model):
	def __str__(self):
		return self.subject
```

```python
# 게시판 목록에서 '[아이디] 제목' 이렇게 보이게
def __str__(self):
	return f'[{self.id}]{self.subject}'
```

model.py을 수정했으면 명령어창에서 makemigrations - migrate - runserver

```python
(mysite) C:\Users\MINJI\Documents\mysite>python manage.py makemigrations
Migrations for 'bbsnote':
  bbsnote\migrations\0002_board_update_date_alter_board_create_date.py
    - Add field update_date to board
    - Alter field create_date on board
```
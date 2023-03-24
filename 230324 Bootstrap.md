# [게시판 실습]3 부트스트랩

날짜: 2023년 3월 24일

board와 comment가 외래키로 연결된 종속관계이기 때문에

board.comment_set.count

board.comment_set.all

이런 함수를 쓸 수 있는 것임

---

# 부트스트랩(Bootstrap)

- CSS를 편리하게 쓰기 위한 도구
- CSS 프레임워크의 한 종류 - Foundation, Skeleton 등
- **HTML태그에 bootstrap에서 제공하는 class 속성을 추가**하는 것만으로도 페이지를 바꿀 수 있음
- 반응형 웹을 지향하고 있기 때문에 유연하게 변화하는 UX/UI를 적용할 수 있음
- mysite - static - css 폴더 만들고 그 안에 [bootstrap으로 시작하는 .css 파일] 2개 저장함

config폴더-settings.py-[static url(정적 파일 설정)] 

```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static', # static파일이 여기 있으니 확인해라
]
```

board_list.html에서 위쪽에 추가

(static파일 로드하겠다. 이름은 bootstrap.min.css야)

```html
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap.min.css' %}">
```

---

html파일마다 위의 작업을 해줘야 하는가?

매번 하려면 너무 비효율적..

템플릿을 상속받을 수 있도록 하자!

공통으로 쓸 수 있는 레이아웃은 한 번만 정의하고 그 다음부터는 끌어다쓰자

## 장고의 템플릿 상속 기능 적용하기

- 기본 틀을 만들어 활용이 가능
- templates폴더 밑에 base.html 파일 만들고, **! 치고 엔터**하고 몇몇 추가하기
- 큰 틀을 만드는 작업!!

```html
{% load static %} # 맨 위에 이거 추가
<!DOCTYPE html>
<html lang="ko"> # 언어 변경
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap.min.css' %}">
# title 바로 밑에 link 이거 추가
</head>
<body>
    {% block content %} #body에 이거 추가
    {% endblock %}
</body>

</html>
```

### block content 사이에 들어갈 내용 추가하기

board_list.html 수정 - 구글드라이브의 board_list 1번.html 을 복사해서 붙여넣기

```html
# url만들기 전이라 맨 밑에만 이렇게 url없이 수정 **href=""**	
<a **href=""** class="btn btn-primary">등록</a> 
</div>
{% endblock %}
```

### 게시글 등록 기능 만들기

bbsnote/forms.py

장고모델폼을 만들때는 클래스 안에 클래스를 만들게 되어있음

```python
from django import forms
from bbsnote.models import Board

# forms.ModelForm을 상속받는 모델폼이므로 자동으로 완성되는...
class BoardForm(forms.ModelForm): 
    class Meta:
        model = Board
        fields = ['subject','content']
```

### 1. 모델폼

- forms.ModelForm을 상속받는 폼
- 모델과 연결된 폼
- 모델 폼 객체를 저장하면 연결된 모델의 데이터를 저장할 수 있음
- Meta클래스를 내부 클래스에 반드시 가져가야 함
- Meta클래스에 모델 폼이 사용할 모델과 모델의 필드를 작성해야 함

### 2. 폼

- forms.Form을 상속받는 폼
- 모델폼과 다르게 직접 필드를 정의하고, 위젯 설정을 해줘야 함

---

bbsnote/urls.py에서 path추가

bbsnote/views.py 에 def board_create 추가

```python
from .forms import BoardForm # 맨위에 추가

def board_create():# 맨 아래에 추가
# 실행은 시키되 커밋은 하지마라(문제생기면 복구하려고)
```

mysql은 오토커밋이라서 commit=false : 오토커밋 하지마

오라클?

insert하게 되면, 

insert into Board()

values();

실행시키면

---

board_form.html 파일 만들기

---

더 꾸미고 싶으면

- forms.py meta 밑에 widgets, labes 속성 추가하면 forms.html의 {{forms.as_p}}을 통해 빠르게 템플릿 만들어져서 편하게 꾸밀 수 있음(장점)
- 하지만, HTML코드가 자동으로 생성되기 때문에 디자인적인 측면에서 많은 제한이 생기게 됨. 특정 태그를 추가하거나 필요한 클래스를 추가하는 것이 자유롭지 못하고, 디자인 영역과 서버 프로그램이 영역이 혼재되는 상황이 발생하여 디자이너와 개발자 간 역할을 분리하기도 애매해지는 단점
- 따라서 폼을 이용하여 자동으로 HTML코드를 생성하지 않고, 직접 HTML코드를 작성하는 방법을 사용하기위해 **forms.html에서 label을 개별 설정**했음(관리포인트를 옮기는 개념)
- board_form.html에 **{{form as.p}} 부분에 덮어쓰기**
    
    ```python
    <div class="form-group">
                <label for="subject">제목</label>
                <input type="text" class="form-control" name="subject" id="subject"
                       value="{{ form.subject.value|default_if_none:'' }}">
            </div>
            <div class="form-group">
                <label for="content">내용</label>
                <textarea class="form-control" name="content"
                          id="content" rows="10">{{ form.content.value|default_if_none:'' }}</textarea>
            </div>
    ```
    
- form.html에서 label을 개별 설정했으니까 forms.py에서 widgets이하를 주석처리(관리포인트를 옮기는 개념)
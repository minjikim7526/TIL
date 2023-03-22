# Web Front-End Programming

날짜: 2023년 3월 20일

HTML

CSS

Django : Python으로 웹을 실행하기 위한 도구

---

## Web Architecture

- World Wide Web
- HTTP 프로토콜
- Request/Response 기반
- URL/URI 주소 방식

## 웹 컨텐츠 - HTML+CSS+JavaScript

### 1. HTML(구조언어)

- 마크업, 시멘틱 정보, 컨텐츠 레이아웃
- 웹 페이지의 뼈대 역할

### 2. CSS(표현언어)

- 화면 디스플레이, 프레젠테이션
- 뼈대를 감싸는 피부역할

### 3. JavaScript(동작언어)

- 동작, 논리적제어, 사용자 상호작용
- HTML과 CSS를 움직이게 하는 근육

---

## 웹페이지 작성을 위한 언어 - HTML

- Hyper Text Markup Language
- Hypertext, 하이퍼텍스트
    - Index, 전화번호부, 사전
    - 링크를 클릭해 다른 문서나 사이트로 즉시 이동할 수 있는 기능
- Markup Language, 마크업언어
    - 문서에 특별한 “표시”를 통해 기능 표현
- 웹 표준
    - 웹 사이트를 만들 때 지켜야하는 약속들을 정리한 것
    - HTML5로 문서를 만드는 것이 웹 표준을 지킨 문서를 만드는 기본
    - 어느 기기에서나 볼 수 있도록 함
        - 디바이스의 크기가 달라질 때 화면이 적절하게 조절되는 것
- HTML5와 CSS3
    - 앱 화면 디자인하기 위한 기초가 됨
    - 웹 사이트와 블로그를 원하는 대로 수정할 수 있음
- 다른 언어와 마찬가지로, HTML도 텍스트 파일로 작성하여 파일로 저장

---

웹편집기로 VScode + Replit 사용 예정

## HTML 기본 문서 구조

### 태그(tag)

- 마크업 할 때 사용되는 약속된 표기법
- 웹 문서에 표시하려는 내용을 전달하는 언어
- 소문자로 씀
- 여는 태그<>와 닫는 태그</>를 정확히 입력
- 들여쓰기를 위해 tab키를 사용
- 태그는 속성과 함께 사용 가능(폰트를 크게, 작게 등)
- 포함 관계를 명확히 해야 함
- head : 문서 정보
- body : 실제 화면에 보이는 문서 내용

### 텍스트 태그

- `<p> ~~ </p>` : paragraph
- `<br>` : 엔터
- `<hr>` : 수평선
- `<strong> <b>`
- `<em>` : 특정 부분 강조하고 싶을 때 이탤릭체, 단순 이탤릭체는 `<i>`
- `<span>` : 일부 텍스트만 묶어 스타일 적용
- `<ul>, <li> `: 순서가 필요하지 않은 목록 만들기
    
    ```html
    <ul>
    	<li> ~~~ </li>
    	<li> ~~~ </li>
    </ul>
    ```
    
- `<ol>, <li>` : 순서**가 필요한 목록 만들기(1부터 순차적으로 순서가 붙음)
- `<dl>목록,<dt>제목,<dd>설명 표시` : 제목과 설명이 한 쌍인 설명 목록 만들기
- `<table>, <tr> 행, <td>셀, <th>제목 셀`, colspan 가로 셀 합침, rowspan 세로 셀 합침
- `<caption>` : `<table>` 다음에 사용. 표 위쪽 중앙에 제목 표시
- `<figcaption>` : 표 위에 쓰면 표 위에 제목 표시, 아래에 쓰면 표 아래 제목 표시
- `<a>` : 링크를 걸어줌
    - href : 주소 입력
        - `<a href=” “>`
    - target : 위치 지정
        - `<a target=”new”>` : 새 창 띄우기
    - download : 링크한 내용을 다운로드(보여주는 것이 아님)
    - rel : 현재 문서와 링크한 문서의 관계
    - hreflang : 링크한 문서의 언어 지정
    - type

### 폼 관련 태그

- `<form>` : 폼 태그. 사용자가 입력하는 칸
    - method속성
        - get방식 : 사용자가 입력한 내용이 주소표시줄에 그대로 드러남. 보안X
        - post방식 : 입력 내용 길이에 제한 없음. 사용자가 입력한 내용이 드러나지 않음. 보안O
- `<label>` : 폼 요소에 레이블 붙이기. 예) 입력 칸 옆에 “아이디” 텍스트
- `<fieldset>` : fieldset 태그 사이의 폼들을 하나의 영역으로 묶고
- `<legend>` : fieldset으로 묶은 영역에 테두리 그어줌. 제목을 붙여줌.

---

## 웹 문서의 디자인 요소를 담당하는 CSS

### CSS(Cascading Style Sheets)

- HTML로 뼈대를 작성하고, CSS로 디자인을 구성
- 스타일 형식
- 선택자 { 스타일속성 : 속성 값; }

```css
p{text-align : center;} 텍스트 단락을 중앙 정렬하겠다는 뜻
```

### 스타일시트

- 스타일 규칙들을 관리하기 쉽도록 한 군데에 묶어 놓은 것
- 내부스타일시트 : html문서 중 head 안에 작성
- 외부스타일시트 : .css 파일을 참조하도록 링크

### 선택자

- 전체선택자 * (=all): 스타일을 모든 요소에 적용할 때 사용
- 태그선택자 : 특정 태그가 쓰인 모든 요소에 적용
- 클래스선택자 : 지정된 클래스에 스타일 적용. 둘 이상도 가능
- id 선택자 # : 문서 안에서 한 번만 적용 가능
- 그룹 선택자 : 두 개 이상의 요소에 같은 스타일 적용

---

### 문단 관련

- `line-height` : 문단의 줄 간격을 조절
- `text-overflow`
    - `white-space` : nowrap으로 지정해서 줄바꿈하지 않을 경우 넘치는 텍스트를 처리하는 것!

---

### 블록 레벨 요소

- 태그를 사용해 컨텐츠를 추가했을 때 한 줄을 통째로 차지하는 요소
- 양 옆으로 다른 요소가 올 수 없음

### 인라인 레벨 요소

- 화면에 표시되는 컨텐츠만큼만 차지하고 한 줄을 차지하지 않는 요소

---

### CSS박스 모델 - 테두리 관련 속성

- border-style
    - none
    - hidden
    - dashed
    - dotted
    - double
    - solid

### CSS박스 모델 - 여백 관련 속성

- margin  : 현재 요소 주변의 여백
- padding : 콘텐츠 영역과 테두리 사이의 여백(테두리 안쪽)

---

### CSS3 연결 선택자

- **하위 선택자** : 부모 요소에 포함된 **하위 요소 모두에** 스타일이 적용되는 것
    - 상위요소**v**하위요소 { 스타일; }
        
        ```css
        section p {text-align : center; }
        container ul {border : 1px dotted blue; }
        container의 자식+손자 중 ul에 스타일 적용
        ```
        
- **자식선택자** : 부모 요소에 포함된 **자식 요소에만** 스타일이 적용되는 것
    - 부모요소 **>** 자식요소 { 스타일; }
        
        ```css
        section > p {text-align : center; }
        container > ul {border : 1px dotted blue; }
        자식요소에만 스타일 적용(손자요소에는 X)
        ```
        
- 인접 형제 선택자 : 문서 구조상 같은 부모를 가진 형제 요소 중 첫 번째 동생요소에 스타일이 적용
    - 형 + 첫째동생 { 스타일; }
        
        ```css
        h1 + ul {text-align : center; }
        ```
        
- 형제 선택자 : 인접 형제 선택자와 달리 모든 형제 요소에 적용
    - 형 ~ 동생 { 스타일; }
        
        ```css
        h1 ~ ul {text-align : center; }
        ```
        

---

## CSS3 속성 가상 클래스

### 가상 클래스(pseudo class)

: 웹 요소에 사용자가 클릭하거나 마우스를 올려놓는 등 특정 동작을 할 때 스타일 적용을 위해 사용

- :link
- :visited
- :hover
- :active
- :focus
- :enable와 :disabled
- :checked

---

## 반응형 웹

- 웹표준으로 사이트를 제작해서 ,디바이스의 크기에 상관없이 사이트의 레이아웃을 자연스럽게 바꾸어 보여주는 것
- 단점 : 유지보수가 힘들다

### 뷰포트

- 접속한 사용자에게 보여지는 화면 영역(실제 내용이 표시되는 영역)

### 미디어 쿼리

- 사이트에 접속하는 장치에 따라 특정한 CSS 스타일을 구분지어 적용될 수 있게 하는 CSS3 모듈
- 화면 회전
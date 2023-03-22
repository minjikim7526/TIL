# JavaScript기초

날짜: 2023년 3월 21일

## JavaScript

- Interpreter언어(파이썬과 동일)
    - 반대개념 : Compile언어
    - 프로그램을 한줄씩 번역해서 실행시키는 소프트웨어
- ECMAScript(코어언어)
    - 현재 ECMAScript2017작업이 진행중

### 클라이언트 측의 고유한 기술요소

- window인터페이스 : 자바스크립트로 브라우저 또는 창을 조작하는 기능 제공
- DOM : 자바스크립트로 **HTML문서의 요소를 제어**하는 기능 제공
- XMLHttpRequest : 서버와 **비동기**로 통신하는 기능 제공
    
    비동기 : 페이지가 동작하지 않는다.
    

### 서버 측 고유한 기술요소

- Node.js : 구글이 개발한 자바스크립트 실행 환경(자주 사용됨)
- Aptana Jaxer : 압타나사가 개발

---

## Javascript 기본 문법

### 자바스크립트 선언 - body or head 영역 안에 선언

```jsx
<script>
	alert("오늘의 명언입니다");
</script>
```

### 변수

- `var 변수명;` : 변수 선언. 변수 정의.
- `var 변수명 = 값;` : 변수의 할당

### 호이스팅(hoisting)

- 프로그램은 작성한 순서에 따라 차례대로 실행되지만, 프로그램 **중간에서 변수를 선언하더라도 첫머리에 선언된 것처럼** 생성되는 것을 말함. **변수 선언의 끌어올림**은 자바스크립트만의 고유한 특징. (단, 선언과 동시에 대입하는 코드는 끌어올리지 않음)

### 데이터 표현

- Java와는 다르게 변수에 데이터의 타입 지정을 하지 않음
- 변수에 값이 저장되는 순간, 변수의 데이터 타입이 결정됨
- 변수에 저장할 수 있는 데이터 타입으로는 문자형, 숫자형, 논리형, 그리고 빈데이터형이 있음
- `undefined`는 변수가 정의되었지만 값은 할당되지 않았을 때 사용
- `null` 는 값이 비어있을 경우 사용
    - undefined와 다르게 직접 할당해야함
    - `var name = null;`

---

### 출력

- alert : =화면에 경고창 띄우기
- console.log() : 개발자 도구에 변수의 값을 출력하는 역할
    - 실제 개발 환경에서 Debugging할 때 주로 사용
- document.write() : html문서내에 script태그를 만들고 javascript변수의 내용 출력

```html
<head>
	<script type=“text/javascript”>
		var helloMessage =“안녕하세요.”;
		document.write(helloMessage);
</script>
</head>
```

### 연산

- `A==B` : 같다
- `A!=B` : 같지 않다(다르다)
- `A===B` : 숫자와 “자료형”이 모두 같다
- `A!==B` : 숫자나 “자료형”이 다르다

---

### 선택문

- if ~~~;
- else if ~~~~;
- else ~~~~;

---

### 반복문

- for(반복값초기화; 조건식; 증감식)
- 중첩 for

---

## 객체

- 자바스크립트도 객체 기반 언어.
- 객체는 기능과 속성을 가지고 있음

### 객체의 종류

- 내장객체(=파이썬의 모듈)
    - 날짜정보객체 `var today = new Date();`
    - 수학객체
    - 배열(=파이썬의 리스트)
    - 문자열 객체
- 브라우저 객체 모델
    - document.write
- 문서 객체 모델(=DOM)
    - html의 문서 구조
    - 호환성 문제를 해결하기 위해 jQuery DOM을 많이 사용함

---

## 함수

---

### 객체 리터럴

- 자바스크립트에서는 원시타입을 제외한 모든 값이 객체
- 가장 기본적인 객체 생성 방법이 객체 리터럴임.

```jsx
var object = {};
object.name = "minji";
object.job = "developer";
console.log(object.name);
console.dir(object); 객체가 구성하고 있는 정보를 콘솔에 찍어줌
```

---

### jQuery

- 실무에서 많이 씀
- Node(=Element=태그들)를 간편하게 컨트롤하기 위한 라이브러리
- 여러 작업들을 편하게 만들어준다
    - html문서에서 element 찾기
    - html문서에서 content 변경하기
    - 사용자의 action에 반응하기
    - 웹 페이지의 내용을 애니메이션 하기
    - 네트워크에서 새로운 컨텐츠 받아오기(ajax)
- jQuery로 처리할 수 있는 element들의 기능들
    - css
    - event
    - animation
    - create
    - modify
    - delete
- html문서는 DOM(Document Object Model)의 집합
- 자바스크립트로 DOM들을 컨트롤하려면 길고 복잡하고, 브라우저마다 방법이 다름..
    - ~  jQuery 등장!
# CSS
---
## CSS이란
CSS는 마크업 언어(HTML)가 실제 표시되는 방법(색상, 크기, 폰트 등)을 지정하여
콘텐츠 구조를 꾸며주는 정적 언어로 웹의 시각적인 표현을 담당한다.

---
## CSS 특징
- 적당한 크기와 아름다운 색상, 원하는 위치를 지정하는데 집중할 수 있다.
- 선택자를 사용하여 원하는 작업을 할 수 있다.
- 다양한 방식으로 CSS를 적용할 수 있다.

---
## CSS의 문법
~~~
h1 { color: red }
~~~
h1, color, red 세 개의 단어가 있는데 각각 선택자, 속성, 값이라고 합니다.
- 선택자(selector) : 무엇을 꾸밀지 정합니다. h1은 h1 요소를 꾸미겠다는 뜻입니다.
- 속성(property) : 어떤 모양을 꾸밀지 정합니다. color는 색을 꾸미겠다는 뜻입니다.
- 값(value) : 어떻게 꾸밀지 정합니다. red는 빨간색으로 만들겠다는 뜻입니다.
즉, CSS 코드는 다음처럼 구성됩니다.
~~~
selector { property: value }
~~~
이때 property와 value를 합쳐서 선언(declaration)이라고 합니다.

---
#### 여러 개의 선언
세미콜론으로 구분하여 선언을 여러 개 넣을 수 있습니다.
~~~
h1 {
    color: red 
    font-size: 20px
}
~~~
h1 요소의 색을 빨간색으로 하고 글자 크기를 20px로 만들겠다는 뜻입니다. 마지막 선언에는 세미콜론을 붙여도 되고 붙이지 않아도 됩니다.
~~~
h1 {
  color: red;
  font-size: 20px
}
~~~

---
#### 값에 공백이 있는 경우
값(value)에 공백이 있다면 작은 따옴표 또는 큰 따옴표로 감쌉니다. 예를 들어 문단의 글꼴을 Times New Roman로 하고 싶다면
~~~
p {
  font-family: 'Times New Roman';
}
~~~
또는
~~~
p {
  font-family: "Times New Roman";
}
~~~
와 같이 합니다.

---
## CSS 선언 방식
---
#### 인라인 방식
HTML 요소의 style 속성에 직접 작성하는 방식
~~~
<body>
  <p style="height:100px; color:blue>
</body>
~~~
#### 내장 방식
HTML `<style></style>`안에 작성하는 방식
~~~
<head> 
  <style type="text/css"> 
    .logo {color: #eeeeee;} 
  </style> 
</head>
~~~
#### 링크 방식
HTML <link>를 이용하여 외부 문서로 CSS를 불러와 적용하는 방식
~~~
<head> 
  <link href="style.css" rel="stylesheet" type="text/css"> 
</head>
~~~
@import 방식
CSS @import를 이용하여 외부 문서로 CSS를 불러와 적용하는 방식
~~~
<head> 
  <style type="text/css"> 
    @import url(style.css); 
  </style> 
</head>
~~~

---
## CSS 선택자
---
#### HTML 요소 선택자
CSS를 적용할 대상으로 HTML 요소의 이름을 직접 사용하여 선택할 수 있다.
HTML
~~~ 
<h2>스타일 적용</h2>
~~~
CSS
~~~
h2 { color: teal; text-decoration: underline; }
~~~
####아이디 선택자
아이디 선택자는 CSS를 적용할 대상으로 특정 요소를 선택할 떄 사용합니다.
이때 #을 써서 구분해 줍니다.
HTML
~~~
<h2 id="heading">스타일 적용</h2>
~~~
CSS
~~~
 # heading { color: teal; text-decoration: line-through; }
~~~
**Tip**
<span style="color:#808080">
HTML과 CSS에서는 하나의 웹 페이지에 속하는 여러 요소에 같은 아이디 이름을 사용해도 별 문제없이 동작합니다. 하지만 이렇게 중복된 아이디를 가지고 자바스크립트 작업을 하게 되면 오류가 발생합니다. 따라서 되도록이면 하나의 웹 페이지에 속하는 요소에는 다른 아이디 이름을 사용하거나 클래스를 사용하는 것이 좋습니다.</span>
#### 클래스 선택자
클래스 선택자는 특정 집단의 여러 요소를 한 번에 선택할 때 사용합니다. 이런 특정 집단을 클래스라고 하며, 같은 클래스 이름을 가진 요소들을 모두 선택해 줍니다.
HTML
~~~
<h1>클래스 선택자를 이용한 선택</h1>

<h2 class="headings">이 부분에 스타일을 적용합니다.</h2>

<p>클래스 선택자를 이용하여 스타일을 적용할 HTML 요소들을 한 번에 선택할 수 있습니다.</p>

<h3 class="headings">이 부분에도 같은 스타일을 적용합니다.</h3>

<h3 class="headings headings2">이 부분에는 다른 스타일과 추가 스타일을 적용합니다.</h3>
~~~
CSS
~~~
.headings {
    color: lime;
    text-decoration: overline;
}
.headings2 { 
    color: blue; 
    font-size: 50px; 
}
~~~
#### 그룹 선택자
그룹 선택자는 여러 선택자를 같이 사용하고자 할 떄 사용합니다. 그룹 선택자는 여러 선택자를 쉼표로 구분하여 연결하고, 이런 그룹 선택자는 코드를 중복해서 작성하지 않도록 하여 코드를 간결하게 만들어 주는 역할을 합니다.
CSS
~~~
h1 { color: navy; }

h1, h2 { text-align: center; }

h1, h2, p { background-color: lightgray; }
~~~
####전체 선택자
전체 선택자는 *문자를 사용하여 요소 내부의 모든 요소를 선택합니다.
CSS
~~~
* { color: teal; text-decoration: underline; }

div * { color: teal; text-decoration: underline; }
~~~
---
## 주석
주석은 /*와 */사이에 씁니다.
~~~
/* 주석 */
~~~
/*와 */ 사이에 줄바꿈이 있어도 모두 주석으로 인식합니다.
~~~
/*
주석1
주석2
*/
~~~
여러 줄의 주석은 꾸미기도 합니다.
~~~
/*
* 주석1
* 주석2
* 주석3
*/
~~~

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
- html에서 하나하나 `<font>`로 감쌀 필요가 없어 코드가 간결해진다.
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
/*와*/ 사이에 작성된 문자를 주석으로 인식합니다.
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

---
## 속성
#### width,heigth 속성
width와 height 속성은 각각 가로 길이, 세로 길이를 의미합니다.

값을 정의 할때는 “100px” 처럼 숫자 뒤에 단위를 표시하여 작성합니다.

`<span>` 태그등 inline 요소는 적용 되지 않는데, 이는 display 속성에서 다시한번 다룹니다.

`#box{ width: 100px; height: 60px }`

#### margin, padding 속성
margin과 padding 속성은 각각 바깥쪽 여백, 안쪽 여백을 의미합니다.
이 속성도 숫자 뒤에 단위를 표시하여 작성합니다.

margin과 padding는 border 을 경계로 나뉩니다.

margin 뒤의 숫자에 따라 여백을 다르게 설정할 수 있다.
- margin:2px 전방향 모두 2px
- margin:1px 2px 상하 1px 
 좌우 2px
- margin:1px 2px 3px 상 1px 좌우 2px 하 3px
- margin:1px 2px 3px 4px 상 1px 좌 2px 하 3px 4px
위처럼 설정된다

`#box{ margin: 10px; padding: 20px }`

#### color 속성
color 속성은 단어 뜻대로 색상, 정확히는 글자의 색상을 의미합니다.

- red, blue등 이미 정의된 색
- #000, #FFFFFF 등의 16진수 색상 코드
- rgb(255, 255, 255) 등의 rgb 색상
- rgba(200, 100, 150, 0.5) 등의 알파(투명도)가 적용된 rgba 색상
color 속성은 위 목록등의 값을 사용할 수 있으며, 기본값은 inherit으로 부모의 색상을 가져옵니다.
`#text1 { color: red; }`
`#text2 { color: #0A0; }`
`#text3 { color: rgb(0, 0, 150); }`
`#text4 { color: rgba(30, 150, 100, 0.5); }`
#### font
font 속성은 글자의 폰트를 정의하는 속성인데, 여러 기능을 동시에 가지고 있는 속성이기도 합니다.

- font-style:이탤릭체 등의 글꼴의 스타일 지정
- font-weight:글자 두께
- font-variant:글꼴 변형 (소문자를 대문자로 바꾸는 등의)
- font-size:글자 크기
- line-height:줄 간격
- font-family:글꼴 (굴림, 돋움, …)

font-style
글꼴의 스타일로, 주로 이탤릭체를 설정하기 위해 사용합니다.

- normal: 기본
- italic: 이탤릭체

font-weight
글꼴의 두께로, 미리 정의된 단어나 100 ~ 900 사이의 숫자를 통해 설정합니다.
기본값은 normal 입니다.

- 100: lighter
- 400: normal
- 700: bold
- 900: bolder
font-size
글자 크기로, <font> 태그의 size 속성과 효과가 같습니다.
주석은 /*와 */사이에 씁니다.
font-family
글꼴 종류로, <font> 태그의 face 속성과 효과가 같습니다.
쉼표(,)로 여러 글꼴을 등록 할 수 있는데, 이때 맨 앞에 있는 글꼴을 우선으로 적용시키며, 맨 앞에 있는 글꼴이 사용자의 컴퓨터에 없을 때 그 다음 글꼴을 사용하게 됩니다.
~~~
.box1 {
	font-size: 20px;
	font-family: 나눔고딕,NanumGothic,돋움,Dotum;
}
.box1 .title { font-weight: bold }
.ex1 { font: 15px NanumGothic, sans-serif }
.ex2 { font: italic bold 12px/30px Dotum, sans-serif }
~~~
#### text-align 속성
text-align 속성은 텍스트의 정렬 방향을 의미합니다.

- left: 왼쪽 정렬
- right: 오른쪽 정렬
- center: 중앙 정렬
- justify: 양쪽 정렬 

`#box1 { text-align: right; }`
`#box2 { text-align: left; }`
`#box3 { text-align: center; }`

#### background 속성
background 속성은 태그의 배경을 지정하는 속성으로, font 속성과 비슷하게 세부적인 속성들을 한번에 쓸 수 있는 속성입니다.

- background-color:배경 색
- background-image:배경 이미지
- background-repeat:배경 이미지 반복 여부
- background-position:배경 이미지 위치

background-color
배경색을 의미하며, 값은 color 속성의 포맷을 사용합니다

background-image
배경 이미지를 설정하며, 주로 이미지 경로를 지정하는 방식으로 사용합니다.
경로는 background-image: url("이미지 경로") 처럼 작성합니다.

background-repeat
background-image로 컨테이너보다 작은 이미지를 적용하면 이미지가 반복되어 출력됩니다.
이때 background-repeat 속성을 사용하면 반복여부를 지정 할 수 있습니다.

background-position
일반적으로 background-image 는 왼쪽 위부터 이미지를 출력합니다.
background-position 속성을 사용하면 이미지의 좌표를 수정 할 수 있게 됩니다.

`#box{ background: #09C url('image.png') no-repeat 10px center; }`

####border 속성
border 속성은 태그의 테두리를 설정하는 속성으로, background 속성과 비슷하게 세부적인 속성들을 한번에 쓸 수 있는 속성입니다. width - style - color의 순서로 사용합니다.

border-width
테두리의 두께로, 주로 px 단위를 사용합니다.

border-style
테두리의 스타일로 실선, 점선, 이중선 등의 옵션이 존재합니다.

border-color
테두리의 색상으로, 값은 color 속성의 포맷을 사용합니다.
테두리의 특정 방향만 따로 설정할 수도 있습니다.

- border-top
- border-bottom
- border-left
- border-right

`#box{
	border: 4px dotted green;
	border-bottom: 5px solid blue;
}`
#### position 속성
position 속성은 태그를 어떻게 위치시킬지를 정의하며, 아래의 5가지 값을 갖습니다.

- static: 기본값, 다른 태그와의 관계에 의해 자동으로 배치되며 위치를 임의로 설정해 줄 수 없습니다.
- absolute: 절대 좌표와 함께 위치를 지정해 줄 수 있습니다.
- relative: 원래 있던 위치를 기준으로 좌표를 지정합니다.
- fixed: 스크롤과 상관없이 항상 문서 최 좌측상단을 기준으로 좌표를 고정합니다.
- inherit: 부모 태그의 속성값을 상속받습니다.
  
좌표를 지정 해주기 위해서는 left, right, top, bottom 속성과 함께 사용합니다.
`#box1 { position:static }`
`#box2 { position:absolute }`
`#box3 { position:relative }`
`#box4 { position:fixed }`
`#box5 { position:inherit }`

여기까지 css 정리 끝
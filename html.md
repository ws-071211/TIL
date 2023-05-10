# HTML
---
## HTML의 특징
HTML은 Hyper Text Markup Languege의 약자로  마크업 언어이다.

---
## HTML태그

#### HTML 문서 기본 구조
<span style="color: #808080">모든 설명에 <>는 생략함.</span>
!DOCTYPE : 현재 문서의 HTML타입을 정의하며 HTML5의 경우<code>!DOCTYPE html</code>로 명시함 
html: HTML 문서의 시작과 끝을 표시
head: 웹 페이지 문서에 대한 정보로 메타데이터를 정의
<pre>
* style, meta, link, script, base 태그 등 정의
* title: HTML 문서 제목 정의
</pre>
  body: 내부에 웹 페이지의 실제적인 내용
  <pre>
  * h1~h6:제목 크기 설정
  * p:단락 정의
  </pre>
  #### HTML 문서 요소
  기본적으로 태그는 시작 태그와 종료 태그로 짝지어 구성
  *시작 태그:<code>title</code>
  *종료 태그:<code>/title</code>
  HTML 요소는 여러 속성을 가짐
  * 태그 이름:p
  * 속성명: class
  * 속성값: value
  * 내용: 단락
  #### 속성
  요소에 추가적인 정보 및 설정 적용
  속성 이름은 대소문자를 구분하지 않지만, 소문자를 권장
  시작 태그에 <code>속성이름 = "값"</code> 형태로 사용됨
  a 태그에 href 속성으로 링크주소의 값을 설정
  #### HTML 주석
  주석은 웹 브라우저가 해석하지 않으며 사용자에게도 보여지지 않읍
  코드의 설명을 위해 작성
  #### HTML 문서 작성 규칙
  content 내의 연속된 공백 또는 줄 바꿈은 하나의 공백으로 처리
  여러 개의 공백이나 탭,줄 바꿈 등은 다른 특수문자를 사용하여 표현
  
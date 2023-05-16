# HTML
---
## HTML의 특징
HTML은 Hyper Text Markup Languege의 약자로  마크업 언어이다.

---
## HTML태그

#### HTML 문서 기본 구조
<span style="color: #">모든 설명에 <>는 생략함.</span>
!DOCTYPE : 현재 문서의 HTML타입을 정의하며 HTML5의 경우<code>!DOCTYPE html</code>로 명시함 
html: HTML 문서의 시작과 끝을 표시
head: 웹 페이지 문서에 대한 정보로 메타데이터를 정의
<pre>
* style, meta, link, script, base 태그 등 정의
* title: HTML 문서 제목 정의
</pre>
  body: 내부에 웹 페이지의 실제적인 내용
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
  태그 이름은 대소문자를 구분하지 않으나 보통 소문자로 작성
  각 태그는 시작 태그와 종료 태그 쌍이 서로 교차되면 안 됨
  * 이 경우 오류가 일어나 태그가 작동하지 않음
  태그는 시작 태그와 종료 태글르 함께 사용하며 태그의 내용이 공백이면 다음과 같이 사용가능
  태그는 포함관계를 들여쓰기를 통해 표시하여 작성
  #### HTML 기본 태그
  **텍스트 요소**
  제목 태그
  <pre>
  h: 태그는 제목을 표시할 때 사용
  h1~h6:숫자가 커질수록 크기가 작아짐
  </pre>
  단락 태그
  <pre>
  p:문단을 나타낼때 사용
  문단 전 후로 준 빈 줄이 추가됨
  </pre>
  줄 나누기 태그
  <pre>
  br:강제로 줄 바꿈을 할 때 사용하는 태그
  종료 태그가 없음
  </pre>
  미리 정의된 서식 태그
  <pre>
  pre: pre 태그는 preformatted text로 입력한 텍스트 그래도 화면에 표시할 때 사용하는 태그
  </pre>
  수평선 태그
  <pre>
  hr: 수평선을 표시하는 태그
  </pre>
  **텍스트 서식 태그**
  텍스트 서식 태그
  <pre>
  b ~ /b 굵게
  i ~ /i 기울이기
  small ~ /small 작게
  ins ~ /ins 밑줄
  del ~ /del 가운데 선
  mark ~ /mark 하이라이트
  strong ~ /strong 중요(굵게)
  code ~ /code 코드(얇은 글씨)
  em ~ /em 강조(기울이기)
  sup ~ /sup 위 첨자
  sub ~ /sub 아래 첨자
  </pre>
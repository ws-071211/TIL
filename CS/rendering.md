# Browser rendering
browser가 서버로부터 html,css,js 등이 작성된 파일을 받아 유저에게 노출시켜주는 것을 의미한다. 
> **browser**  
> 유저가 원하는 자원을 서버에 요청해 화면에 표시하는 것  
자원은 HTML문서, PDF 파일, 이미지 파일 등으로 다양한 형태를 띄고 자원의 주소는 URL에 의해서 결정된다.
## 순서
1. 로더가 서버로부터 문서를 불러와 전달받는다.
2. 웹 엔진의 HTML/XML 파서가 HTML문서를 파싱해 DOM 트리를 생성한다.
3. 웹 엔진의 CSS 파서가 css문서를 파싱해 CSSOM 트리를 생성한다. 이 CSSOM은 DOM이 어떻게 화면에 보여질지를 정해준다.  
4. 위 과정에서 생성된 DOM 트리와 CSSOM 트리를 합쳐 Render 트리를 구축한다.
5. Render 트리의 요소들이 표시될 위치와 크기를 계산한다.
6. 계산이 완료된 요소들을 크기와 위치에 맞게 화면에 출력한다. layout -> paint 순서로 이루어진다.
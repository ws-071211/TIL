# meta
웹페이지가 담고 있는 컨텐츠가 아닌 웹페이지 자체의 정보를 명시하기 위한 목적으로 사용되는 HTML 태그를 의미한다.  
주로 html 파일의 `<head>`안에 사용되며 `<body>`앞에만 사용되면 된다.
## meta의 종류
- Keywords: 검색엔진에 의해 검색되는 단어를 지정한다.
- Description: 검색결과에 표시되는 문자를 표시한다.
- robots: 검색 제어 로봇
  - All(default) : 색인 생성이나 게재에 대한 제한이 없다, 기본값이므로 명시적으로 표시해도 효과 없음
  - noindex: 검색 결과에 이 페이지를 표시 하지 않음.
  - nofollow:  이 페이지의 링크를 따라가지 않음.
  - noarchive: 검색결과에 저장된 페이지 링크를 표시하지 않음.
  - Non: noindex, nofollow와 같음.
  - index: 그 페이지를 수집대상으로 함.
  - Follow: 그 페이지를 포함해 링크가 걸린 곳을 수집대상으로 함.
- charset: 문자 코드의 종류 설정한다.
- Date: 날짜 제작일을 표시한다.
- Content-Script-Type: 웹페이지에 사용된 언어를 표시한다.
- Content-Script-Type: 브라우저 호환성을 표시한다.
- subject: 브라우저의 주제를 지정한다.
- title: 브라우저의 제목을 지정한다.
- Author: 페이지를 만든 제작자의 이름을 표시한다.

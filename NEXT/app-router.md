# app router

next 13 이상에서 사용가능한 페이지 라우팅 방식 중 1개이다.
사용자가 다른 경로로 이동할 경우 해당 경로에 알맞는 페이지를 사용자에게 보여지도록 해당 페이지의 컴포넌트를 렌더링시켜준다.
서버 중심 라우팅으로 서버 컴포넌트를 기반으로 구축되었있다.

## 장점

- 동적 경로
  - 동적으로 경로에 맞는 매칭을 지원
- 초기 로딩
  - 필요한 부분만 로딩하기 때문에 초기 로딩을 최적화할 수 있다.
- 레이아웃
  - root 레이아웃과 여러 레이아웃을 조합할 수 있다.

## page router와의 차이

- 클라이언트 중심 라우팅으로 파일 시스템을 기반으로 구현한다.
- 파일 이름이 경로이다.
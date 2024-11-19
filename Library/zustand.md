# zustand

리액트의 전역 상태관리 라이브러리이다.
zustand는 독일어로 상태라는 의미를 가지고 있다.

## 특징

- 작고 빠르다.
  - 간단하고 우수한 성능을 가지고 있다.
  - redux보다 설정이 간편하다.

- react hooks api 기반
  - react hooks api를 기반으로 제작되어 react 개발자들의 코드 파악에 도움을 준다.
  - redux와 달리 복잡한 구조를 피해 간단한 함수형 컴포넌트 내에서 상태 관리가 가능하다.

- 렌더링 최적화
  - 상태 변경 시 컴포넌트를 필요할 때만 다시 렌더링하기때문에 불필요한 렌더링을 방지하여 성능 향상에 도움을 준다.

- 코드 단축
  - redux의 경우 store, action, reducer 와 같이 많은 보일러플레이트 코드를 필요로 하지만, zustand의 경우 보다 더 적은 코드로 상태관리가 가능하다.
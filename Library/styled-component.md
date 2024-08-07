# styled-components

## styled-components란?

태그나 id, class이름으로 가져와 쓰지 않고, 동일한 컴포넌트에서 컴포넌트 이름을 쓰듯 스타일을 지정하는 것을 styled-components라고 부른다.
css 파일을 밖에 두지 않고, 컴포넌트 내부에 넣기 때문에, css가 중첩되지 않도록 만들어주는 장점이 있다.

설치법

```javascript
npm install -i styled-components
```

## 기본 문법

styled-components를 사용하기 위해서는 styled를 import 해야한다.

```javascript
import styled from "styled-components";
```

html의 모든 태그에 스타일을 적용할 수 있다.
적용 방법은 styled.tagName과 같이 작성한 뒤, 적용하고자 하는 CSS 스타일을 작성하면 된다.

```javascript
import styled from "styled-components";

const CD = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
`;

const PD = styled.div`
  background-color: #cf6a87;
  width: 100px;
  height: 100px;
`;

const VD = styled.div`
  background-color: #574b90;
  width: 100px;
  height: 100px;
`;

const App = () => {
  return (
    <CD>
      <PD />
      <VD />
    </CD>
  );
};
```

전역 사용을 하려면 styled 대신 createGlobalStyle를 사용하면 된다.

## Props 이용

1. 컴포넌트의 props에 값을 설정한다.

```javascript
function App(){
  return(
    <Block bgcolor="blue"/>
    <Block bgcolor="red"/>
  )
}
```

구조분해할당 예시

```js
function App() {
  const [done, setDone] = useState(true);
  return <Block done={done} />
}
```

2. styled-components에서 props를 가져와서 적용시킨다.
(`${(props) => props.bgColor};`처럼 사용하면 된다.)

```js
  const Block = styled.div`
    width: 100px;
    height: 100px;
    background-color : ${(props) => props.bgColor};
  `
```

구조분해할당

```javascript
  const Block = styled.div`
    width: 100px;
    height: 100px;
    background-color: ${({done}) => done ? "red" : "blue"};
    color: ${({done}) => done ? "black" : "white"};
  `;
```

## 상속

컴포넌트 스타일을 상속받을 수 있다.
styled(Block): Block의 컴포넌트 스타일을 가져옴

```javascript
const RoundBlock = styled(Block)`
  border-radius: 50px;
`;
```

## 애니메이션

styled-components에서는 애니메이션 효과를 넣기위해서 keyframes이라는 유틸을 사용한다.

```javascript
import {keyframes} from "styled-components"

const fade = keyframe`
  0%{
    opacity: 1;
  }
  25%{
    opacity: 0.5;
  }
  50%{
    opacity: 0
  }
  75%{
    opacity: 0.5;
  }
  100%{
    opacity: 1;
  }
`

const Box = styled.div`
  width: 100px;
  height: 100px;

  animation: ${fade} 1s 2s infinite;
  //animation: ${애니메이션 이름} | 실행시간 | 지연시간 | 반복 횟수

`
```

## 전역 스타일

모든 html 요소에 대해서 공통적인 스타일을 가질 수 있게 설정하는 역할을 한다.

createGlobalStyle을 사용한다.

```js
import { createGlobalStyle } from "styled-components";

const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  li {
    list-style: none;
  }

  button {
    cursor: pointer;
  }
`;

export default GlobalStyle;

```

이 파일을 app.jsx파일에서 import하여 해당 엘리먼트 최상단에 작성해주면 적용된다.

```js
import GlobalStyle from "./GlobalStyles";

function App() {
  return (
    <>
      <GlobalStyle />
      <ul>
        <li>
           list
        </li>
      </ul>
      <button>
        button
      </button>
    </>
  );
}

export default App;
```

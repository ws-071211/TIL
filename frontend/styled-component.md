# styled-components
## styled-components란?
태그나 id, class이름으로 가져와 쓰지 않고, 동일한 컴포넌트에서 컴포넌트 이름을 쓰듯 스타일을 지정하는 것을 styled-components라고 부른다.
css 파일을 밖에 두지 않고, 컴포넌트 내부에 넣기 때문에, css가 중첩되지 않도록 만들어주는 장점이 있다.   

설치법   
```javascript
npm i styled-components
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

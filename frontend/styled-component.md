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
html
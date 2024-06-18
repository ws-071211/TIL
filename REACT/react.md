# React

---

## React란

React는 웹 프레임워크이자 자바스크립트의 라이브러리 중 하나로서 사용자 인터페이스를 만들기 위해 사용된다.

---

## React의 특징

1. 선언적인 개발    
개발 방식을 크게 두가지로 나누면 선언적 방식과 절차적 방식으로 나눌 수 있다.   
절차적 방식은 모든 절차를 되짚어보면서 문제가 무엇인지 확인하는 방식으로 프로그램이 복잡해질수록 유지보수가 힙들어진다.    
선언적 방식은 우리가 생각한 모습과 출력된 모습의 차이를 비교하는 방식으로 절차적 방식보다 유지보수가 쉽다.

2. Virtual-DOM   
Virtual-DOM은 가상의 DOM을 말한디. DOM은 HTML 문서를 제어할 수 있는 API 트리 자료구조다. react에서 사용하는 가상 DOM도 실제 DOM에 기반하여 만들어진다.
   > **Virtual-DOM을 사용하는 이유?**   
   가상 DOM을 만들어 이벤트가 새로 발생할 때마다 실제 DOM과 비교하여 최소한의 변경사항만 반영하기 위함이다. 또한 실제 DOM에는 브라우저가 화면을 표현하는데 필요한 정보가 모두 들어있어 실제 DOM을 이용하여 작업을 하기엔 무거우며 속도가 느리다. 그래서 가상 DOM을 이용해 효율성과 속도를 개선할 수 있다.

   virtual-DOM은 리액트가 화면을 업데이트 하는 과정을 조금 더 효율적으로 수행하기 위한 구조이다.

3. CRA
   >Create React App의 약어이다.   
    CRA는 리액트 프로젝트를 시작하는데 필요한 개발 환경을 세팅 해주는 도구이다.

   - 리액트는 UI 기능만을 제공하는 라이브러리다. 그러나 실제 온전한 웹사이트를 구축하기 위해서는 UI 구성 외에도 여러가지 다른 도구들이 필요하다.    
   그래서 리액트로 프로젝트를 진행하기 위해서는 필요한 도구들을 toolchain이라고 부른다.
   - CRA는 리액트로 웹 애플리케이션을 만들기 위한 환경을 제공한다.
   - CRA를 이용하면 하나의 명령어로 리액트 개발환경 구축이 가능하다.

4. Component   
component는 **재사용**이 가능한 구성단위이다.   
component 사용시에는 여러 장점이 있다.

   >- 코드의 유지보수가 편함
   >- 페이지 구성을 파악하기 쉬움
   >- 컴포넌트가 다른 컴포넌트를 포함할 수 있다.

5. JSX   
자바스크립트 확장 문법이다. 형태는 자바스크립트와 html을 합쳐놓은 듯한 문법이다. 또한 마크업을 편리하게 작성하기 위한 문법이며 JSX로 작성한 코드는 실제 자바스크립트가 인식할 수 없는 문법이기에 Babel이라는 패키지를 이용해서 변환해줘야 한다.
   >**특징**
   >- 모든 태그들은 하나의 부모태그로 감싸져야 한다.
   >- 모든 태그들은 셀프 클로징이 가능하다.
   >- 모든 property들은 camelCase로 사용한다.
   >- 자바스크립트 동작이 가능하다.

   >**장점**
   >- HTML 태그를 그대로 사용하기 때문에 사용감이 익숙하다.
   >- HTML 마크업과 자바스크립트 로직을 같이 구현할 수 있다.
   >- 자바스크립트 문법을 이용해서 HTML을 생성할 수 있다. 별도의 HTML 파일이 필요하지 않다.

## 컴포넌트 종류
### 함수형 컴포넌트
function으로 정의한 뒤 return문에 있는 jsx코드를 반환한다.
```javascript
import React from "react";

function comp(){
  const box = "name";
  return(
    <>
       <p>{name}</p>    
    </>
  )
}

export default comp;
```
function은 arrow function으로 작성해도 된다.
```javascript
import React from "react";

const comp = () => {
  const box = "name";
  return (
    <>
      <div>
        {name}
      </div>
    </>
  )
};

export default comp;
```

### 클래스형 컴포넌트   
class로 정의하고 render()함수에서 jsx코드를 반환한다.    
```javascript
import React, { Component } from "react";

class Comp extends Component {
  render() {
    const box = "name";
    return (
      <div className="react">
        {name}
      </div>
    );
  }
}

export default Comp;
```
클래스형 컴포넌트에서는 state를 사용할 수 있으며 각종 생명주기 및 메서드를 이용하여 컴포넌트가 마운트 혹은 언마운트 될 때 추가 작업을 수행시키는 등 조작을 할 수 있었는데 Hook이 등장한 이후부터는 위 기능들을 함수형 컴포넌트에서도 대부분 구현이 가능하게 되었다.

### 두 컴포넌트의 차이
클래스형은 임의의 메서드를 정의할 수 있고 state와 LifeCycleAPI의 사용이 가능하다.   
함수형은 클래스형보다 선언이 편하고 메모리 자원도 클래스형보다 덜 사용하고 빌드한 결과물 역시 클래스형보다 작다.   
그리고 클래스형과 마찬가지로 state와 같이 생명주기의 사용이 가능하다.(hook 사용)

## 생명주기
1. mount:사용자한테 보여지는 화면 상태
2. unmount:사용자한테 안 보여지는 화면
3. update:상태가 변할 떄

## hooks
- useState : 컴포넌트의 상태를 간편하게 생성 및 업데이트 해주는 도구를 제공해주는 hook

  사용법
  ```javascript
  import {useState} from 'react';
  //useState의 사용을 위한 import
  const [coin,setcoin] = useState(/*초기값*/);
  //useState의 변수 선언
  setcoin(1);
  //coin의 값 변경
  ```
  


- useEffect : 컴포넌트가 렌더링 될 때마다 특정 작업을 실행할 수 있도록 하는 hook

  컴포넌트가 mount 되었을 때, unmount 되었을 때, update 되었을 때의 특정 작업을 처리할 수 있다.

  사용법
  ```javascript
  import {useEffect} from 'react'
  //useEffect의 사용을 위한 import
  useEffect(()=>{

  },[])
  //컴포넌트가 마운트 될 때마다 실행됨
  useEffect(()=>{

  })
  //컴포넌트가 렌더링 될 때마다 실행됨
  useEffect(()=>{

  },[name])
  //name값이 업데이트 될 떄마다 실행됨
  ```
- useRef: 저장공간 또는 DOM에 접근하기 위한 hooks이다.    
javascript에 queryselector와 같이 특정 DOM에 접근해야하는 상황에서 사용한다
  
  - useRef로 관리하는 값은 값이 변해도 화면이 새로 랜더링되지 않는다.


- useParams : react-router-dom에서 제공해주는 hooks 중 하나로 파라미터값을 URL을 통하여 넘겨받은 페이지에서 사용할 수 있게 해준다.
## custom hooks
반복되는 로직이 있을 때 custom hooks를 만들어 겹치는 여러 줄의 코드를 1줄로 요약하는 방법이다.

custom hook를 생성할 때에는 `use~~~`의 이름으로 적는 것이 좋다.

> vsc에서 hook으로 판단하여 적절한 메시지를 추천해준다.


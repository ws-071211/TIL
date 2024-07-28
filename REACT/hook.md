# hook 
react hook은 react 16.8버전에 새로 도입된 기능으로 기존 생명주기를 사용해야할 경우에 클래스형 컴포넌트로 사용해야했지만 기존 클래스형에 여러 단점이 있었기에 이를 보완하여 함수형에서도 사용 가능하게 만든 것이 react hook이다.  
대표적인 hook으로는 useState, useEffect 등이 있다.
> 생명주기
>1. mount:사용자한테 보여지는 화면 상태
>2. unmount:사용자한테 안 보여지는 화면
>3. update:상태가 변할 떄

## 대표적인 hook 예시

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
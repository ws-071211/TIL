# React

---

## React란

React는 웹 프레임워크이자 자바스크립트의 라이브러리 중 하나로서 사용자 인터페이스를 만들기 위해 사용된다.

---

## React의 특징

- Data Flow:단방향의 데이터 흐름을 가짐
  - 단방향인 이유: 양방향 데이터 바인딩은 규모가 커질수록 데이터의 흐름을 추적하기 힘들고 복잡해져서 예측이 비교적 쉬운 단방향을 사용한다.
- Component 기반 구조:UI를 여러 컴포넌트로 나누고 조립하여 만든다.
  - component란?:독립적 단위의 소프트웨어 모듈
- Props and State
  - Props:부모 컴포넌트에서 자식 컴포넌트로 전달해주는 데이터이고 전달 받은 Props는 변경이 불가능하고 Props를 전달한 최상위 부모 컴포넌트에서만 수정 가능하다.
  - State:컴포넌트 내부에서 값을 변경하고 동적인 데이터를 다룰 때 사용하며, 사용자와의 상호작용을 통해 데이터를 동적으로 변경할 때 사용하고 클래스형 컴포넌트에서만 사용할 수 있고 각각의 state는 독립적입니다. 

## JSX
- 

## 생명주기
1. mount:사용자한테 보여지는 화면 상태
2. unmount:사용자한테 안 보여지는 화면
3. update:상태가 변할 떄

## hooks
- useState:컴포넌트의 상태를 간편하게 생성 및 업데이트 해주는 도구를 제공해줌

  사용법
  ```javascript
  import {useState} from 'react';
  //useState의 사용을 위한 import
  const [coin,setcoin] = useState(/*초기값*/);
  //useState의 변수 선언
  setcoin(1);
  //coin의 값 변경
  ```
  


- useEffect:컴포넌트가 렌더링 될 때마다 특정 작업을 실행할 수 있도록 하는 hook

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
  useEffect(()=>{
    
  })
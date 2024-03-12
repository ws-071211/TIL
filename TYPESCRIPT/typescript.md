# TypeScript
## 타입스크립트란?
마이크로소프트에서 개발 및 관리되고 있는 자바스크립트의 슈퍼셋인 오픈소스 프로그래밍 언어로 엄격한 문법을 지원한다.  
자바스크립트에  타입을 부여한 형태로 자바스크립트의 문법과 대부분 동일하다.  
자바스크립트의 슈퍼셋이기 때문에 자바스크립트로 컴파일되어 실행된다.  

## 타입스크립트의 특징
브라우저에서는 타입스크립트가 동작하지 않는다.  
그래서 타입스크립트의 컴파일러를 통해 자바스크립트 코드로 변환주어야된다.

## 타입스크립트의 장점
1. 정적 타입 지원
자바스크립트는 실행중에 매개변수와 반환값의 타입을 실행중에 결정하는 동적 타입의 인터프리터 언어여서 코드 작성중에는 코드의 오류를 찾기 어려울 수 있다.  
하지만 타입스크립트는 정적 언어이기 때문에 코드 작성중에 오류를 컴파일 단계에서 발견할 수 있어서 디버깅을 보다 쉽게 할 수 있다.
2. 실행 속도  
아까 설명했듯이 자바스크립트는 동적 타입의 인터프리터 언어이다. 타입스크립트는 정적 타입인 컴파일러 언어라서 사전에 타입을 결정하기 떄문에 자바스크립트처럼 추가로 타입을 결정하고 오류를 발견하는 작업을 줄여서 실행 시간이 빨라진다.

## 타입스크립트의 단점
1. 코드량 증가  
자바스크립트에서 타입이 추가된 만큼 타입 선언도 추가로 해주어야해서 코드량이 더 증가하여 개발 시간이 길어진다.
2. 초기 설정
타입스크립트는 초기의 세팅이 까다롭고 귀찮지만 **이 단점은** `CRA`,`Vue CLI`,`Angular CLI`같은 초기 세팅 도구를 사용하면 세팅해야 될 프로젝트 구조와 컴파일 옵션을 자동으로 설정해준다.
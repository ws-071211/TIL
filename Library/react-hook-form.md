# React Hook Form
react hook form은 react 기반의 폼 관리 라이브러리이다.  
간편한 유효성 검사와 폼 상태를 관리할 수 있다.

react hook form  사용 시 유효성 검사를 위해 필요한 코드를 줄일 수 있고 이를 통해 개발과 유지보수를 더 용이하게 할 수 있다.

## 장점
- 성능 최적화  
성능을 최우선으로 하여 설계한 만큼 불필요한 작업을 최소화하였다.

- 간편한 API  
API가 쉽고 직관적이다.
ex)handleSubmit,register

- 유연성과 확장성
다양한 유효성 검사 규칙을 사용하여 정보를 쉽게 처리할 수 있고다른 상태 관리 라이브러리와 
사용할 수 있다.
ex)Redux

## 기능
- input 설정
  - required  
   필수 입력 필드로 설정한다.
  - pattern  
  정규식을 사용해 입력값의 형식을 검증한다.
  - aria-invalid  
  접근성을 위한 속성으로, 폼이 제출된 후 오류가 있는지 여부를 낸다.
- 이외의 기능
  - isSubmitting  
  폼이 현재 제출 중인 경우 true로 설정된다. 제출 중이 아닌 경우 false이다.
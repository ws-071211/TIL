# cookie
브라우저에 저장되는 key와 value로 이루어진 작은 문자열 데이터이다.
> ## 등장배경
>http는 비연결성과 무상태성의 특징을 가지고있어 한번 서버에 요청하고 응답을 받으면 연결이 끊긴다. 그래서 다음에 다시 서버에 또 요청한다고해도 서버는 요청했던 클라이언트를 기억하지 못한다. 하지만 연결이 끊어져도 기억하고 싶은 데이터가 존재하기 떄문에 쿠키가 등장했다. 쿠키를 사용하면 서버에서 사용자의 정보에 대한 정보가 담긴 쿠키를 전달하고 다음에 클라이언트가 다시 서버에 쿠키를 포함한 정보를 요청시 서버에서 클라이언트를 식별하여 정보를 전달해줄 수 있다.

## 특징
1. 4kB의 용량제한
2. 만료일 설정
3. http 요청시 따로 설정하지 않아도 자동으로 전달

## 활용예시
1. 로그인 유지
> cookie에 로그인 정보를 저장하여 서버에 요청시 인증을 받을 수 있다.
2. n일 동안 보지 않기
> cookie에 만료일을 설정하여 해당 정보를 안 뜨게 설정할 수 있다.

## 단정
1. 4KB라는 적은 용량
2. 불필요한 정보까지 서버에 요청됨
3. XSS,XSRF 공격에 취약하다.
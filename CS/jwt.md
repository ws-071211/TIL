# JWT
jwt는 json web token의 줄임말이고 인증 정보를 json형식으로 암호화하여 토큰으로 만든 후 해당 토큰을 클라이언트로 전달하는 인터넷 표준 인증 방식을 뜻한다.  

## 구조
- Header
  - 토큰 타입
  - 알고리즘 정보
- Payload
  - 전달할 내용  
    ```
    iss 토큰 발급자
    exp 토큰 만료 날짜
    sub 토큰 제목
    iat 토큰 발급 시간
    aud 토큰 대상자
    jti 토큰 식별자
    nbf 토큰 활성 날짜 
    등등..
    ```
- Signature
  - Header와 Payload의 인코딩된 정보와 .을 포함하여 알고리즘 방식과 secret key를 포함하여 해싱한다

## 장점
- 클라이언트에서 관리하기 때문에 서버에서 세션 정보를 유지할 필요가 없다.
- 클라이언트에서 인증 정보를 관리하기 때문에 서버를 확장하거나 분산시키는 것이 용이하다.
- Signature로 정보의 위변조를 막을 수 있음
## 단점
- 클라이언트에서 관리하기 떄문에 탈취되거나 조작될 수 있다.  
- 서버와 클라이언트 모두에서 관리해야 하기 떄문에 구현이 힘들 수 있다.
- Payload는 암호화가 되지않아 중요한 정보를 담을 수 없다.
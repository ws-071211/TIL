# token
클라이언트에서 인증 정보를 보관하는 방법이다.  
매 요청마다 db를 찾아보며 인증하는 것도 부담이 되어서 토큰 인증 방식이 생겼다.  
클라이언트에 저장하더라도 암호화가 된 상태의 정보라서 보안이 취약하지 않아서 클라이언트에 저장할 수 있다.  

## Access token
특정한 정보에 접근할 수 있는지 여부를 판단하는데 사용되는 token이다.  
클라이언트가 처음 인증을 받을 때 access token과 refresh token을 받는데 access token에 권한이 담겨있다.  
그리고 토큰이 탈취되면 위험하기 때문에 만료기간을 되도록 짧게 설정해야한다.

## Refresh token 
access token이 만료되었을 떄 refresh token이 있는지에 따라 다시 access token이 다시 생성된다.
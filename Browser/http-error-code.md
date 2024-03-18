# http 상태 코드
http 상태 코드는 http 요청이 성공적으로 이루어졌는지를 알려주는 역할을 한다. http의 상태는 5개로 나누어지는데 정보성 상태코드, 성공 상태코드, 리다이렉션 상태코드, 클라이언트 에러 상태코드, 서버 에러 상태코드가 있다.  
#### HTTP 응답 코드

1. 2xx 성공
  - `200`: 클라이언트의 요청을 성공적으로 처리했음을 알려주는 상태코드
  - `201`: 클라이언트에게 리소스 생성 작업을 요청 받았고 리소스 생성작업을 성공했음을 알려주는 상태코드
  - `204`: 요청은 성공했지만 응답할 콘텐츠가 없음을 알려주는 상태코드
2. 3xx 리다이렉션
  - `301`: 요청한 리소스의 URL이 변경되었으며, 이후 요청부터는 새 URL을 사용해야함을 알려주는 상태코드
  - `302`: 301과 같지만 임시적으로 주소가 바뀌었을 때 알려주는 상태콛,
3. 4xx 클라이언트 오류
  - `400`: 클라이언트가 올바르지 못한 요청을 보냄
  - `401`: 로그인을 하지 않아서 페이지를 열 권한이 없음을 알려주는 상태코드( 권한 없음 )
  - `403`: 금지된 페이지, 로그인을 하든 안 하든 접근할 수 없음을 알려주는 상태코드 ( 관리자 권한 관련 )
  - `404`: 찾을 수 없는 페이지 없는 주소를 입력했음을 알려주는상태코드
  - `408`: 요청 시간이 초과되었음을 알려주는 상태코드
  - `410`: 영구적으로 사용할 수 없는 페이지임을 알려주는 상태코드
  - `429`: 사용자에게 주어진 시간동안 너무 많은 요청을 보넀음을 알려주는 상태코드
4. 5xx 서버 오류
  - `501`: 해당 요청을 처리하는 기능이 만들어지지 않음을 알려주는 상태코드
  - `502`: 서버로 가는 요청이 중간에서 유실된 경우에 발생하는 상태코드
  - `503`: 서버가 터졌거나 유지보수 중임을 알려주는 상태코드
  - `504`: 서버 게이트웨이에 문제가 생겨 시간 초과가 되었음을 알려주는 상태코드
  - `505`: HTTP 버전이 달라 요청을 처리할 수 없음을 알려주는 상태코드
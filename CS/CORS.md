# CORS(cross-origin resource sharing)
CORS는 직역할 시 '교차 출처 리소스 공유'라고 해석할 수 있고 여기서 교차 출처는 출처가 다르다는 걸 의미한다.  
즉 서로 도메인이 다른 곳에서 리소스를 주고받을 때의 보안을 위해 생긴 정책이라고도 할 수 있다.  
프론트엔드와 백엔드가 협업하면서 각자 따로 서버를 열었을 때도 서로의 포트가 달라서 교차 출처로 판단되어 CORS위반 에러가 발생한다.  
교차 출처와 동일 출처를 구분하는 기준은 Origin이 다른가로 판단한다.  
Origin이란 `https://www.google.com/search?q=enbraning`와 같은 URL이 있을 때 `https://`까지는 protocol `www.google.com`은 host `/search`는 path `?q=enbraning`은 querystring이라고 한다. 여기서 origin에 해당하는 부분은 protocol와 host부분이고 host부분 뒤에는 `:8080`등의 포트 번호도 있는데 이 부분또한 origin으로 분류된다. 이 중에 1개라도 다르다면 그 origin은 cross-origin으로 분류된다.

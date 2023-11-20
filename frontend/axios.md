# axios   
## axios란?
- 브라우저,Node.js를 위한 Promise Api를 활용한 http 비동기 통신 라이브러리이다.
- 백엔드와 프론트엔드의 통신을 쉽게하기 위해 Ajax도 더불어 사용한다.

## 특징
- 운영 환경에 따라 브라우저의 XMLHttpRequest 객체 또는 Node.js의 http api 사용함
- Promise Api를 사용함
- 요청과 응답데이터의 변형
- HTTP 요청 취소
- HTTP 요청과 응답을 JSON 형태로 자동 변경

## Fetch Api와의 차이점?
axios는 별도의 설치가 필요하지만 fetch는 브라우저에 빌트인이라서 설치할 필요가 없다.   
axios는 XSRF 보호를 해주고 data 속성을 사용하고 자동으로 JSON 형식으로 변환되고 요청 취소와 타임아웃을 걸 수 있다.   
fetch는 별도의 보호가 없으며 body 속성을 사용하고 .json()메서드를 사용해야 하고 요청을 취소하고 타임아웃을 걸 수 있는 기능이 없다.   
한 마디로 axios가 fetch에 비해 간편하다.

## axios 사용법
### axios 설치하는 법
```
npm install axios
```

### axios 문법 구조
```javascript
axios({
  url: 'https://wordlist/days', 
  method: 'get',
  data: { 
    day: '1'
  }
});
```
### axios 요청 파라미터   
- method : 요청방식(기본은 get)   
- url : 서버 주소
- baseURL : url을 상대경로로써 사용할 때 url 맨 앞에 붙는 주소.

    - 예시로 url이 /day이고 baseURL이 `https://wordlist/days`이면, `https://wordlist/days/day`로 요청이 간다.

- headers : 요청 헤더   
- data : 요청 방식이 `PUT`, `POST`, `PATCH` 일때 body에 보내는 데이터   
- params : URL 파라미터(url get방식을 객체로 표현한 것)   
- timeout : 요청 timeout이 발동 되기 전 miliseconds의 시간을 요청. timeout보다 요청이 길어진다면, 요청은 취소된다.
- responseType : 서버가 응답해주는 데이터의 타입 지정(arraybuffer, document, json, text, stream, blob)
- withCredentials : cross-site access-control 요청을 허용 유무. 이를 true로 하면 cross-origin으로 쿠키값을 전달 할 수 있다.

### Axios 단축 메소드

axios를 편리하게 사용하기 위해 모든 요청 메소드는 aliases가 제공된다.    
위 처럼 객체 옵션을 이것저것 주면 가독성이 떨어지고 너저분하니, 함수형으로 재구성하여 나눠논 것으로 이해하면 된다.    
axios의 Request method에는 대표적으로 다음과 같은 것들이 있다.

- GET : axios.get(url[, config])
- POST : axios.post(url, data[, config])
- PUT : axios.put(url, data[, config])
- DELETE : axios.delete(url[, config])

#### GET   

get메서드가 필요한 상황은 크게 2개의 상황이 있다.     

단순 데이터(페이지 요청,지정된 요청)를 요청을 수행할 때   
파라미터 데이터를 포함시키는 경우 (사용자 번호에 따른 조회)

#### POST

post메서드에는 일반적으로 데이터를 Message body에 포함시켜 보낸다.   
get메서드에서 params를 사용한 경우와 비슷하게 수행된다.   

#### Delete

delete 메서드에는 일반적으로 body가 비어있다.

REST 기반 API 프로그램에서 데이터베이스에 저장되어 있는 내용을 삭제하는 목적으로 사용한다.

하지만 query나 params가 많아져서 헤더에 많은 정보를 담을 수 없을 경우에는 data를 두번째 인자에 포함시켜줄 수 있다.

#### PUT
REST 기반 API 프로그램에서 데이터베이스를 수정/갱신할 때 사용한다.   
PUT메서드는 서버에 있는 데이터베이스의 내용을 변경하는 것이 주 목적이다.   
PUT메서드는 서버 내부적으로 get -> post 과정을 거치기 때문에 post 메서드와 비슷한 형태이다.
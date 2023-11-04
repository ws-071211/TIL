# axios

- Promise 기반의 http 비동기 통신 라이브러리이며 http 메서드의 전부를 지원한다.
    ```
     axios.get(url[, config])
     axios.delete(url[, config])
     axios.post(url[, config])
     axios.put(url[, config])
    ```
>### HTTP 메서드
>  클라이언트가 웹서버에게 사용자 요청의 목적/종류를 알리는 수단
> get:입력한 url에 존재하는 자원에 요청을 하는 메서드
> - get은 서버에서 어떤 데이터를 가져와서 보여주는 용도이다.
>그렀기 떄문에 값이나 상태의 변경은 불가하다.
>응답은 json 형태로 넘어온다


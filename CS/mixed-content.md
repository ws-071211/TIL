# mixed-content

![예시 사진](/asset/mixed-content.png)
mixed-content error는 보안상의 이유로 브라우저에서 발생하는 에러이다.  
이미 암호화가 되어있는 https 페이지에서 http로 요청을 보내는 경우 발생한다.  
위에 예시 사진과 같이 `https~~`의 client에서 `http~~`의 server로 요청을 보내는 경우가 해당한다.

## 해결 방법

1. **서버의 URL 프로토콜을 https로 변경**  
기존의 서버의 URL이 `http`로 되어있는 경우, 서버의 URL을 `https`로 변경한다. 하지만 `https`를 지원하지 않을 경우 해결되지 않는다.

2. **`<meta>`를 적용하여 `http`를 변경**  
```
<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
```
위의 코드를 적용하여 브라우저에게 모든 `http` 요청을 `https`로 변경하도록 지시하여 해결하는 방법도 있다.

# Turbopack
vercel에서 개발한 웹팩의 새로운 rust 기반의 차세대 번들링 툴이다.
## 기능
- 웹팩보다 700배 빠르고 vite보다 10배 빠르다.
![사진](/asset/image.png)
- 다양한 파일을 변환하고 모듈 해결 방법을 변경하기 위해 사용자 정의할 수 있다.

### Turbopack이 빠른 이유??
turbopack은 turborepo와 구글의 bazel에서 영감을 받았다. 그리고 이 두 도구는 캐시를 활용하여 같은 작업을 두번 이상 실행하지 않게 해주게 핵심입니다.  
그래서 turbopack은 turbo라는 프레임워크를 사용하여 어떤 함수의 결과라도 캐싱할 수 있게 하였다.  
이러한 과정을 통해서 입력값이 변경될 경우에만 계산을 실행하기 때문에 압도적으로 빠를 수 있다.  
그래서 규모가 큰 웹 사이트의 경우 대부분의 작업을 건너뛰어 웹팩보다 700배 빠른 속도를 낼 수 있다.

## 설치
next 13 이상 버전부터 사용할 수 있고 다음 명령어로 쉽게 사용할 수 있다.
```
npx create-next-app --example with-turbopack
```
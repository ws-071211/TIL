# Dependencies, devDependencies

## Depnedencies

package.json 파일에 있는 dependencies는 패키지 매니저를 통해 설치한 라이브러리들이 들어가있는 곳이다. 실제 애플리케이션의 동작에 영향을 끼치기 떄문에 dependencies에 설치된 라이브러리의 경우 배포시 같이 배포된다.

## devDependencies

dependencies와 비슷하지만 devDependencies의 경우 eslint나 prettier와 같은 개발 환경에만 도움을 주고 실제 애플리케이션 동작에 영향을 끼치지않는 라이브러리들을 설치하는 공간이다. 설치시에 `--dev`나 `-D`를 붙여서 설치하면 해당 라이브러리는 devDependencies에 설치된다.

## 굳이 왜 사용?

dependencies와 devDependencies를 나눠서 설치하는 이유는 불필요한 라이브러리를 포함시키지 않고 빌드 시간도 단축시킬 수 있기 떄문이다.
dependencies와 devDependencies를 구분짓지 않는다면 단순히 코드의 일관성을 맞춰줄 뿐인 라이브러리가 애플리케이션의 빌드시간에 영향을 끼쳐 실제 성능에 영향을 줄 수 있기 때문에 이렇게 구분지어줘야한다.
# Package-manager(js)
## js에서 package manager란?
- js의 package manager는 Node.js의 실행환경에서 수행하며 프로젝트가 의존하고 있는 패키지는 효과적으로 설치,갱신,삭제가 가능하게 도와주는 도구들을 의미한다.    
대표적인 예:npm(node package manager),yarn

## package manager 관련 파일   
- package.json : 프로젝트에서 사용되고 있는 패키지를 관리하는 json형태의 파일
- package-lock.json / yarn.lock : 프로젝트 내에서 팀원들 간에 서로 다른 버전을 설치하지 않고, 동일한 버전을 설치하는 것을 보장하도록 명시된 패키지 잠금 파일   
    - package-lock.json :  npm 패키지 매니저를 사용할 경우 사용되는 잠금 파일
    - yarn.lock : yarn 패키지 매니저를 사용할 경우 사용되는 잠금 파일
- node_modules : package.json 파일에 명시된 패키지에 따라 설치 된 패키지 디렉토리

## 패키지 매니저 종류
- npm : node.js와 함께 기본적으로 설치되며, 많은 개발자들이 널리 사용하고 있다.CLI를 제공하여 패키지 설치,버전 관리,의존성 해결 등의 기능을 수행한다. 패키지를 각각 별도로 설치한다. 이로 인해 중복 설치가 될 수 있다.   

- yarn : Facebook에서 만든 package manager로 npm과 비슷한 목적을 가지고 있다. npm의 속도, 안정성, 보안성 등의 단점을 보완하여 더 나은 성능과 안정성을 제공한다. 여러 개의 패키지를 병렬로 설치하여 빠른 속도를 보장한다.
yarn.lock파일로 의존성을 더욱 확실히 관리한다.

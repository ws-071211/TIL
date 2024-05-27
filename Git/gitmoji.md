# gitmoji
git과 emoji의 합성어로 commit message에 이모지를 추가하는 tool이다.  
일반 commit message에 비해 커밋의 의도와 목적이 이모지를 통해 좀 더 쉽게 확인할 수 있게 된다.  
예를 들면 이모지가 없는 커밋 메시지는 글로 된 메시지로 파악을 해야하지만 이모지가 있는 커밋 메시지라면 한 눈에 이모지에 따라서 목적과 의도의 파악이 가능해지는 기능이 가능해진다.
```
add edit modal

✨ add edit modal
```
위에 두 커밋 메시지를 볼 때는 차이를 못 느낄 수도 있지만 만약 여러 커밋 메시지가 있다면 이모지가 있는 모습이 더 기능별로 찾기 쉬워질 것이다.

## 사용법
설치
```
npm -i g gitmoji-cli
```
> gitmoji는 npm 패키지를 필요로 하기 때문에, 그전에 node.js를 설치해야한다.

`gitmoji -c`: `git commit -m`을 대신하여 커밋 메시지를 작성할 수 있다.
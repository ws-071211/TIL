# husky

husky란 git hook을 쉽게 설정하고 관리하도록 도와주는 라이브러리이다.  
husky를 사용하면 커밋이나 푸시들의 이벤트가 발생하기 전에 prettier나 eslint가 자동적으로 적용되도록 설정할 수 있어 협업 시 사용하면 좋다.

## 기능

- git 이벤트가 발생하기 전에 특정 스크립트가 실행되도록 설정하는 걸 도와준다.

- ex) pre-commit, pre-push

## 설치 및 설정

1. 설치

```
//npm
npm install --save-dev husky lint-staged
//yarn
yarn add --dev husky lint-staged
```

2. 초기화

```
npx husky install
```

3. package.json 설정

```json
{
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": [
      "prettier --write",
      "eslint --fix"
    ]
  }
}
```

4. hook 설정

```yarn
npx husky add .husky/pre-commit "yarn lint-staged"
```

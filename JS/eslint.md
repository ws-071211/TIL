# ESLINT

ESLint는 js 코드에서 문제를 찾아 수정하는데 도움을 주는 코드 분석 도구이다. 도움을 주는 방식은 오류가 발생하는 코드에 표시를 해주고 오류뿐만 아니라 코딩스타일까지 설정할 수 있다.

## 설정

```js
{
  "env": {
    "browser": true,
    "es2021": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:react/recommended",
    "plugin:@typescript-eslint/recommended"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaFeatures": {
      "jsx": true
    },
    "ecmaVersion": "latest",
    "sourceType": "module"
  },
  "plugins": [
    "react",
    "@typescript-eslint"
  ],
  "rules": {
    "semi": ["error", "always"],
    "quotes": ["error", "double"],
    "no-unused-vars": "warn",
    "react/prop-types": "off"
  }
}


```
## Closures
- 함수와 함수가 선언된 어휘적 환경의 조합으로 함수 안에 함수를 선언한 형태를 의미한다.  
- 클로저로 선언된 함수 안에 함수는 외부 함수로 지역변수를 접근할 수 있고 외부 함수의 실행이 끝난 후에도 외부로 접근할 수 있는 것을 의미한다.
```js
function outer(){
  let v = 10;
  function inner(){
    console.log(x)
  }
  return inner;
}
```
위의 함수를 호출 시 이미 실행이 끝난 함수더라도 console에 10이 작성된다.
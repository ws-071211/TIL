# async/await
Promise를 기반으로 사용해 비동기 처리를 하는 문법이다.

## async/await 사용
async는 function앞에 붙여서 사용하고 await는 async로 작성된 function안에 비동기 처리 부분에 앞에 붙여주면 된다.   
async function이 정의되어 있지 않다면 await를 사용할 수 없다.

```javascript
async function test() {
  await delay(1000);
  await delay(2000);
  const result = await Promise.resolve('끝');
  console.log(result);
}
```
async function에서의 리턴값은 무조건 promise객체로 감싸져 반환된다는 특징이 있다.
# map
자바스크립트 배열 내장함수이다.  
React에서 반복되는 컴포넌트를 렌더링하기 위해서 자바스크립트 배열의 내장함수인 map()을 사용한다.   

## Ex
map 미사용
```js
function snack(){
  return(
    <ul>
      <li>과자</li>
      <li>젤리</li>
      <li>빵</li>
      <li>사탕</li>
    </ul>
  )
}
```
map 사용
```js
function snack(){
  return(
    <ul>
      {['과자','젤리','빵','사탕'].map((item,index)=>(
        <li key={index}>{item}</li>
      ))}
    </ul>
  )
}
```
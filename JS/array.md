# 배열
## 배열 리터럴
```js
const arr = [0,1,2,3,4,5];
```
## 배열 생성자
```js
const array = new Array(1,2,3);

const arr = new Array(5);//인수가 1개일 경우 그 인수는 배열의 길이
```
## 배열 메서드
### Array.sort()
배열의 요소들을 오름차순이나 내림차순으로 정렬한다.
```js
const arr = [1,4,3,2,5];

const sort_arr = arr.sort();//(a,b)=>a-b
const sort_arr2 = arr.sort((a,b)=>b-a);

console.log(sort_arr);
console.log(sort_arr2);
```

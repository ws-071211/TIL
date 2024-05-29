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

### Array.join()
배열을 문자열로 변환해준다.
```js
const arr = ["a","p","p","l","e"];

console.log(arr.join(''));//apple
```

### Array.reverse()
배열의 순서를 반대로 뒤집는다.
```js
const arr = ["a","p","p","l","e"];

console.log(arr.reverse());//elppa
```

### Array.slice()
배열의 특정 부분만 반환해준다.
```js
const arr = [1,2,3,4,5];

const slice = arr.slice(3);
const slice2 = arr.slice(1,4);

console.log(slice);//[4,5];
console.log(slice2);//[2,3,4];
```

### Array.map()
배열의 아이템을 순서대로 받아 map안에 명령문을 실행한다.
```js
const arr = [1,2,3,4,5];
const res = 0;

arr.map(item=>res+=item);

console.log(res);//15
```

### Array.push()
배열의 끝에 새로운 아이템을 추가해준다.
```js
const arr = [1,2,3,4,5];

arr.push(6);

console.log(arr);//[1,2,3,4,5,6]
```
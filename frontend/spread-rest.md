# spread
스프레드 연산자는 배열이나 객체의 값을 나열하는 연산자이다.

스프레드 연산자는 `...변수명` 으로 사용이 가능하다

이 말의 뜻은 
```javascript
const array=["I"," am"," student"];
console.log(array);//["I"," am"," student"]
console.log(...array);//I am student
```
와 같이 표시된다는 말이다.

# rest

스프레드 연산자와 사용법은 똑같지만 객체,배열,함수의 파라미터에도 사용가능한 rest연산자도 있다.

함수의 파라미터
```javascript
const array= max(1,2,3,4);

function max(...rest){
    return Math.max(...rest);
}


console.log(plus(...array));//10
```

객체
```javascript
const student = {
    name: "Hong gildong";
    age: 17;
    num: 18;
}
const {name,age}=student;
console.log(name);//Hong gildong
//객체의 나머지 값 출력
console.log(...rest);//student{age: 17, num: 18}
```

# 구조분해할당
- 구조분해할당은 배열이나 객체의 속성을 나눠 그 값을 개별 변수에 담을 수 있게하는 JS의 표현식이다.

예시
```javascript
const student = {
    name: "Hong gildong";
    age: 17;
    num: 18;
}
```
이 객체에서 name이라는 속성을 변수로 사용하고 싶을 때에 이렇게 선언한다.
```javascript
const name = student.name;
```
하지만 위와 같은 방식이 아닌 더 간단하게 변수명을 앞뒤로 감싼 형식이 있다. 
```javascript
const {name} = student;
```
이러한 형식을 구조분해할당이라고 한다.

하지만 구조분해할당을 사용할 때의 주의점은 변수의 이름은 객체의 속성명과 같아야한다는 점이 있다.

그리고 객체에서 다른 객체로 값을 넘겨줄 때에 
```javascript
const student = {
    name: "Hong gildong";
    age: 17;
}
const person = {
    name: "lee mongryung"
    age: 18;
}
student=person;
```
와 같은 코드에서 자신이 넘겨주고 싶은 속성만 중괄호를 감싸면 그 속성만 선택하여 변수로 선언과 할당을 진행할 수 있다.

배열을 사용한 구조분해할당은 객체의 구조분해할당과 조금의 차이점이 있다.
```javascript
const scores= [81,100,83,78,78];
const [score]= scores;//81
const [score1,score2]= scores;//81,100
```
위의 코드에서 보이듯이 배열의 구조분해할당에서는 중괄호대신 대괄호로 변수명을 감싼다.

그리고 대괄호 안에 선언한 변수만큼 배열에서의 값이 넘어온다.
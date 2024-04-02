# JSON
## 특징
json은 javascript object notation의 약자이다.  
데이터를 쉽게 주고 받을 수 있는 데이터 교환 표준이다.  
간단한 텍스트로 구성되어있다.  
key와 value로 구성되어있다.
```js
  {key:value}
```
데이터 나열 시에는 ,를 사용한다.
```js
{
  key:value,
  k:v
}
```
객체는 {}, 배열은 []이다.
```js
{
  obj:{key:value},
  arr:[value1,value2]
}
```
다양한 데이터 타입을 넣을 수 있다.  

## JSON 메서드
1. JSON.stringify(arg): 객체를 문자열로 변환해주는 메서드이다.
```js
const json = {"key":value};
const str = JSON.stringify(json);//str = '{"key":value}'
console.log(str);//'{"key":value}'
```
2.JSON.parse(arg): JSON 형태의 문자열을 객체로 변환해주는 메서드이다.
```js
const str = '{"key":value}'
const obj = JSON.parse(str);//obj = {"key":value}
console.log(obj);//{"key": value}
```
**주의**: 문자열이 무조건 JSON 형식으로 작성되어 있어야한다.
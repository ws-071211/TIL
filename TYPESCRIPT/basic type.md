# 타입 스크립트의 기본 타입

## 타입 종류
- string
- number
- boolean
- array
- Object
- null & undefined

## string 타입
```typescript
let str1:string = 'string';
let str2:string = "string";
let str3:string = `string`;
```
'',""로 감싼 문자열만 받으며 ``으로 감싼 경우 ${}안에 js의 표현식도 사용할 수 있다.

## number 타입
```typescript
let num1:number = 1;
let num2:number = 1.1;
let num3:number = -1;
```
정수와 실수, 음수를 받을 수 있다.

## boolean
```typescript
let bool:boolean = true;
```
참과 거짓만 받을 수 있다.

## array
```typescript
let arr1:number[] = {1,2,3}
let arr2:string[] = {"밥","빵","면"}
let arr3:any[] = {"밥",1,"빵",2}
let arr4:Array<number> = {1,2,3};
```
각 타입에 맞는 배열을 만들고 배열 안에 타입에 안 맞는 값이 있으면 오류를 띄워준다.   
arr4같은 제네릭 배열타입으로도 사용할 수 있다.   
>### 제네릭 배열 타입을 사용하는 이유?
> ```typescript
>interface user<T>{
>    id:number;
>    name:string;
>    age:number;
>    item:Array<T>;
>}
>
>interface male{
>    discharge:boolean;
>    marry:boolean;
>}    
>interface female{
>    marry:boolean;
>}
>
>function callMaleUser(){
>    let res:user<male>;
>    return res;
>}
>
>function callFemaleUser(){
>    let res:user<female>;
>    return res;
>}
>```
>위와 같은 코드가 있을 때 제네릭 배열을 사용하면 사용할 배열을 유동적으로 지정할 수 있다.

## Object
```typescript
  const user:object = {
        name:"kim dong hak",
        age:16,
        projects:[coding,exercise]
    }
    
```
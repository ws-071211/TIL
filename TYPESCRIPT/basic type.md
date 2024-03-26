# 타입 스크립트의 기본 타입

## 타입 종류
- string
- number
- boolean
- array
- Object
- Tuple
- null & undefined
- any

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
객체의 형태인 타입에만 사용할 수 있다.

## Tuple
```ts
  const user = [name:string, age:number];
```
속성의 타입을 각각 다르게 설정해줄수있다.

## null & undefined
```ts
  const user1:string|undefined = 'name'
  const user2:string|null = 'name'
```
값이 없거나 정의되지않은 경우의 값이 들어갈 수 있다.

## any 
```ts
  const user1:any = 'a';
  const user2:any = 1;
  const user3:any = true;
  const user4:any = null;
  const user5:any = {1,2,3};
  const user6:any = [name: string, age: number];
```
어떤 타입이든지 상관없이 모두 받을 수 있다.
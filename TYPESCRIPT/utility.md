# utility type
utility type은 ts의 문법을 이용하여 만든 함수같은 느낌이다.  
타입 변경을 보다 더 쉽고 용이하게 할 수 있게 도와주는 역할을 한다.  

## `Partial<T>`
T의 속성을 모두 옵셔널로 변경한 타입을 반환한다.  
```ts
interface Student{
  name: String,
  grade: number,
  phone: number
}

const stuName: Partial<Student> = {
  //Student의 속성을 모두 옵셔널로 변경
  name: 'Min'
};
```

## `Required<T>`
T의 속성을 옵셔널에서 필수로 변경한 타입을 반환한다.  
```ts
interface Student{
  name?: String,
  grade?: number,
  phone?: number
}

const studentData: Required<Student> = { 
  //Student의 속성이 모두 옵셔널에서 필수로 변경
  name: 'Min'
};//error

const studentData: Required<Student> = {
  name: 'Min',
  grade: 2,
  phone: 01012341234
};
```

## `Readonly<T>`
T의 속성을 모두 읽기 전용으로 변경한 타입을 반환한다.  
```ts
interface Student{
  name: String,
  grade: number,
  phone: number
}

const studentData: Readonly<Student> = { 
  //Student의 속성을 모두 읽기전용으로 변경
  name: 'Min',
  grade: 2,
  phone: 01012341234
};

student.name = 'kim';//error
```

## `Record<K, T>`
K를 속성으로 하고 T를 타입으로 갖는 타입을 반환한다.
```ts
type Value = {
  name: string;
  value: number
}

type naming = 'item' | 'price';

const sell: Record<Key, number> = {
   item: 'Candy',
   price: 200
};
```

## `Pick<T, K>`
T의 속성 중에 K에 해당하는 속성만 모은 타입을 반환한다.
```ts
type Student = {
  name: string,
  grade: number,
  phone: number,
  email: string
}

type Key = 'name' | 'email';

const sell: Pick<Student, Key> = {
   name: 'Min',
   email: 'test@gmail.com'
};
```

## `Omit<T, K>`
`Pick<T, K>`와 반대로 K를 제외한 T의 속성을 타입으로 반환한다.  
```ts
type Student = {
  name: string,
  grade: number,
  phone: number,
  email: string
}

type Key = 'name' | 'email';

const sell: Pick<Student, Key> = {
   name: 'Min',
   email: 'test@gmail.com'
};
```

## `Exclude<T,U>`
T에서 U를 제외한 타입을 반환한다.
```ts
type T = string | boolean | object | number ;
type R = Exclude<T,string>;
// R = boolean | object | number
```

## `Extract<T,U>`
T와 U의 공통되는 타입을 반환한다.
```ts
type T = string | number ;
type U = string | boolean ;
type R = Extract<T,U> ;
// R = string
```

## `NonNullable<T>`
T에서 null과 undefined을 제외한 타입을 반환한다.
```ts 
type T = string | null | number | undefined ;
type R = NonNullable<T> ;
// R = string | number
```
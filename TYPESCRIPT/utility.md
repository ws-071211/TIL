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

type P = Partial<Student>
//Student의 속성을 모두 옵셔널로 변경

const stuName: Partial<Student> = {
  name: 'Min'//옵셔널로 변경되었기때문에 name 속성만 사용가능
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

type R = Required<Student>
//Student의 속성이 모두 옵셔널에서 필수로 변경

const studentData: Required<Student> = {
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

type Read = Readonly<Student>
//Student의 속성을 모두 읽기전용으로 변경

const studentData: Readonly<Student> = {
  name: 'Min',
  grade: 2,
  phone: 01012341234
};

student.name = 'kim';//error
```


# var,const,let
var,const,let은 모두 js에서 변수를 선언할 때 사용되지만 모두 차이가 존재한다.  
## var
var는 ES6의 등장 이전에 사용되었던 변수 중 하나이다.  
**특징**    
1. var의 생성 순서
    - var는 생성되는 과정에서 선언, 초기화, 할당이 모두 따로 발생한다.  
    그렇기 때문에 호이스팅이 일어나도 오류가 발생하지 않는다.
       ```js
      console.log(v)//undefined
      var v = 'var'
      ```
      호이스팅된 모습
      ```js
      var v
      console.log(v)//undefined
      v = 'var'
      ```
2. 현재 사용되지않는 이유
    - var는 현재 let과 const의 등장 이후에 거의 사용되지 않는데 그 이유 중 1개로 재정의가 가능하다는 점이 있다.  
    - 재정의가 가능한게 문제인 이유는 다음의 예제에서 볼 수 있다.
      ```js
      var v = 0
      function F(){
        var v = 1 
      }
      console.log(v)//1
      ```
      v가 F에서 재정의된 1로 출력된다는 것이 문제점인 이유는 작성자가 만약 다른 위치에서 v라는 이름을 가진 다른 변수가 존재하는 걸 모르고 다시 사용 시 출력되는 값이 변하여 수많은 오류를 발생시킬 수 있기 떄문이다.

## const
ES6 이후에 등장한 변수이다.  
const로 선언된 값은 변하지않는다.
```js
const c = 'as'
c = 'asd'//error
```
그리고 var와 달리 선언과 초기화가 동시에 일어나기 때문에 무조건 const 변수를 사용하는 명령문 위에 선언되어야한다.
```js
console.log(v)//error
const c = 'c'
```

## let
ES6 이후에 등장한 변수이고 const와 달리 값을 재정의할 수 있다.
```js
let c = 'as'
c = 'asd'
console.log(c)//asd
```
그리고 const와 같은 점은 let으로 선언한 변수가 그 변수가 사용되는 명령문 위에 있어야한다.
```js
console.log(v)//error
let c = 'c'
```
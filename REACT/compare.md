# 얕은 비교/깊은 비교

## 얕은 비교
숫자, 문자열 등 원시 자료형은 값을 비교한다.  
하지만 배열이나 객체의 경우 들어있는 값이 아닌 참조값을 비교한다.  

```
const object1 = { a: 1, b: 2 };
const object2 = { a: 1, b: 2 };

console.log(object1 === object2); // false
```
객체의 내부값은 같은데 참조값이 다르기 때문에 false가 반환됩니다.
그렇기때문에 객체state를 props로 사용하게 될 경우 재렌더링이 발생한다.


## 깊은 비교
 얕은 비교와 달리 깊은 비교는 객체의 경우에도 값으로 비교한다.
 ```
 const object1 = { a: 1, b: 2 };
const object2 = { a: 1, b: 2 };

console.log(object1 === object2); // true
 ```
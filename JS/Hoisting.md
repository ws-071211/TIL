# 호이스팅
선언한 변수나 함수를 각 스코프의 최상단으로 끌어올리는 JS의 특징

## 호이스팅의 발생 이유
JS에서의 변수는 생성과 초기화,할당이 각각 따로 진행되기 때문이다.
>변수는 var만 호이스팅 대상이다.

호이스팅
```js
  console.log(a);//a
  console.log(b);//error
  console.log(c);//error

  function a(){
    return 'a';
  }
  var b = function d(){
    return 'd';
  };
  var c = function() {
    return 'c';
  };
```

호이스팅된 모습
```js
  function a() {
    return 'a';
  }
  var b;
  var c; 

  console.log(a());
  console.log(b());
  console.log(c());
  
  b = function bb() {
      return 'bb';
  }
  c = function() {
      return 'c';
  }
```
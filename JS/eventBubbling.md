# 이벤트 버블링   
이벤트가 발생한 요소부터 점점 부모 요소로 올라가 최상위 요소까지 이벤트를 전파하는 것   

```html
<div class='one'  onclick='alert(this.className)'>
  <div class='two'  onclick='alert(this.className)'>
    <div class ='three' onclick='alert(this.className)'>
      three
    </div>
  </div>
</div>
```
1. 클래스가 three인 div가 클릭되었으면 그 div의 onclick 핸들러가 동작한다.
2. 그리고 부모 요소인 클래스 two인 div의 onclick 핸들러가 동작한다.
3. 그리고 이어서 클래스 one인 div의 onclick 핸들러까지 동작한다.

## 이벤트 버블링을 멈추는 법
이벤트 객체의 메서드인 event.stopPropagation()를 사용하면 된다.
```html
<div class='one'  onclick='alert(this.className)'>
  <div class='two'  onclick='alert(this.className); event.Propagation()'>
    <div class ='three' onclick='alert(this.className)'>
      three
    </div>
  </div>
</div>
```
이러면 클래스 two인 div까지만 실행되고 클래스가 one인 div부터는 실행되지 않는다.
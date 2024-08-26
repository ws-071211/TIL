# Object vs object

typescript에는 객체 타입을 설정하는 타입이 Object와 object가 있다.  
두 가지 타입에는 무슨 차이가 있을까?

## Object

- null과 undefined를 제외한 모든 원시값을 받을 수 있다.
- 위의 사실을 모르는 경우도 있기에 가독성을 위해 eslint의 일부 설정에서는 Object 대신 다른 타입을 사용하라는 문구가 발생한다.
- `NonNullable<object>`로 작성하기를 권장한다.

## object

- 원시값을 제외한 객체값을 받을 수 있다.
- Object보다 더 엄격한 타입이라고 볼 수 있다.
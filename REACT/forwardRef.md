# forwardRef

react에는 ref라고 하는 HTML 엘리먼트에 직접적으로 접근하기 위해서 사용되는 props가 있다.
하지만 함수형 컴포넌트에는 인스턴스가 없어서 직접 ref를 사용할 수 없지만 forwardRef로 부모 컴포넌트에서 자식 컴포넌트의 DOM으로 ref를 전달할 수 있게 되었다.

## 사용예시

```tsx
const Input = forwardRef(({type,placeholder, onChange,...props},ref)) => {
  return(
    <div ref={ref}>
      <input
        type={type}
        placeholder={placeholder}
        onChange={(e)=>onChange?.(e)}
      />
    </div>
  )
}
```

## 장점

- DOM 접근
  - 부모 컴포넌트에서 자식 컴포넌트의 DOM에 직접 접근이 가능해져 여러 작업들에 유용하다.

- 재사용성
  - 자식 컴포넌트에 DOM에 직접적인 접근이 가능해져 재사용성이 높아진다.

- 캡슐화
  - forwardRef의 사용으로 Ref의 세부적인 구현 사항을 숨기고 필요한 부분만 외부로 보여줄 수 있다.

## 단점

- 의존성 증가
  - 부모 컴포넌트에서 자식 컴포넌트의 DOM에 직접 접근이 가능하게 되어 서로 간의 결합도를 높여 의존성이 증가할 수 있다.

- 성능 저하
  - 불필요하게 많이 남용되는 경우 코드를 복잡하게 만들고 이를 통한 많은 ref 전달은 성능 저하를 야기할 수 있게 된다. 그래서 많은 컴포넌트가 동시에 렌더링될 경우 주의가 필요하다.

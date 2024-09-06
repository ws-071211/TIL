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
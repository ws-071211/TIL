# recoil

react의 상태관리 라이브러리이다.  
react는 단방향 데이터 흐름을 따르기 때문에 하위 컴포넌트의 상태를 다른 컴포넌트에서 사용하기 위해서는 상태를 상위 컴포넌트로 끌어올려서 사용하거나 redux와 같은 전역 상태 관리 라이브러리를 사용해야했다.
하지만 recoil을 사용하면 기존 react 컴포넌트 내에서 상태를 관리할 수 있다.

## 특징

1. 데이터 흐름 그래프
    - recoil은 상태와 파생 상태를 관리하기 위해 데이터 흐름 그래프를 사용하는데 이를 토애헛 상태 간의 의존성 관리가 효율적이다.
2. 비동기 처리
   - recoil은 비동기 관련 작업의 수행이 편하다. 그 이유는 Promise나 async/await를 사용하여 비동기 처리를 할 수 있으며, 상태 변화를 감지하여 자동으로 컴포넌트를 업데이트하기 때문이다.
3. 상태 변경 관리
    - recoil은 상태를 구독하여 상태의 변경을 감지하고 상태가 변경되었을 때만 관련 컴포넌트를 업데이트하여 불필요한 렌더링을 줄여 성능을 최적화할 수 있다.
4. 유연한 상태 관리
    - 상태를 atom과 selector로 관리하는데 atom은 상태의 기본 단위이고, selector는 파생 상태를 계산할 떄 사용된다.

## 사용

```
// npm 
npm i recoil
// yarn 
yarn add recoil
```

### RecoilRoot

redux의 Provider를 사용하는 식으로 사용해주면 된다.
루트에 RecoilRoot를 감싸서 사용해준다.

```tsx
import Layout from '@/layout';
import '@/styles/globals.css';
import type { AppProps } from 'next/app';
import { RecoilRoot } from 'recoil';

export default function App({ Component, pageProps }: AppProps) {
  return (
    <RecoilRoot>
      <Layout>
        <Component {...pageProps} />
      </Layout>
    </RecoilRoot>
  );
}
```

### atoms

recoil에서의 상태 단위이다.  
atom의 값이 변경될 시 해당 atom을 구독해놓은 모든 컴포넌트가 리렌더링된다.

```tsx
import { atom } from "recoil";

export const userDataState = atom<UserDataType>({
  key: 'userData',
  default: {},
})
```

### useRecoilState()

atom의 상태를 사용하고 변경할 수 있다.
useState와 활용법이 비슷하며 `userData`는 userDataState의 상태를 가지고 `setUserData`는 `userData`의 값을 변경할 수 있는 setter함수를 가지게 된다.

```tsx
import { useRecoilState } from 'recoil';
import { userDataState } from '@/recoil/atoms/atoms';

const Mypage = () => {
  const [userData,setUserData] = useRecoilState(userDataState);
  // 생략
  useEffect(()=>{
    axios.get(url)
      .then((res)=>
        setUserData(res.data);
      )
      .catch((error)=>
        console.log(error);
      )
  },[])
  
  return(
    <S.WelcomeContainer>
      <S.WelcomeText>안녕하세요</S.WelcomeText>
      <S.UserNameText>
        <span>{userData?.name}</span>님
      </S.UserNameText>
    </S.WelcomeContainer>
  )
}
```

### useRecoilValue()

atom의 상태를 읽기 전용으로 받아올 수 있다.

```tsx
import { useRecoilState } from 'recoil';
import { userDataState } from '@/recoil/atoms/atoms';

const Mypage = () => {
  const userData = useRecoilState(userDataState);
  
  return(
    <S.WelcomeContainer>
      <S.WelcomeText>안녕하세요</S.WelcomeText>
      <S.UserNameText>
        <span>{userData?.name}</span>님
      </S.UserNameText>
    </S.WelcomeContainer>
  )
}
```

### useSetRecoilState()

atom의 상태를 변경하기 위한 setter 함수를 받아올 수 있다.

```tsx
const Mypage = () => {
  const setUserData = useSetRecoilState(userDataState);
  // 생략
  useEffect(()=>{
    axios.get(url)
      .then((res)=>
        setUserData(res.data);
      )
      .catch((error)=>
        console.log(error);
      )
  },[])
}
```

>**useRecoilValue()와 useSetRecoilState()를 왜 사용할까??**  
useRecoilState()는 atom의 상태와 setter 함수를 모두 받을 수 있는데 왜 굳이 useRecoilValue()와 useSetRecoilState()를 사용할까?  
useREcoilValue()와 useSetRecoilState()는 각각 atom의 상태 읽기와 atom의 값 변경을 위한 setter 함수의 기능만을 가지고 있는데 useRecoilState는 모든 기능을 가지고 있어 값만 읽는 용도로 사용하더라도 모든 기능을 가지고 있어 성능적으로 useRecoilValue()보다 떨어질 수 밖에 없다. useSetRecoilState()도 마찬가지다.

### useResetRecoilState()

atom의 값을 각 atom의 default로 초기화해준다.


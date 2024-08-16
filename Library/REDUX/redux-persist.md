# redux-persist

redux의 상태를 새로고침이나 세션 종료 후에도 유지하기 위한 라이브러리이다.

## 원리

상태를 로컬 스토리지에 저장하여 상태를 새로고침이나 세션 종료 후에도 유지할 수 있다.

## 사용

설치

```
// npm
npm i redux-persist
// yarn 
yarn add redux-persist
```

설정

```js
// 생략
const rootReducer = combineReducers({
  user: userSlice.reducer,
});

const persistConfig = {
  key: 'root',
  storage,
};

const persistedReducer = persistReducer(persistConfig, rootReducer);
// 생략
export type RootState = ReturnType<typeof rootReducer> & { _persist: any };

```

적용

```js
import { ToastContainer } from 'react-toastify';
import type { AppProps } from 'next/app';
import Layout from '../layout';
import '../styles/globals.css';
import 'react-toastify/dist/ReactToastify.css';
import { Provider } from 'react-redux';
import { PersistGate } from 'redux-persist/integration/react';
import wrapper, { persistor } from '@/store';


export default function App({ Component, ...pageProps }: AppProps) {
  const { store, props } = wrapper.useWrappedStore(pageProps);

  return (
    <Provider store={store}>
      <PersistGate loading={null} persistor={persistor}>
        <Layout>
          <Component {...props.pageProps} />
        </Layout>
        <ToastContainer/>
      </PersistGate>
    </Provider>
  );
}

```

# react-query

fetching,caching,서버 데이터와의 동기화를 지원해주는 라이브러리이다.  

서버 상태와 클라이언트 상태를 분리해서 관리할 수 있어 직관적이고 효율적이다.  
서버 상태를 받아와 데이터를 갱신해줄 수 있다.  
캐싱을 이용하여 서버에 불필요한 요청을 줄일 수 있다.  
그리고 에러 처리, 로딩, 캐싱 등의 다양한 불편했던 작업들을 선언적으로 간편하게 사용할 수 있다.  

## caching

데이터 캐싱을 통해 동일한 데이터에 대한 비동기 호출을 방지할 수 있다.  
데이터 재갱신 시도가 발생하는 상황은 다음과 같다.

```
1. 화면을 보고 있을 때
2. 페이지 전환이 발생했을 때
3. 페이지 전환없이 데이터 요청이 발생했을 때
```

그리고 react-query에서는 다음과 같은 기본 옵션들을 제공한다.

```
refetchOnWindowFocus, //기본값: true
refetchOnMount, //기본값: true
refetchOnReconnect, //기본값: true
staleTime,  //기본값: 0
cacheTime //기본값: 5분 (60 * 5 * 1000)
```

- refetchOnWindowFocus: 브라우저가 포커스되었을 때
- refetchOnMount: 새로운 컴포넌트가 마운트 되었을 때
- refetchOnReconnect: 네트워크 재연결 발생했을 때
- staleTime
  - 데이터가 fresh에서 stale로 변화하는 시간
  > fresh: 최신 데이터  
  > stale: 기존 데이터
  - fresh 상태일 경우는 refetch의 상황이 발생해도 refetch가 일어나지 않지만 기본값이 0이므로 설정을 해주지 않는다면 refetch의 경우네 refetch가 발생한다.
- cacheTime
  - 데이터가 비활성 상태(inactive)일 때 캐싱된 상태로 남아있는 시간
  - 컴포넌트가 unmount되었을 때 사용되었던 데이터가 비활성 상태(inactive)로 바뀌는데 이 데이터가 cacheTime으로 설정한 시간만큼 유지된다.
  - cacheTime 이후에는 garbage collector에 수집되어 메모리에서 해제된다.
  - cacheTime이 다 지나기 전에 다시 mount된다면 새 데이터를 fetch해오는 동안에 캐싱되어있는 데이터를 임시로 보여준다.

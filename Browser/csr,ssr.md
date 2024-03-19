# CSR/SSR
## CSR이란?
(client side rendering)   
클라이언트에서 렌더링이 일어나는 것   
서버에서 HTML, JS를 보내주면 클라이언트에서 렌더링을 하는 것     
user가 web에 요청을 보내고 서버가 요청을 받으면 클라이언트에게 html과 js를 보내주고 그것을 클라이언트가 렌더링한다. 처음 html을 빈 화면으로 받고 
## SSR이란?
(server side rendering)   
서버에서 렌더링이 일어나는 것   

## SSR과 CSR의 차이
user에게 보이기까지 걸리는 시간   
CSR은 클라이언트에서 모든 작업을 마무리한 뒤 user에게 노출시키기 떄문에 작업이 끝나기 전까지는 user는 아무것도 보지 못한다.
SSR은 서버에서 작업을 해서 보여주기 때문에 user에게 보여지면서 렌더링도 진행된다. 
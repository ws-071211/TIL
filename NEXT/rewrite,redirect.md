# rewrite, redirect
두 기능은 모두 유저가 특정 경로로 이동할 시 보여지게 설정된 화면을 보이게 하는 기능이다.
## 차이점?
redirect는 유저가 이동한 경로를 바로 URL에 보여준다는 특징이 있다.  
하지만 rewrite는 유저가 이동한 경로가 아니라 보여지게 설정된 경로로 설정해 URL에 자신이 설정한 경로로 보여줄 수 있다.  
rewrite를 사용할 경우 원래 노출되었던 API key와 같은 정보를 숨길 수 있다는 장점이 있다.
## 사용법
next에서는 next.config.js에서 설정하여 사용할 수 있다.
- redirect
```js
/** @type {import('next').NextConfig} */
const nextConfig = {
  async redirects() {
    return [
      {
        source: "/contact",
        destination: "/form",
        permanent: false
      }
    ]
  }
}

module.exports = nextConfig
```
- rewrite
```js
/** @type {import('next').NextConfig} */
const API_KEY = "~~~";

const nextConfig = {
  async rewrites() {
    return [
      {
        source: "/api/movies",
        destination: `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}`,
      },
    ];
  },
};

module.exports = nextConfig
```


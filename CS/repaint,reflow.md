# reflow
reflow는 브라우저 렌더링 과정 중에 요소를 배치하는 layout을 다시하는 것을 의미한다.  
이러한 reflow가 발생하는 대표적인 경우는
- DOM의 추가와 제거
- DOM의 위치변경
- DOM 및 이미지의 크기 변경(width,height 등)
- CSS의 애니메이션과 트랜지션
- 폰트 및 내용 변경
- 페이지 초기 렌더링
- 리사이징

등이 있다

# repaint
repaint는 브라우저 렌더링 과정 중에 요소의 시각적인 스타일을 변경하는 paint를 다시하는 것을 의미한다. 레이아웃에 영향을 주지 않는 개별적인 요소의 변경에서 repaint만 발생한다.  
paint과정은 layout 다음에 일어나는 과정이라서 reflow가 발생하면 repaint도 같이 발생한다.  
때문에 reflow가 repaint보다 비용 발생이 커 reflow를 줄일수록 성능 측면에 좋다.

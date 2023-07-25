import pygame # 1. pygame 선언
from datetime import datetime
from datetime import timedelta
import random     

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
size = [400, 400]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()
last_moved_time = datetime.now()

KEY_DIRECTION = {
    pygame.K_UP: 'W',
    pygame.K_DOWN: 'E',
    pygame.K_LEFT: 'N',
    pygame.K_RIGHT: 'S', 
}

def draw_block(screen, color, position):
    block = pygame.Rect((position[0] * 20, position[1] * 20), (20, 20))
    pygame.draw.rect(screen, color, block)

class Snake:
    def __init__(self):
        self.positions = [(2, 0), (1, 0), (0, 0)]  # 뱀의 위치, (2,0이 머리)
        self.direction = ''

    def draw(self):
        for position in self.positions: 
            draw_block(screen, GREEN, position)

    def move(self):
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'N':
            self.positions = [(y - 1, x)] + self.positions[:-1]
        elif self.direction == 'S':
            self.positions = [(y + 1, x)] + self.positions[:-1]
        elif self.direction == 'W':
            self.positions = [(y, x - 1)] + self.positions[:-1]
        elif self.direction == 'E':
            self.positions = [(y, x + 1)] + self.positions[:-1]

    def grow(self):
        tail_position = self.positions[-1]
        x, y = tail_position
        if self.direction == 'N':
            self.positions.append((x, y - 1)) 
        elif self.direction == 'S':
            self.positions.append((x, y + 1))
        elif self.direction == 'W':
            self.positions.append((x - 1, y))
        elif self.direction == 'E':
            self.positions.append((x + 1, y))   

class Apple:
    def __init__(self, position=(5, 5)):
        self.position = position

    def draw(self):
        draw_block(screen, RED, self.position)

# 4. pygame 무한루프
def runGame():
    global done, last_moved_time
    # 게임 시작 시, 뱀과 사과를 초기화
    snake = Snake() 
    apple = Apple()
    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key in KEY_DIRECTION:
                    snake.direction = KEY_DIRECTION[event.key]

        if timedelta(seconds=0.1) <= datetime.now() - last_moved_time:
            snake.move()

            # 뱀의 머리와 사과의 위치가 충돌하는지 확인
            if snake.positions[0] == apple.position:
                snake.grow()
                apple.position = (random.randint(0, 19), random.randint(0, 19))

            # 뱀이 화면 밖으로 나가지 않도록 처리
            head_x, head_y = snake.positions[0]
            if head_x < 0 or head_x >= 20 or head_y < 0 or head_y >= 20:
                done = True

            last_moved_time = datetime.now()

        snake.draw()
        apple.draw()
        pygame.display.update()

runGame()
pygame.quit()
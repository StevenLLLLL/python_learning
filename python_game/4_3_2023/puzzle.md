# This is a puzzle game made by pygame. 
```python
import pygame

pygame.init()
pygame.key.set_repeat(10)
sc = pygame.display.set_mode((500, 500))
bg2 = pygame.image.load("4_3_2023_bg1.jpg")
bg3 = pygame.image.load("4_3_2023_bg2.jpg")
bg1 = pygame.image.load("4_3_2023_bg3.jpg")
bg_list = [bg1, bg2, bg3]
level = 0
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)


def detect(x, y):
    if sc.get_at((x - 8, y)) != white:
        return sc.get_at((x - 8, y))
    if sc.get_at((x + 8, y)) != white:
        return sc.get_at((x + 8, y))
    if sc.get_at((x, y-8)) != white:
        sc.get_at((x, y-8))
    if sc.get_at((x, y+8)) != white:
        return sc.get_at((x, y+6))


class Ball:
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size

    def draw_ball(self):
        pygame.draw.circle(sc, self.color, (self.x, self.y), self.size)

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def reset(self):
        self.x = 250
        self.y = 30


ball = Ball(250, 30, red, 6)

while True:
    sc.blit(bg_list[level], (0, 0))
    ball.draw_ball()
    color = detect(ball.x, ball.y)
    if color == black:
        ball.reset()
    if color == green:
        if level == 2:
            print("win")
            pygame.quit()
        else:
            level += 1
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball.move_left()
            if event.key == pygame.K_RIGHT:
                ball.move_right()
            if event.key == pygame.K_UP:
                ball.move_up()
            if event.key == pygame.K_DOWN:
                ball.move_down()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
```

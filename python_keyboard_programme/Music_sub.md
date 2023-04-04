## This programme is that I want to put it in to my main programme , so that when I click start, the main programme will begin, and when I am using my keyboard the sound whill going to play. It is also not finished. 
```python 
import pygame
import random

pygame.init()
pygame.mixer.init()
screen_info_1 = pygame.display.Info()
sc_width = screen_info_1.current_w
sc_height = screen_info_1.current_h
sc = pygame.display.set_mode((sc_width, sc_height))
pygame.display.update()
bg_pos_w = (sc_width - 750) / 2
bg_pos_h = (sc_height - 750) / 2

image_gif = pygame.image.load("music_moving.gif")
image_pause = pygame.image.load("pause1.png")
image_next = pygame.image.load("next1.png")
image_pre = pygame.image.load("pre1.png")
clock_music = pygame.time.Clock()
fps = 60
while True:
    pygame.draw.rect(sc, (255, 255, 255), (0, 0, sc_width, sc_height))
    sc.blit(image_gif, (bg_pos_w, bg_pos_h - 100))
    sc.blit(image_pause, ((sc_width - 100) / 2, (sc_height - 240) / 2 + 400))
    sc.blit(image_next, ((sc_width - 100) / 2 + 300, (sc_height - 240) / 2 + 400))
    sc.blit(image_pre, ((sc_width - 100) / 2 - 300, (sc_height - 240) / 2 + 400))
    pygame.display.flip()
    clock_music.tick(fps)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            temp_1, temp_2 = pygame.mouse.get_pos()
            if temp_1 < (sc_width - 100) / 2 and temp_1 < sc_width / 2 and temp_2 < (
                    sc_height - 240) / 2 + 400 and temp_2 < (sc_height - 240) / 2 + 500:
                pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

# This is a programme that can help me figure out the position of my mouse. 
```python
import pygame
pygame.init()

screen_info = pygame.display.Info()
sc_width = screen_info.current_w
sc_height = screen_info.current_h
bg_pos_w = (sc_width - 830)/2
bg_pos_h = (sc_height - 466)/2
sc = pygame.display.set_mode((sc_width, sc_height))

pygame.mixer.set_num_channels(27)
bg = pygame.image.load("keyboard_pic.png")

while True:
    sc.blit(bg, (bg_pos_w, bg_pos_h))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
```
#### It will print the position of my mouse after I click my mouse. 

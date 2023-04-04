# This is just part of the programme, I met some problems and need to fix them. 
## The problems is about how to use pynput, and how to send variebles into the function.
```python
import pygame
import random
import sys
from pynput import keyboard
from pynput.keyboard import Listener

pygame.init()
pygame.mixer.init()

screen_info = pygame.display.Info()
sc_width = screen_info.current_w
sc_height = screen_info.current_h
bg_pos_w = (sc_width - 830) / 2
bg_pos_h = (sc_height - 466) / 2
sc = pygame.display.set_mode((sc_width, sc_height))

pygame.mixer.set_num_channels(27)
bg = pygame.image.load("keyboard_pic.png")
s1 = "dog_1.mp3"
s2 = "dog_2.mp3"
s3 = "linhua_1.mp3"
s4 = "linhua_2.mp3"
s5 = "linhua_3.mp3"
s6 = "linhua_4.mp3"
s7 = "linhua_5.mp3"
s8 = "linhua_6.mp3"
s9 = "linhua_7.mp3"
s10 = "nahida_1.mp3"
s11 = "nahida_2.mp3"
s12 = "nahida_3.mp3"

sound_list = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12]
l1 = []
for i in sound_list:
    l1.append(pygame.mixer.Sound(i))
c1 = pygame.mixer.Channel(0)
c2 = pygame.mixer.Channel(1)
c3 = pygame.mixer.Channel(2)
c4 = pygame.mixer.Channel(3)
c5 = pygame.mixer.Channel(4)
c6 = pygame.mixer.Channel(5)
c7 = pygame.mixer.Channel(6)
c8 = pygame.mixer.Channel(7)
c9 = pygame.mixer.Channel(8)
c10 = pygame.mixer.Channel(9)
c11 = pygame.mixer.Channel(10)
c12 = pygame.mixer.Channel(11)
c13 = pygame.mixer.Channel(12)
c14 = pygame.mixer.Channel(13)
c15 = pygame.mixer.Channel(14)
c16 = pygame.mixer.Channel(15)
c17 = pygame.mixer.Channel(16)
c18 = pygame.mixer.Channel(17)
c19 = pygame.mixer.Channel(18)
c20 = pygame.mixer.Channel(19)
c21 = pygame.mixer.Channel(20)
c22 = pygame.mixer.Channel(21)
c23 = pygame.mixer.Channel(22)
c24 = pygame.mixer.Channel(23)
c25 = pygame.mixer.Channel(24)
c26 = pygame.mixer.Channel(25)
c27 = pygame.mixer.Channel(26)

current_audio = None


def on_press(key, current_audio):
    try:
        if key.char == 'q':
            c1.play(current_audio)
        elif key.char == 'w':
            c2.play(current_audio)
        elif key.char == 'e':
            c3.play(current_audio)
        elif key.char == 'r':
            c4.play(current_audio)
        elif key.char == 't':
            c5.play(current_audio)
        elif key.char == 'y':
            c6.play(current_audio)
        elif key.char == 'u':
            c7.play(current_audio)
        elif key.char == 'i':
            c8.play(current_audio)
        elif key.char == 'o':
            c9.play(current_audio)
        elif key.char == 'p':
            c10.play(current_audio)
        elif key.char == 'a':
            c11.play(current_audio)
        elif key.char == 's':
            c12.play(current_audio)
        elif key.char == 'd':
            c13.play(current_audio)
        elif key.char == 'f':
            c14.play(current_audio)
        elif key.char == 'g':
            c15.play(current_audio)
        elif key.char == 'h':
            c16.play(current_audio)
        elif key.char == 'j':
            c26.play(current_audio)
        elif key.char == 'k':
            c17.play(current_audio)
        elif key.char == 'l':
            c18.play(current_audio)
        elif key.char == 'z':
            c19.play(current_audio)
        elif key.char == 'x':
            c20.play(current_audio)
        elif key.char == 'c':
            c21.play(current_audio)
        elif key.char == 'v':
            c22.play(current_audio)
        elif key.char == 'b':
            c23.play(current_audio)
        elif key.char == 'n':
            c24.play(current_audio)
        elif key.char == 'm':
            c25.play(current_audio)
        elif key.char == 'm' and key.char == 'a':
            c25.play(current_audio)

    except AttributeError:
        pass


def on_release(key):
    pass
```
## The problem starts from here
### The code below can't be ran. 
```python
sc.blit(bg, (bg_pos_w, bg_pos_h))
pygame.display.update()
with keyboard.Listener(on_press=on_press, args=current_audio, on_release=on_release) as listener:
    while True:
        num_audio = random.choice(l1)
        current_audio = num_audio
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        listener.join(0.1)
```    

import easygui as g
import pygame
import random
import sys
from pynput import keyboard

pygame.init()
pygame.mixer.init()
screen_info = pygame.display.Info()
sc_width = screen_info.current_w
sc_height = screen_info.current_h
bg_pos_w = (sc_width - 1400) / 2
bg_pos_h = (sc_width - 502) / 2
set_pos_w = (sc_width - 1000) / 2
set_pos_h = (sc_height - 1000) / 2
sc = pygame.display.set_mode((sc_width, sc_width))

pygame.mixer.set_num_channels(59)
bg = pygame.image.load("keyboard_pic.png")
sw_pic = pygame.image.load("pause1.png")
heart = pygame.image.load("heart.png")
setting = pygame.image.load("setting.png")
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
c28 = pygame.mixer.Channel(27)
c29 = pygame.mixer.Channel(28)
c30 = pygame.mixer.Channel(29)
c31 = pygame.mixer.Channel(30)
c32 = pygame.mixer.Channel(31)
c33 = pygame.mixer.Channel(32)
c34 = pygame.mixer.Channel(33)
c35 = pygame.mixer.Channel(34)
c36 = pygame.mixer.Channel(35)
c37 = pygame.mixer.Channel(36)
c38 = pygame.mixer.Channel(37)
c39 = pygame.mixer.Channel(38)
c40 = pygame.mixer.Channel(39)
c41 = pygame.mixer.Channel(40)
c42 = pygame.mixer.Channel(41)
c43 = pygame.mixer.Channel(42)
c44 = pygame.mixer.Channel(43)
c45 = pygame.mixer.Channel(44)
c46 = pygame.mixer.Channel(45)
c47 = pygame.mixer.Channel(46)
c48 = pygame.mixer.Channel(47)
c49 = pygame.mixer.Channel(48)
c50 = pygame.mixer.Channel(49)
c51 = pygame.mixer.Channel(50)
c52 = pygame.mixer.Channel(51)
c53 = pygame.mixer.Channel(52)
c54 = pygame.mixer.Channel(53)
c55 = pygame.mixer.Channel(54)
c56 = pygame.mixer.Channel(55)
c57 = pygame.mixer.Channel(56)
c58 = pygame.mixer.Channel(57)
c59 = pygame.mixer.Channel(58)

channel_list = [c1,
                c2,
                c3,
                c4,
                c5,
                c6,
                c7,
                c8,
                c9,
                c10,
                c11,
                c12,
                c13,
                c14,
                c15,
                c16,
                c17,
                c18,
                c19,
                c20,
                c21,
                c22,
                c23,
                c24,
                c25,
                c26,
                c27,
                c28,
                c29,
                c30,
                c31,
                c32,
                c33,
                c34,
                c35,
                c36,
                c37,
                c38,
                c39,
                c40,
                c41,
                c42,
                c43,
                c44,
                c45,
                c46,
                c47,
                c48,
                c49,
                c50,
                c51,
                c52,
                c53,
                c54,
                c55,
                c56,
                c57,
                c58,
                c59, ]

temp = True


def on_press(key):
    num_audio = random.choice(l1)
    current_audio = num_audio
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

    except AttributeError:
        pass


def on_release(key):
    pass


switch = 0
switch_pos = ((sc_width / 2) - 105, sc_height + 200)

num_audio = random.choice(l1)
current_audio = num_audio
sc.blit(bg, (bg_pos_w, bg_pos_h))
pygame.display.update()
pos_x = 0
pos_y = 0
red = (255, 0, 0)
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

sw_pause = False

while temp:
    sc.fill((0, 0, 0))
    num_audio = random.choice(l1)
    current_audio = num_audio
    sc.blit(bg, (bg_pos_w, bg_pos_h))
    sc.blit(sw_pic, switch_pos)
    sc.blit(heart, (pos_x - 25, pos_y - 18))
    sc.blit(setting, (sc_width / 2, sc_height + 200))
    # pygame.draw.rect(sc, red, (sc_width/2, 0, 3, sc_height*2))
    set_sw = True
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            pos_x, pos_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_1, y_1 = pygame.mouse.get_pos()
            if (sc_width / 2) - 105 < x_1 < (sc_width / 2) - 5 and (sc_height + 200) < y_1 < (sc_height + 300):
                if not sw_pause:
                    for set_v in channel_list:
                        set_v.set_volume(0.0001)
                    sw_pause = True
                else:
                    for set_v in channel_list:
                        set_v.set_volume(0.5)
                    sw_pause = False
            if sc_width / 2 < x_1 < sc_width / 2 + 100 and sc_height + 200 < y_1 < sc_height + 300:
                set_volume = g.enterbox(msg="请输入0-1之间的小数", title="音量设置")
                a = float(set_volume)
                if 0 < a < 1:
                    for set_v in channel_list:
                        set_v.set_volume(a)
                else:
                    continue
        if event.type == pygame.QUIT:
            listener.stop()
            temp = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                listener.stop()
                temp = False
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                c26.play(current_audio)
            if event.key == pygame.K_TAB:
                c27.play(current_audio)
            if event.mod & pygame.KMOD_ALT:
                c28.play(current_audio)
            if event.mod & pygame.KMOD_CTRL:
                c29.play(current_audio)
            if event.mod & pygame.KMOD_CAPS:
                c30.play(current_audio)
            if event.mod & pygame.KMOD_SHIFT:
                c31.play(current_audio)
            if event.mod & pygame.KMOD_CAPS:
                c32.play(current_audio)
            if event.key == pygame.K_1:
                c33.play(current_audio)
            if event.key == pygame.K_2:
                c34.play(current_audio)
            if event.key == pygame.K_3:
                c35.play(current_audio)
            if event.key == pygame.K_4:
                c36.play(current_audio)
            if event.key == pygame.K_5:
                c37.play(current_audio)
            if event.key == pygame.K_6:
                c38.play(current_audio)
            if event.key == pygame.K_7:
                c39.play(current_audio)
            if event.key == pygame.K_8:
                c40.play(current_audio)
            if event.key == pygame.K_9:
                c41.play(current_audio)
            if event.key == pygame.K_0:
                c42.play(current_audio)
            if event.key == pygame.K_F1:
                c43.play(current_audio)
            if event.key == pygame.K_F2:
                c44.play(current_audio)
            if event.key == pygame.K_F3:
                c45.play(current_audio)
            if event.key == pygame.K_F4:
                c46.play(current_audio)
            if event.key == pygame.K_F5:
                c47.play(current_audio)
            if event.key == pygame.K_F6:
                c48.play(current_audio)
            if event.key == pygame.K_F7:
                c49.play(current_audio)
            if event.key == pygame.K_F8:
                c50.play(current_audio)
            if event.key == pygame.K_F9:
                c51.play(current_audio)
            if event.key == pygame.K_F10:
                c52.play(current_audio)
            if event.key == pygame.K_F11:
                c53.play(current_audio)
            if event.key == pygame.K_F12:
                c54.play(current_audio)
            if event.key == pygame.K_LEFT:
                c55.play(current_audio)
            if event.key == pygame.K_UP:
                c56.play(current_audio)
            if event.key == pygame.K_DOWN:
                c57.play(current_audio)
            if event.key == pygame.K_RIGHT:
                c58.play(current_audio)

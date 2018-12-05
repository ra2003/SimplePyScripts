#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# pip install pygame
import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN

FPS = 60
W = 700  # ширина экрана
H = 300  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# координаты и радиус круга
x = W // 2
y = H // 2
r = 50

step = 4

game_active = True

while True:
    for event in pygame.event.get():  # получение всех событий
        if event.type == pygame.QUIT:  # проверка события "Выход"
            game_active = False
            break

    if not game_active:
        break

    sc.fill(WHITE)

    pygame.draw.circle(sc, BLUE, (x, y), r)

    pygame.display.update()

    is_pressed = pygame.key.get_pressed()

    if is_pressed[K_LEFT]:
        x -= step

    if is_pressed[K_RIGHT]:
        x += step

    if is_pressed[K_UP]:
        y -= step

    if is_pressed[K_DOWN]:
        y += step

    pygame.display.set_caption("move_rect [{} fps]".format(int(clock.get_fps())))

    clock.tick(FPS)
    pygame.event.pump()

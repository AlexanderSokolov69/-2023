#!/usr/bin/env python3
# coding:utf-8
import pygame
from pygame.locals import *


pygame.init()

dis = pygame.display.set_mode((500, 400))
pygame.display.update()

pygame.display.set_caption('Змейка от Skillbox')  # Добавляем название игры.

pygame.display.update()

game_over = False
mod = pygame.draw.rect(dis, "green", (20, 20, 30, 30))
while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True
        print(event)

pygame.quit()
quit()

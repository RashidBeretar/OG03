from random import random

import pygame
from pygame.examples.go_over_there import screen

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра Тир')
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

target1_img = pygame.image.load("img/target1.png")
target2_img = pygame.image.load("img/target2.png")
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    pass

pygame.quit()
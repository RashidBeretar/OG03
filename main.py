import pygame
import random
# from pygame.examples.go_over_there import screen

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

hits_cnt = 0
target_cnt = 0
target_lives_cnt = 4

pygame.display.set_caption('Игра Тир')
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target1.png")
# target1_img = pygame.image.load("img/target1.png")
# target2_img = pygame.image.load("img/target2.png")
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

font = pygame.font.SysFont('Arial', 22)
hits_text = font.render(f'Попаданий: {hits_cnt}', True, (255, 255, 255))  # Белый цвет
target_text = font.render(f'Разбитых мишеней: {target_cnt}', True, (255, 255, 255))  # Белый цвет

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

                hits_cnt += 1
                target_cnt = hits_cnt // target_lives_cnt
                state_number = hits_cnt % target_lives_cnt + 1

                hits_text = font.render(f'Попаданий: {hits_cnt}', True, (255, 255, 255))  # Белый цвет
                target_text = font.render(f'Разбитых мишеней: {target_cnt}', True, (255, 255, 255))  # Белый цвет

                target_img = pygame.image.load(f"img/target{state_number}.png")

    screen.blit(target_img, (target_x, target_y))
    screen.blit(hits_text, (10, 10))
    screen.blit(target_text, (10, 40))

    pygame.display.update()

pygame.quit()
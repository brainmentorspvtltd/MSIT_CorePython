# pip install pygame
import pygame
import random
pygame.init()

width = 900
height = 500

screen = pygame.display.set_mode((width, height))

# rgb
white = 255, 255, 255
black = 0, 0, 0
blue = 50, 50, 255
green = 50, 255, 57
red = 242, 29, 29

x = 100
y = 100
x2 = random.randint(0, 850)
y2 = random.randint(0, 450)
moveX = 0
moveY = 0
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:   # key was pressed
            if event.key == pygame.K_DOWN:  # down array key was pressed
                moveY = 1
                moveX = 0
            if event.key == pygame.K_UP:
                moveY = -1
                moveX = 0
            if event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            if event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0

    screen.fill(green)
    color = random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255)

    # surface, color, (x,y,width,height)
    pygame.draw.rect(screen, blue, (x, y, 50, 50))
    pygame.draw.rect(screen, red, (x2, y2, 50, 50))

    x += moveX
    y += moveY

    pygame.display.update()

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

screen.fill(green)
x = 100
y = 100
moveX = 5
moveY = 5
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # screen.fill(green)
    color = random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255)
    # surface, color, (x,y), radius
    pygame.draw.circle(screen, color, (x, y), 50)
    x += moveX
    y += moveY

    if y > 450:
        moveY = random.randint(-10, -5)
    if y < 50:
        moveY = random.randint(5, 10)
    if x > 850:
        moveX = random.randint(-10, -5)
    if x < 50:
        moveX = random.randint(5, 10)
    pygame.display.update()

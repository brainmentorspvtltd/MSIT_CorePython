# pip install pygame
import pygame
import random
pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width, height))
black = 0, 0, 0
font = pygame.font.SysFont(None, 60)

bricks = []

for i in range(9):
    for j in range(4):
        x = 10 + (i * 110)
        y = 10 + (j * 35)
        brick = pygame.Rect((x, y, 100, 25))
        bricks.append(brick)
    # 0 -> 10
    # 1 -> 120
    # 2 -> 230
    # 3 - >340

print(bricks)


def homeScreen():
    bgImage = pygame.image.load(
        "assets/brick-breaker-switch-hero_1000x500.jpg")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # print("Space pressed")
                    mainScreen()
        screen.fill(black)
        screen.blit(bgImage, (0, 0))
        color = random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)
        msg = "Press SPACE to continue"
        renderedMsg = font.render(msg, True, color)
        screen.blit(renderedMsg, (250, 350))

        pygame.display.update()


def mainScreen():
    barX = 375
    barY = 465
    ballX = 500
    ballY = 455
    moveX = 0
    moveY = 0
    moveBarX = 0
    color = random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    moveX = 5
                    moveY = -5
                if event.key == pygame.K_RIGHT:
                    moveBarX = 5
                if event.key == pygame.K_LEFT:
                    moveBarX = -5
        screen.fill(black)
        bar = pygame.draw.rect(screen, color, (barX, barY, 250, 10))
        ball = pygame.draw.circle(screen, color, (ballX, ballY), 10)

        for brick in bricks:
            pygame.draw.rect(screen, color, brick)

        if bar.colliderect(ball):
            moveY = -5

        for brick in bricks:
            if brick.colliderect(ball):
                bricks.remove(brick)
                moveY = 5
                break

        if ballY > 500:
            endGame()
        if ballY < 10:
            moveY = 5
        if ballX > 990:
            moveX = -5
        if ballX < 10:
            moveX = 5

        ballX += moveX
        ballY += moveY
        barX += moveBarX

        pygame.display.update()


def endGame():
    print("game ended")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


homeScreen()

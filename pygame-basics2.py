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
snakeSpeed = 5
frog = pygame.image.load("assets/frog_2.png")
game_bg = pygame.image.load("assets/snake_bg.png")
collisionSound = pygame.mixer.Sound("assets/point.wav")
bg_music = pygame.mixer.Sound("assets/music_1.wav")
bg_music.play(-1)
counter = 0

# font = pygame.font.SysFont("assets/font_1.ttf", 30)
font = pygame.font.SysFont(None, 30)

# snakeBody = [[500, 100], [505, 100], [510, 100], [515, 100]]
snakeBody = []
snakeLength = 1

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:   # key was pressed
            if event.key == pygame.K_DOWN:  # down array key was pressed
                if moveY == 0:
                    moveY = snakeSpeed
                    moveX = 0
            if event.key == pygame.K_UP:
                if moveY == 0:
                    moveY = -snakeSpeed
                    moveX = 0
            if event.key == pygame.K_LEFT:
                if moveX == 0:
                    moveX = -snakeSpeed
                    moveY = 0
            if event.key == pygame.K_RIGHT:
                if moveX == 0:
                    moveX = snakeSpeed
                    moveY = 0

    screen.fill(white)
    msg = f"Score : {counter}"
    renderedMsg = font.render(msg, True, red)
    screen.blit(renderedMsg, (20, 20))
    # screen.blit(game_bg, (0, 0))
    color = random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255)

    # surface, color, (x,y,width,height)
    rect1 = pygame.draw.rect(screen, blue, (x, y, 50, 50))
    # rect2 = pygame.draw.rect(screen, green, (x2, y2, 50, 50))
    rect2 = pygame.Rect((x2, y2, 50, 50))
    screen.blit(frog, (x2, y2))
    # ball = pygame.draw.circle(screen, red, (x2, y2), 25)

    snakeBody.append([x, y])

    if len(snakeBody) > snakeLength:
        del snakeBody[0]

    print(snakeBody)

    for bodyPart in snakeBody:
        color = random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)
        pygame.draw.rect(screen, color, (bodyPart[0], bodyPart[1], 50, 50))

    if rect1.colliderect(rect2):
        x2 = random.randint(0, 850)
        y2 = random.randint(0, 450)
        collisionSound.play()
        counter += 1
        snakeLength += 10

    x += moveX
    y += moveY

    if x > width:
        x = -50
    if x < -50:
        x = width
    if y > height:
        y = -50
    if y < -50:
        y = height

    pygame.display.update()

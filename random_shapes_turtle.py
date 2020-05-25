import turtle
import random

screen = turtle.Screen()
screen.bgcolor('black')
pen = turtle.Pen()
#pen.color('yellow')
pen.width(3)
pen.turtlesize(3)
pen.shape('turtle')
pen.speed(0)

colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan',
          'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'gray', 'white']

for i in range(50):

    shape = random.randint(1,8)
    #color1 = random.choice(colors)
    #color2 = random.choice(colors)
    #pen.color(color1)
    #pen.fillcolor(color2)
    pen.color( random.choice(colors) )
    pen.fillcolor( random.choice(colors) )
    pen.begin_fill()
    pen.penup()  # stop drawing
    # pen.setposition( x-coordinate, y-coordinate )
    pen.setposition( random.randint(-250,150), random.randint(-250,150) )
    pen.pendown()

    if shape == 1:
        pen.circle(100)
    elif shape == 2:
        for i in range(8):
            pen.forward(100)
            pen.left(45)
    elif shape == 3:
        pen.dot(200)
    elif shape == 4:
        for i in range(4):
            pen.forward(200)
            pen.left(90)
    elif shape == 5:
        for i in range(2):
            pen.forward(300)
            pen.left(90)
            pen.forward(200)
            pen.left(90)
    elif shape == 6:
        for i in range(5):
            pen.forward(150)
            pen.left(72)
    elif shape == 7:
        for i in range(6):
            pen.forward(150)
            pen.left(60)
    elif shape == 8:
        for i in range(3):
            pen.forward(200)
            pen.left(120)

    pen.end_fill()

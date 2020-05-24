import turtle
import random

screen = turtle.Screen()
screen.bgcolor('black')
pen = turtle.Pen()
pen.color('yellow')
pen.width(3)
pen.turtlesize(3)
pen.shape('turtle')
pen.speed(0)

colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan',
          'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'gray', 'white']

for i in range(50):

    shape = random.randint(1,4)

    pen.fillcolor('darkblue')
    pen.begin_fill()

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
        pass
    elif shape == 6:
        pass
    elif shape == 7:
        pass
    elif shape == 8:
        pass

    pen.end_fill()

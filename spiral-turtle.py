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

for i in range(25):
    pen.circle(10 + (i * 5) )
    pen.left(10)
    pen.forward(10)

'''for i in range(1,500,5):
    pen.circle(10 + i)
    pen.left(10)'''

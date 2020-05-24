import turtle
screen = turtle.Screen()
screen.bgcolor('black')
pen = turtle.Pen()
pen.color('yellow')
pen.width(3)
pen.turtlesize(3)
pen.shape('turtle')
pen.speed(10)

'''
print("1. Circle")
print("2. Octagon")
print("9. Exit")'''

'''print("1. Circle \
      \n2. Octagon \
      \n9. Exit")    # \ charcater tells python that the statement sin't complete, please look into the next line
'''

print("""
    1. Circle
    2. Octagon
    3. Dot
    4. Square
    5. Rectangle
    6. Pentagon
    7. Hexagon
    8. Triangle
    9. Exit
""")

while True:

    pen.fillcolor('darkblue')
    pen.begin_fill()

    user_input = int(input("Enter shape number to draw: "))

    if user_input == 1:
        pen.circle(100)
    elif user_input == 2:
        for i in range(8):
            pen.forward(100)
            pen.left(45)
    elif user_input == 3:
        pen.dot(200)
    elif user_input == 4:
        for i in range(4):
            pen.forward(200)
            pen.left(90)
    elif user_input == 5:
        pass
    elif user_input == 6:
        pass
    elif user_input == 7:
        pass
    elif user_input == 8:
        pass
    elif user_input == 9:
        break  # break the loop just above it
    else:
        print("Shape doesn't exist")

    pen.end_fill()

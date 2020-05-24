import turtle
screen = turtle.Screen()
screen.bgcolor('black')
pen = turtle.Pen()
pen.color('yellow')
pen.width(3)
pen.turtlesize(3)
pen.shape('turtle')
pen.speed(10)

# for(int i = 0; i < 300; i++){
#     
# }

'''for i in [0,1,2]:
    pen.forward(200)
    pen.left(120)'''

'''for i in [0,1,2,3,4,5,6,7,8,9,10,11]:
    pen.forward(100)
    pen.left(60)'''

# if(user_input == "circle"){}

while True:

    pen.fillcolor('darkblue')
    pen.begin_fill()

    user_input = input("Enter shape name: ").lower()

    if user_input == "circle":
        pen.circle(100)
    elif user_input == "octagon" or user_input == "Octagon":
        for i in range(8):
            pen.forward(100)
            pen.left(45)
    elif user_input == "dot":
        pen.dot(200)
    elif user_input == "square":
        for i in range(4):
            pen.forward(200)
            pen.left(90)
    elif user_input == "rectangle":
        pass
    elif user_input == "pentagon":
        pass
    elif user_input == "hexagon":
        pass
    elif user_input == "triangle":
        pass
    else:
        print("Shape doesn't exist")

    pen.end_fill()

'''
for i in range(8):
    pen.forward(100)
    pen.left(45)
'''

'''
# range( starting index, stopping index, step )
>>> # range(5) -> [0,1,2,3,4]
>>> # range(2,10) -> [2,3,4,5,6,7,8,9]
>>> # range(2,10,2) -> [2,4,6,8]
>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(2,10))
[2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> list(range(20,10,-1))
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
>>> 
>>> i = 10
>>> i++
SyntaxError: invalid syntax
>>> i+1
11
>>> i
10
>>> i = i + 1
>>> i
11
>>> i += 1
>>> i
12
>>> i -= 1
>>> i
11
>>> i *= 2
>>> i
22
>>> i /= 11
>>> i
2.0
>>> i **= 10
>>> i
1024.0
>>> i //= 8
>>> i
128.0
'''

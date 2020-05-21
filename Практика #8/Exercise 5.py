import turtle
import time

turtle.shape('turtle')
turtle.speed('fastest')
turtle.width(2)

turtle.penup()
turtle.right(180)
turtle.forward(450)
turtle.right(180)
turtle.pendown()

length = 40

def bunch(deep=1):
    if deep == 0:
        turtle.forward(length)
        return
    if deep == 1:
        turtle.forward(length / 4)
        turtle.left(90)
        turtle.forward(length / 4)
        turtle.right(90)
        turtle.forward(length / 4)
        turtle.right(90)
        turtle.forward(length / 2)
        turtle.left(90)
        turtle.forward(length / 4)
        turtle.left(90)
        turtle.forward(length / 4)
        turtle.right(90)
        turtle.forward(length / 4)
        return
    bunch(deep - 1)
    turtle.left(90)
    bunch(deep - 1)
    turtle.right(90)
    bunch(deep - 1)
    turtle.right(90)
    bunch(deep - 1)
    bunch(deep - 1)
    turtle.left(90)
    bunch(deep - 1)
    turtle.left(90)
    bunch(deep - 1)
    turtle.right(90)
    bunch(deep - 1)


bunch(2)

time.sleep(2)
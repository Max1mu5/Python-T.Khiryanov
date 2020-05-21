import turtle
import time

turtle.shape('turtle')
turtle.speed(6)

turtle.penup()
turtle.right(180)
turtle.forward(450)
turtle.right(180)
turtle.pendown()

length = 81

def bunch(deep=1):
    if deep == 1:
        turtle.forward(length / 3)
        turtle.left(60)
        turtle.forward(length / 3)
        turtle.right(120)
        turtle.forward(length / 3)
        turtle.left(60)
        turtle.forward(length / 3)
        return
    bunch(deep-1)
    turtle.left(60)
    bunch(deep-1)
    turtle.right(120)
    bunch(deep - 1)
    turtle.left(60)
    bunch(deep-1)

bunch(1)


time.sleep(10)

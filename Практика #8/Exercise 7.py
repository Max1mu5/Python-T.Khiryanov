import turtle
import time

turtle.shape('turtle')
turtle.speed(6)
turtle.width(3)


length = 80

def bunch(deep=1):
    if deep == 0:
        turtle.forward(length)
        return
    if deep == 1:
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        return
    elif deep == 2:
        turtle.right(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        return

    turtle.right(45)
    bunch(deep - 1)
    # turtle.left(90)

        
bunch(1)

time.sleep(10)
import turtle
import time

turtle.shape('turtle')
turtle.speed('fastest')
turtle.width(3)


length = 20

def bunch(deep=1):
    if deep == 0:
        turtle.forward(length)
    if deep == 1:
        turtle.left(45)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(45)
        return
    
    turtle.left(45)
    bunch(deep - 1)
    turtle.right(90)
    bunch(deep - 1)
    turtle.left(45)
    
bunch(3)

time.sleep(2)
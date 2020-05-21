import turtle
import time

turtle.shape('turtle')
turtle.speed('fastest')
turtle.width(0.5)


length = 8


def bunch(deep, direction):
    if deep == 0:
        turtle.forward(length)
    if not direction:
        if deep == 1:
            turtle.forward(length)
            turtle.right(90)
            print('right')
            turtle.forward(length)
            return
    else:
        if deep == 1:
            turtle.forward(length)
            turtle.left(90)
            print('left')
            turtle.forward(length)
            return

    bunch(deep - 1, True)
    if direction:
        turtle.left(90)
    else:
        turtle.right(90)
    bunch(deep - 1, False)


n = 10
turtle.right(n * 45)
bunch(n, True)


time.sleep(5)
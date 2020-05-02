import turtle
import time

turtle.shape('turtle')
turtle.speed(3)


def foo(b):
    if b:
        for _ in range(90):
            turtle.forward(3)
            turtle.left(4)
    else:
        for _ in range(90):
            turtle.forward(3)
            turtle.right(4)


for _ in range(3):
    foo(True)
    foo(False)
    turtle.left(60)

time.sleep(2)

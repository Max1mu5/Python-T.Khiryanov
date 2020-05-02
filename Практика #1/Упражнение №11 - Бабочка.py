import turtle
import time

turtle.shape('turtle')
turtle.speed(3)


def foo(r):
    for _ in range(90):
        turtle.forward(r)
        turtle.left(4)
    for _ in range(90):
        turtle.forward(r)
        turtle.right(4)


turtle.right(90)
for i in range(4, 16, 1):
    foo(i)

time.sleep(2)
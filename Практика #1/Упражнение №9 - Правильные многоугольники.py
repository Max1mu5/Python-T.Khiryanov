import turtle
import math
import time

turtle.shape('turtle')
turtle.speed(3)


def foo(n, d):
    a = (n - 2) / n * 180
    turtle.left(a / 2)
    for _ in range(n):
        turtle.left(180 - a)
        turtle.forward(d)
    turtle.right(a / 2)


k = 3
R = 35
for i in range(1, 11):
    x = 2 * R * math.sin(math.pi / k)
    foo(k, x)

    turtle.penup()
    turtle.forward(20)
    turtle.pendown()

    k += 1
    R += 20

time.sleep(2)

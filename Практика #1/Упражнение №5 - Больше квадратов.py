import turtle
import time

turtle.shape('turtle')
turtle.speed(3)

for i in range(1, 11):
    for _ in range(4):
        turtle.forward(20 + 2*i*10)
        turtle.left(90)

    turtle.penup()
    turtle.goto(-10*i, -10*i)
    turtle.pendown()

time.sleep(2)
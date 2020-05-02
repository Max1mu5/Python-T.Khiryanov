import turtle
import time

turtle.shape('turtle')
turtle.speed(3)

turtle.left(90)
turtle.penup()
turtle.setpos(-300, 0)
turtle.pendown()

for i in range(10):
    for _ in range(45):
        turtle.forward(3)
        turtle.right(4)
    for _ in range(45):
        turtle.forward(0.5)
        turtle.right(4)

time.sleep(2)

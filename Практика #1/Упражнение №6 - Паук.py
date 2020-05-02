import turtle
import time

n = int(input())

turtle.shape('turtle')
turtle.speed(3)

for i in range(n):
    turtle.forward(60)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(60)
    turtle.right(180)
    turtle.right(360/n)


time.sleep(2)
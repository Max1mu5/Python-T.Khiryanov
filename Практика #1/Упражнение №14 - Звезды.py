import turtle
import time

n = int(input())

turtle.shape('turtle')
turtle.speed(3)


while True:
    turtle.forward(200)
    turtle.left(180 - 180/n)
    if abs(turtle.pos()) < 1:
        break
        
time.sleep(2)
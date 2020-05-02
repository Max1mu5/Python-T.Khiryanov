import turtle
import time

turtle.shape('turtle')
turtle.speed(3)


def colored_circle(r, *color):
    turtle.color(*color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


colored_circle(60, 'black', 'yellow')

turtle.penup()
turtle.setpos(-30, 60)
turtle.pendown()

colored_circle(10, 'black', 'blue')

turtle.penup()
turtle.setpos(30, 60)
turtle.pendown()

colored_circle(10, 'black', 'blue')

turtle.width(10)
turtle.color('red')
turtle.right(270)

turtle.penup()
turtle.setpos(30, 40)
turtle.pendown()

turtle.circle(30, -180)

time.sleep(2)
import turtle
import time

turtle.shape('turtle')
turtle.speed(1)
turtle.width(3)

length = 162

turtle.penup()
turtle.right(180)
turtle.forward(length / 2)
turtle.right(180)
turtle.pendown()

def bunch(deep, L, first_call=True):
    if deep == 0 and not first_call:
        turtle.forward(L)
        turtle.penup()
        
        return
    if first_call:
        tp = turtle.pos()
        turtle.forward(L)
        turtle.penup()
        turtle.setpos(tp[0], tp[1] - 20)
        turtle.pendown()
    else:
        # turtle.penup()
        # turtle.setpos(tp[0], tp[1] - 20)
        # turtle.pendown()
        # bunch(deep - 1, L / 3)
        # turtle.setpos(turtle.pos()[0] + 2 * L, turtle.pos()[1])
        # bunch(deep - 1, L / 3)


bunch(3, length)
turtle.setpos(0, 0)
time.sleep(5)
import turtle
import time

turtle.shape('turtle')
turtle.speed(4)
turtle.width(3)

length = 666

turtle.penup()
turtle.right(180)
turtle.forward(length / 2)
turtle.right(180)
turtle.pendown()

def bunch(deep, L, first_call=True):
    cur_coords = turtle.pos()
    if deep == 0:
        turtle.forward(L)
        turtle.penup()
        turtle.setpos(cur_coords[0] + 2 * L, cur_coords[1])
        turtle.pendown()
        turtle.forward(L)
        return
    if first_call:
        turtle.forward(L)
        turtle.penup()
        turtle.setpos(cur_coords[0], cur_coords[1] - 20)
        turtle.pendown()
        bunch(deep, L / 3, False)
        return

    turtle.forward(L)
    turtle.penup()
    turtle.setpos(cur_coords[0], cur_coords[1] - 20)
    turtle.pendown()
    bunch(deep - 1, L / 3, False)



bunch(3, length)
time.sleep(5)
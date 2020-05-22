import turtle
import time

turtle.shape('turtle')
turtle.speed(4)
turtle.width(2)

length = 666

turtle.penup()
turtle.right(180)
turtle.forward(length / 2)
turtle.right(180)
turtle.pendown()

def bunch(deep, L, first_call=True):
    cur_coords = turtle.pos()
    if first_call:
        turtle.forward(L)
        turtle.penup()
        turtle.setpos(cur_coords[0], cur_coords[1] - 20)
        turtle.pendown()
        bunch(deep, L / 3, False)
        return
    if deep == 0:
        return

    turtle.forward(L)
    turtle.penup()
    turtle.setpos(cur_coords[0], cur_coords[1] - 20)
    turtle.pendown()
    bunch(deep - 1, L / 3, False)

    turtle.penup()
    turtle.setpos(cur_coords[0] + 2 * L, cur_coords[1])
    turtle.pendown()
    new_coords = turtle.pos()
    turtle.forward(L)
    turtle.penup()
    turtle.setpos(new_coords[0], new_coords[1] - 20)
    turtle.pendown()
    bunch(deep - 1, L / 3, False)

bunch(6, length)
time.sleep(5)
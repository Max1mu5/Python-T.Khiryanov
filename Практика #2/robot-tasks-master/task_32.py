#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    c = 0
    while not wall_is_on_the_right():
        if cell_is_filled():
            c += 1
        if wall_is_above() and wall_is_beneath():
            fill_cell()
        move_right()
        
        if not wall_is_beneath() and not wall_is_above():
            break
        while not wall_is_above():
            move_up()
            if cell_is_filled():
                c += 1
            fill_cell()
        else:
            while not wall_is_beneath():
                move_down()
    mov('ax', c)


if __name__ == '__main__':
    run_tasks()

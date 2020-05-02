#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while not wall_is_beneath():
        if wall_is_on_the_left():
            while not wall_is_on_the_right():
                fill_cell()
                move_right()
            fill_cell()
            move_down()
        else:
            while not wall_is_on_the_left():
                fill_cell()
                move_left()
            fill_cell()
            move_down()

    else:
        if wall_is_on_the_left():
            while not wall_is_on_the_right():
                fill_cell()
                move_right()
            fill_cell()
            while not wall_is_on_the_left():
                move_left()
        else:
            while not wall_is_on_the_left():
                fill_cell()
                move_left()
            fill_cell()




if __name__ == '__main__':
    run_tasks()

#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_8_30():
    exit = True
    while exit:
        while not wall_is_on_the_left():
            if not wall_is_beneath():
                while not wall_is_beneath():
                    move_down()
            move_left()
        else:
            while not wall_is_on_the_right():
                move_right()
                if not wall_is_beneath():
                    exit = True
                    break
            else:
                exit = False

    while not wall_is_on_the_left():
        move_left()



if __name__ == '__main__':
    run_tasks()

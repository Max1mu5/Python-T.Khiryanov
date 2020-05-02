#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()

    x = 1
    while not wall_is_on_the_right():
        for _ in range(x):
            if wall_is_on_the_right():
                break
            move_right()
        else:
            fill_cell()
        x += 1


if __name__ == '__main__':
    run_tasks()

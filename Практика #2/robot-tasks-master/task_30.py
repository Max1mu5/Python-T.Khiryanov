#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    a = 1
    while not wall_is_on_the_right():
        move_right()
        a += 1

    move_left(a - 1)
    for i in range(1, a+1):
        for j in range(1, a+1):
            if (j == i) or (j + i == a + 1):
                if not wall_is_on_the_right():
                    move_right()
            else:
                fill_cell()
                if not wall_is_on_the_right():
                    move_right()
        if not wall_is_beneath():
            move_down()
        move_left(a-1)


if __name__ == '__main__':
    run_tasks()

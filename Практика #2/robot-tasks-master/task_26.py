#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    for i in range(5):
        for _ in range(10):
            krest()
            if _ == 9:
                break
            move_right(4)
        move_left(36)
        if i == 4:
            break
        move_down(4)


def krest():
    move_right()
    fill_cell()
    move_right()
    move_down()
    fill_cell()
    move_down()
    move_left()
    fill_cell()
    move_up()
    fill_cell()
    move_left()
    fill_cell()
    move_up()


if __name__ == '__main__':
    run_tasks()

#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_down()
    for _ in range(5):
        krest()
        if _ == 4:
            break
        move_right(4)


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

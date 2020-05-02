#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    for i in range(14):
        for _ in range(i):
            fill_cell()
            move_right()
        for _ in range(i):
            move_left()
        move_down()
        
if __name__ == '__main__':
    run_tasks()

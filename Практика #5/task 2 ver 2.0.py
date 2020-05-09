import graphics as gr
from math import *
"""
Улучшенное решение второго задания из практики №5.
Пока на каждой итерации цикла рисуется новый объект, из-за это сильно падает оптимизация.
Тут добавлена возможность изменения стартового угла наклона, длинны веревки и коэффициента затухания.
Код взят отсюда - https://github.com/kkmoskalenko/pendulum-test и переписан на питоне 
"""
window = gr.GraphWin('test', 500, 500)

angle = -45
deceleration = 0.001
length = 0.6
g = 9.80665

coef = 400
length *= coef
amp = sin(radians(angle)) * length
period = 2 * pi * sqrt(length / coef / g)


def calc_x():
    angfreq = (2 * pi) / period
    decel = e**(-deceleration * get_time())
    return amp * cos(angfreq * get_time()) * decel


def calc_y():
    return sqrt(length**2 - calc_x()**2) - length


time = 0
def get_time():
    return time / 1000


def clear():
    rect = gr.Rectangle(gr.Point(0, 0), gr.Point(500, 500))
    rect.setFill('white')
    rect.draw(window)


interval = 30
while True:
    clear()
    ball = gr.Circle(gr.Point(250 + calc_x(), length + calc_y()), 10)
    ball.setFill('blue')
    ball.draw(window)

    time += interval
    gr.time.sleep(0.01)


import graphics as gr
from math import *
"""
Улучшенное решение второго задания из практики №5.
Тут добавлена возможность изменения стартового угла наклона, длинны веревки и коэффициента затухания.
Код взят отсюда - https://github.com/kkmoskalenko/pendulum-test и переписан на питоне 
"""
window = gr.GraphWin('test', 500, 500)

angle = -30
deceleration = 0
length = 0.1
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


ball = gr.Circle(gr.Point(250 + calc_x(), length + calc_y()), 10)
ball.setFill('RED')
ball.draw(window)


interval = 25
while True:
    time += interval
    x = 250 + calc_x() - ball.getCenter().x
    y = length + calc_y() - ball.getCenter().y
    ball.move(x, y)

    gr.time.sleep(0.04)


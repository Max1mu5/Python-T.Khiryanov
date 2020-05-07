import graphics as gr
import math

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Simple pendulum", SIZE_X, SIZE_Y)
line = gr.Line(gr.Point(400, 0), gr.Point(400, 800))
line.setWidth(4)
line.draw(window)


R = 10
x, y = 200, 550
circle = gr.Circle(gr.Point(x, y), R)
circle.setFill('Blue')
circle.draw(window)

# a = math.radians(90)
# L = math.sqrt((500-x)**2+(500-y)**2)
max_amp = SIZE_X - circle.getCenter().x
velocity = gr.Point(0, 0)
acceleration = gr.Point(0, 2)
grav = gr.Point(0, 0.03200049999999)


def check_coords(obj):
    if obj.getCenter().x + R > 500 + max_amp:
        velocity.x = -velocity.x
        velocity.y = 0
    if obj.getCenter().x - R < 500 - max_amp:
        velocity.x = -velocity.x
        velocity.y = 0

def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def sub (point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)

    return new_point

def update_velocity(velocity, acceleration):
    return add(add(velocity, grav), acceleration)


def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)
    G = 2000.0705395603
    print(-diff.x*G/distance_2)
    return gr.Point(-diff.x*G/distance_2, -diff.y*G/distance_2)



while True:

    circle.move(velocity.x, velocity.y)
    # circle.clone().draw(window)
    acceleration = update_acceleration(circle.getCenter(), gr.Point(SIZE_X/2, SIZE_Y/2))
    velocity = update_velocity(velocity, acceleration)


    gr.time.sleep(0.01)

window.close()
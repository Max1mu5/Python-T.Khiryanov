import graphics as gr

SIZE_X = 400
SIZE_Y = 400

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)
circle = gr.Circle(gr.Point(200, 200), 10)
circle.draw(window)

velocity = gr.Point(1, -2)
acceleration = gr.Point(0, 0.1)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def check_coords(obj: gr.Circle, velocity):
    if obj.getCenter().getX() - 10 < 0 or obj.getCenter().getX() + 10 > SIZE_X:
        velocity.x = -velocity.x

    if obj.getCenter().getY() - 10 < 0 or obj.getCenter().getY() + 10 > SIZE_Y:
        velocity.y = -velocity.y


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


while True:
    circle.move(velocity.x, velocity.y)
    velocity = update_velocity(velocity, acceleration)
    check_coords(circle, velocity)

    gr.time.sleep(0.02)

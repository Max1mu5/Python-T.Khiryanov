import graphics as gr

window = gr.GraphWin("Russian game", 1000, 1000)


def background():
    top_rec = gr.Rectangle(gr.Point(0, 0), gr.Point(1000, 500))
    top_rec.setFill('Blue')
    bot_rec = gr.Rectangle(gr.Point(0, 500), gr.Point(1000, 1000))
    bot_rec.setFill('Light Grey')
    top_rec.draw(window)
    bot_rec.draw(window)


def tree(p1, p2, p3):
    trig = gr.Polygon(p1, p2, p3)
    trig.setFill('Green')
    trig.setWidth(3.5)
    trig.draw(window)


def sun():
    sun1 = gr.Circle(gr.Point(720, 200), 75)
    sun1.setFill('Yellow')
    sun1.draw(window)


def clouds(x, y, r):
    cl_1 = gr.Circle(gr.Point(x, y), r)
    cl_1.setFill('White')
    cl_2 = gr.Circle(gr.Point(x + 30, y), r)
    cl_2.setFill('White')
    cl_3 = gr.Circle(gr.Point(x - 15, y + 16), r)
    cl_3.setFill('White')
    cl_4 = gr.Circle(gr.Point(x + 15, y + 16), r)
    cl_4.setFill('White')
    cl_5 = gr.Circle(gr.Point(x + 45, y + 16), r)
    cl_5.setFill('White')
    cl_1.draw(window)
    cl_2.draw(window)
    cl_3.draw(window)
    cl_4.draw(window)
    cl_5.draw(window)


def house():
    wall = gr.Rectangle(gr.Point(200, 350), gr.Point(500, 650))
    wall.setFill('Grey')
    wall.setWidth(3)
    top_trig = gr.Polygon(gr.Point(200, 350), gr.Point(500, 350), gr.Point(350, 200))
    top_trig.setFill('#a52a2a')
    top_trig.setWidth(3)
    wnd = gr.Rectangle(gr.Point(300, 450), gr.Point(400, 550))
    wnd.setFill('Yellow')
    wnd.setWidth(4)
    wnd_line_1 = gr.Line(gr.Point(350, 450), gr.Point(350, 550))
    wnd_line_1.setWidth(4)
    wnd_line_2 = gr.Line(gr.Point(300, 500), gr.Point(400, 500))
    wnd_line_2.setWidth(4)
    wall.draw(window)
    top_trig.draw(window)
    wnd.draw(window)
    wnd_line_1.draw(window)
    wnd_line_2.draw(window)


def draw_all():
    background()

    tree(gr.Point(650, 575), gr.Point(850, 575), gr.Point(750, 475))
    tree(gr.Point(650, 625), gr.Point(850, 625), gr.Point(750, 525))
    tree(gr.Point(650, 675), gr.Point(850, 675), gr.Point(750, 575))
    tree_rec = gr.Rectangle(gr.Point(740, 675), gr.Point(760, 725))
    tree_rec.setWidth(3.5)
    tree_rec.setFill('Brown')
    tree_rec.draw(window)

    house()

    clouds(115, 200, 30)
    clouds(415, 150, 30)
    sun()
    clouds(770, 250, 40)





draw_all()

window.getMouse()
window.close()
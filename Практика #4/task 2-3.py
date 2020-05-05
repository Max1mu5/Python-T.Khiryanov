import graphics as gr

main_window = gr.GraphWin("Russian game", 1000, 1000)


def background(color1, color2, sizeX, sizeY, window):
    """
    Данная функция отрисовывыет небо и землю в отношении 1:1 относительно размеров окна:
    color1 - цвет неба
    color2 - цвет земли
    sizeX - размер окна по Ох
    sizeY - размер окна по Oy
    """
    top_rec = gr.Rectangle(gr.Point(0, 0), gr.Point(sizeX, sizeY // 2))
    top_rec.setFill(color1)
    bot_rec = gr.Rectangle(gr.Point(0, sizeY // 2), gr.Point(sizeX, sizeY))
    bot_rec.setFill(color2)
    top_rec.draw(window)
    bot_rec.draw(window)


def tree(p1, p2, p3, window):
    trig = gr.Polygon(p1, p2, p3)
    trig.setFill('Green')
    trig.setWidth(3.5)
    trig.draw(window)


def sun(posX, posY, r, window):
    """
    posX, posY - координаты центра Солнца
    r - радиус
    """
    sun1 = gr.Circle(gr.Point(posX, posY), r)
    sun1.setFill('Yellow')
    sun1.draw(window)


def clouds(posX, posY, r, window):
    """
    Ф-ция рисует составное облако из 4 окружностей в виде перевернутого знака олимпиады
    Размер высчитывается относительно левого круга из верхнего ряда
    posX, posY - координаты верхнего левого облака
    r - радиус
    """
    cl_1 = gr.Circle(gr.Point(posX, posY), r)
    cl_1.setFill('White')
    cl_2 = gr.Circle(gr.Point(posX + r, posY), r)
    cl_2.setFill('White')
    cl_3 = gr.Circle(gr.Point(posX - r/2, posY + r/2+1), r)
    cl_3.setFill('White')
    cl_4 = gr.Circle(gr.Point(posX + r/2, posY + r/2+1), r)
    cl_4.setFill('White')
    cl_5 = gr.Circle(gr.Point(posX + r*1.5, posY + r/2+1), r)
    cl_5.setFill('White')
    cl_1.draw(window)
    cl_2.draw(window)
    cl_3.draw(window)
    cl_4.draw(window)
    cl_5.draw(window)


def house(posX, posY, size, window):
    """
    Ф-ция рисует дом относительно левого верхнего угла
    size - множитель размеров дома
    """
    wall = gr.Rectangle(gr.Point(posX, posY), gr.Point(posX + 100*size, posY + 100*size))
    wall.setFill('Grey')
    wall.setWidth(3)
    top_trig = gr.Polygon(gr.Point(posX, posY), gr.Point(posX + 100*size, posY), gr.Point(posX+50*size, posX-10*size))
    top_trig.setFill('#a52a2a')
    top_trig.setWidth(3)
    wnd = gr.Rectangle(gr.Point(posX + 30*size, posY + 30 * size), gr.Point(posX + 70*size, posY + 70*size))
    wnd.setFill('Yellow')
    wnd.setWidth(4)
    wnd_line_1 = gr.Line(gr.Point(posX + 50*size, posY + 30*size), gr.Point(posX + 50*size, posY + 70*size))
    wnd_line_1.setWidth(4)
    wnd_line_2 = gr.Line(gr.Point(posX+30*size, posY + 50*size), gr.Point(posX+70*size, posY + 50*size))
    wnd_line_2.setWidth(4)
    wall.draw(window)
    top_trig.draw(window)
    wnd.draw(window)
    wnd_line_1.draw(window)
    wnd_line_2.draw(window)


def draw_all():
    background('blue', 'light grey', 1000, 1000, main_window)

    tree(gr.Point(650, 675), gr.Point(850, 675), gr.Point(750, 575), main_window)
    tree(gr.Point(650, 625), gr.Point(850, 625), gr.Point(750, 525), main_window)
    tree(gr.Point(650, 575), gr.Point(850, 575), gr.Point(750, 475), main_window)
    tree_rec = gr.Rectangle(gr.Point(740, 675), gr.Point(760, 725))
    tree_rec.setWidth(3.5)
    tree_rec.setFill('Brown')
    tree_rec.draw(main_window)

    house(250, 350, 3, main_window)

    clouds(115, 200, 30, main_window)
    clouds(415, 150, 30, main_window)
    sun(720, 200, 75, main_window)
    clouds(770, 250, 40, main_window)





draw_all()

main_window.getMouse()
main_window.close()
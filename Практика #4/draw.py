import graphics as gr

window = gr.GraphWin("Russian game", 1000, 1000)

#Фон
top_rec = gr.Rectangle(gr.Point(0, 0), gr.Point(1000, 500))
top_rec.setFill('Blue')
bot_rec = gr.Rectangle(gr.Point(0, 500), gr.Point(1000, 1000))
bot_rec.setFill('Light Grey')
top_rec.draw(window)
bot_rec.draw(window)

#Елка
trig_1 = gr.Polygon(gr.Point(650, 575), gr.Point(850, 575), gr.Point(750, 475))
trig_2 = gr.Polygon(gr.Point(650, 625), gr.Point(850, 625), gr.Point(750, 525))
trig_3 = gr.Polygon(gr.Point(650, 675), gr.Point(850, 675), gr.Point(750, 575))
trig_1.setFill('Green')
trig_1.setWidth(3.5)
trig_2.setFill('Green')
trig_2.setWidth(3.5)
trig_3.setFill('Green')
trig_3.setWidth(3.5)
tree_rec = gr.Rectangle(gr.Point(740, 675), gr.Point(760, 725))
tree_rec.setWidth(3.5)
tree_rec.setFill('Brown')
trig_3.draw(window)
trig_2.draw(window)
trig_1.draw(window)
tree_rec.draw(window)

#Солнце
sun = gr.Circle(gr.Point(720, 200), 75)
sun.setFill('Yellow')
sun.draw(window)

#Облако
cl_1 = gr.Circle(gr.Point(115, 200), 32)
cl_1.setFill('White')
cl_2 = gr.Circle(gr.Point(145, 200), 32)
cl_2.setFill('White')
cl_3 = gr.Circle(gr.Point(100, 216), 32)
cl_3.setFill('White')
cl_4 = gr.Circle(gr.Point(130, 216), 32)
cl_4.setFill('White')
cl_5 = gr.Circle(gr.Point(160, 216), 32)
cl_5.setFill('White')
cl_1.draw(window)
cl_2.draw(window)
cl_3.draw(window)
cl_4.draw(window)
cl_5.draw(window)

#Дом
wall = gr.Rectangle(gr.Point(200, 350), gr.Point(500, 650))
wall.setFill('Grey')
wall.setWidth(3)
wall.draw(window)
top_trig = gr.Polygon(gr.Point(200, 350), gr.Point(500, 350), gr.Point(350, 200))
top_trig.setFill('#a52a2a')
top_trig.setWidth(3)
top_trig.draw(window)
wnd = gr.Rectangle(gr.Point(300, 450), gr.Point(400, 550))
wnd.setFill('Yellow')
wnd.setWidth(4)
wnd.draw(window)
wnd_line_1 = gr.Line(gr.Point(350, 450), gr.Point(350, 550))
wnd_line_1.setWidth(4)
wnd_line_1.draw(window)
wnd_line_2 = gr.Line(gr.Point(300, 500), gr.Point(400, 500))
wnd_line_2.setWidth(4)
wnd_line_2.draw(window)



window.getMouse()
window.close()
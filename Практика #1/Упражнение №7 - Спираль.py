import turtle

turtle.shape('turtle')
turtle.speed(3)

k = 1
while True:
    turtle.forward(0.15*k)
    turtle.right(0.1*180/3.14)
    k += 0.2

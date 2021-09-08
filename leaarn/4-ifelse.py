import turtle

kura = turtle.Turtle()

def square() : 
    kura.forward(100)
    kura.left(90)
    kura.forward(100)
    kura.left(90)
    kura.forward(100)
    kura.left(90)
    kura.forward(100)
    kura.left(90)

def triangle() :
    kura.forward(300)
    kura.left(90)
    kura.forward(400)
    kura.left(135)
    kura.forward(500)
    kura.left(135)


elephant_weight = 0.001
ant_weigth = 0.1

if elephant_weight > ant_weigth :
    square()
else :
    triangle()

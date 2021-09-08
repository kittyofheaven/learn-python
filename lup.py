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
    

#while loops
#while True : 
#    square()

#for loops
for i in range(8) :
    square()


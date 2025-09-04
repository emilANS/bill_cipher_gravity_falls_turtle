import turtle

tortuga = turtle.Turtle()

tortuga.shape("turtle")

tortuga.penup()

tortuga.setposition(-150, -100)

tortuga.pendown()

distancia = 300


def crear_triangulo(angulo):

    tortuga.color("yellow")

    tortuga.fillcolor("yellow")

    tortuga.begin_fill()


    tortuga.left(angulo)

    tortuga.forward(distancia)

    tortuga.right(angulo * 2)

    tortuga.forward(distancia)

    tortuga.right(angulo * 2)

    tortuga.forward(distancia)

    tortuga.end_fill

def crear_ojo(radio):

    tortuga.penup()

    tortuga.setpos(0, 50)

    tortuga.pendown()

    tortuga.color("black")

    tortuga.begin_fill()

    tortuga.circle(50)

    tortuga.end_fill()

    tortuga.setpos(0, 25)

    tortuga.fillcolor("white")

    tortuga.begin_fill()

    tortuga.circle(radio)

    tortuga.end_fill()

def crear_pie_derecho():

    tortuga.penup()

    tortuga.setposition(-100, -100)

    tortuga.fillcolor("black")

    tortuga.pendown()

    tortuga.begin_fill()

    tortuga.left(95)

    tortuga.forward(100)

    tortuga.left(95)

    tortuga.forward(55)

    tortuga.left(100)

    tortuga.forward(15)

    tortuga.left(75)


    tortuga.forward(35)

    tortuga.right(90)

    tortuga.forward(75)

    tortuga.left(100)

    tortuga.forward(15)

    tortuga.end_fill()

def crear_pie_izquierdo():

    tortuga.penup()

    tortuga.setposition(100, -100)

    tortuga.fillcolor("black")

    tortuga.pendown()

    tortuga.begin_fill()

    tortuga.left(-95)

    tortuga.forward(-100)

    tortuga.left(-95)

    tortuga.forward(-55)

    tortuga.left(-100)

    tortuga.forward(-15)

    tortuga.left(-75)


    tortuga.forward(-35)

    tortuga.right(-90)

    tortuga.forward(-75)

    tortuga.left(-100)

    tortuga.forward(-15)

    tortuga.end_fill()

def crear_sombrero():

    tortuga.penup()

    tortuga.setpos(0, 100 + 60)

    tortuga.pendown()

    tortuga.fillcolor("black")

    tortuga.begin_fill()

    tortuga.forward(35)

    tortuga.right(90)

    tortuga.forward(15)

    tortuga.right(90)

    tortuga.forward(20)

    tortuga.left(90)

    tortuga.forward(30)

    tortuga.right(90)

    tortuga.forward(25)
    
    tortuga.right(90)

    tortuga.forward(28)

    tortuga.left(90)

    tortuga.forward(25)

    tortuga.right(90)
    
    tortuga.forward(15)

    tortuga.right(90)

    tortuga.forward(35)

    tortuga.end_fill()


tortuga.begin_fill()
crear_triangulo(60)
tortuga.end_fill()

tortuga.fillcolor("white")

crear_ojo(30)

crear_pie_derecho()

crear_pie_izquierdo()

crear_sombrero()

turtle.done()
import turtle

def dibujar_ventana(): # función
    turtle.speed(1)  # Velocidad de dibujo

    # Instrucciones para dibujar la ventana
    turtle.penup() #Subir el lápiz
    turtle.goto(0, 0)  # Posición inicial coordenadas(0,0)
    turtle.pendown() #Bajar el lápiz

    # Dibuja la ventana siguiendo las instrucciones
    turtle.forward(25)   # go (25)
    turtle.left(90)      # turn (90)
    turtle.forward(35)   # go (35)
    turtle.right(90)     # turn (-90)
    turtle.forward(45)   # go (45)
    turtle.left(90)      # turn (90)
    turtle.forward(52)   # go (52)
    turtle.left(90)      # turn (90)
    turtle.forward(85)   # go (85)
    turtle.right(90)     # turn (-90)
    turtle.forward(55)   # go (55)
    turtle.right(90)     # turn (-90)
    turtle.forward(47)   # go (47)
    turtle.left(90)      # turn (90)
    turtle.forward(30)   # go (30)
    turtle.right(90)     # turn (-90)
    turtle.forward(35)   # go (35)

    # Finaliza el dibujo
    turtle.hideturtle()
    turtle.done()

# Llama a la función para dibujar la ventana
dibujar_ventana()
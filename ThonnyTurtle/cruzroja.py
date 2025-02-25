import turtle

def dibujar_cuadrado():
    turtle.pensize(5)  # Grosor del lápiz para el cuadrado
    turtle.color("red")  # Color del cuadrado
    turtle.penup()
    turtle.goto(-150, 150)  # Posición inicial del cuadrado
    turtle.pendown()

    # Dibuja el cuadrado
    for _ in range(4):
        turtle.forward(300)  # Longitud de cada lado del cuadrado
        turtle.right(90)

def dibujar_rectangulo(x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("red")
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def dibujar_cruz_roja():
    # Dibuja la línea horizontal de la cruz
    dibujar_rectangulo(-50, 150, 100, 300)  # (x, y, ancho, alto)

    # Dibuja la línea vertical de la cruz
    dibujar_rectangulo(-150, 50, 300, 100)  # (x, y, ancho, alto)

# Configuración inicial
turtle.speed(1)  # Velocidad de dibujo

# Dibuja el cuadrado
dibujar_cuadrado()

# Dibuja la cruz roja
dibujar_cruz_roja()

# Finaliza el dibujo
turtle.hideturtle()  # Oculta la tortuga
turtle.done()  # Mantiene la ventana abierta
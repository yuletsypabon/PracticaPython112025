import turtle  # Importa la biblioteca turtle para dibujar
turtle.speed(1)
# Dibuja un cuadrado
def dibujar_cuadro():
    for _ in range(4):  # Repite 4 veces
        turtle.forward(150)  # Dibuja un lado del cuadrado
        turtle.right(90)  # Gira 90 grados a la derecha

# Dibuja el primer cuadro (superior izquierdo)
dibujar_cuadro()

# Mueve a la posición del segundo cuadro (superior derecho)
turtle.penup()  # Levanta el lápiz para no dibujar
turtle.goto(150, 0)  # Mueve a la derecha
turtle.pendown()  # Baja el lápiz para empezar a dibujar
dibujar_cuadro()  # Dibuja el segundo cuadro

# Mueve a la posición del tercer cuadro (inferior izquierdo)
turtle.penup()  # Levanta el lápiz
turtle.goto(0, -150)  # Mueve hacia abajo
turtle.pendown()  # Baja el lápiz
dibujar_cuadro()  # Dibuja el tercer cuadro

# Mueve a la posición del cuarto cuadro (inferior derecho)
turtle.penup()  # Levanta el lápiz
turtle.goto(150, -150)  # Mueve a la derecha y hacia abajo
turtle.pendown()  # Baja el lápiz
dibujar_cuadro()  # Dibuja el cuarto cuadro

# Finaliza el dibujo
turtle.done()  # Mantiene la ventana abierta
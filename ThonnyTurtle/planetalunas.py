import turtle  # Importa la biblioteca turtle para dibujar

# Configuración de la pantalla
screen = turtle.Screen()  # Crea una ventana para dibujar
screen.bgcolor("black")  # Establece el color de fondo a negro

# Crear el planeta
planeta = turtle.Turtle()  # Crea un objeto Turtle para el planeta
planeta.color("blue")  # Establece el color del planeta a azul
planeta.shape("circle")  # Cambia la forma del objeto a un círculo
planeta.shapesize(7)  # Aumenta el tamaño del planeta (radio de 100)
planeta.penup()  # Levanta el lápiz para no dibujar al mover
planeta.goto(0, 0)  # Mueve el planeta al centro de la pantalla

# Crear la luna 1
luna1 = turtle.Turtle()  # Crea un objeto Turtle para la luna 1
luna1.color("gray")  # Establece el color de la luna 1 a gris
luna1.shape("circle")  # Cambia la forma del objeto a un círculo
luna1.shapesize(1)  # Aumenta el tamaño de la luna 1 (radio de 10)
luna1.penup()  # Levanta el lápiz para no dibujar al mover
luna1.goto(100, 0)  # Mueve la luna 1 a la derecha del planeta

# Crear la luna 2
luna2 = turtle.Turtle()  # Crea un objeto Turtle para la luna 2
luna2.color("lightgray")  # Establece el color de la luna 2 a gris claro
luna2.shape("circle")  # Cambia la forma del objeto a un círculo
luna2.shapesize(0.7)  # Aumenta el tamaño de la luna 2 (radio de 7)
luna2.penup()  # Levanta el lápiz para no dibujar al mover
luna2.goto(-100, 0)  # Mueve la luna 2 a la izquierda del planeta

# Mantener la ventana abierta
turtle.done()  # Finaliza el dibujo y mantiene la ventana abierta
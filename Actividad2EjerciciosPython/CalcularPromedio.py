"""
Sumas todas las notas y divides el resultado entre la cantidad de notas.
"""

# Inicializar la suma de las notas
suma_notas = 0

# Solicitar 4 notas al usuario
for i in range(4):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    suma_notas += nota  # Sumar la nota a la suma total

# Calcular el promedio
promedio = suma_notas / 4

# Mostrar el promedio
print(f"El promedio de las notas es: {promedio:.2f}")
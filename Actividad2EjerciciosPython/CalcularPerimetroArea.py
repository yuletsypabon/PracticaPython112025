"""
El perímetro (circunferencia) de un círculo se calcula con 
la fórmula ( P = 2 \pi r ) y el 
área con ( A = \pi r^2 ), donde ( r ) es el radio y ( \pi ) es aproximadamente 3.14159.
"""

import math  # Importar la biblioteca math para usar pi

# Solicitar el radio del círculo
radio = float(input("Introduce el radio del círculo: "))

# Calcular el perímetro y el área
perimetro = 2 * math.pi * radio
area = math.pi * (radio ** 2)

# Mostrar los resultados
print(f"El perímetro del círculo es: {perimetro:.2f}")
print(f"El área del círculo es: {area:.2f}")
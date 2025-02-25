"""
Para convertir centímetros a pulgadas, puedes usar la relación ( 1 \text{ pulgada} = 2.54 \text{ centímetros} ). 
Por lo tanto, para convertir centímetros a pulgadas,
 divides la cantidad de centímetros entre 2.54.
"""

# Solicitar la medida en centímetros
centimetros = float(input("Introduce la medida en centímetros: "))

# Convertir a pulgadas
pulgadas = centimetros / 2.54

# Mostrar el resultado
print(f"{centimetros} centímetros son {pulgadas:.2f} pulgadas.")
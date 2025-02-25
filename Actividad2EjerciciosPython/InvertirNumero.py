"""
 Puedes convertir el número a una cadena (string) para poder invertirlo fácilmente. 
 Luego, puedes usar el índice negativo para acceder a los caracteres en orden inverso.
"""

# Solicitar un número de tres dígitos
numero = input("Introduce un número de tres dígitos: ")

# Verificar que el número tenga tres dígitos
if len(numero) == 3 and numero.isdigit():
    # Invertir el número
    numero_invertido = numero[::-1]
    print(f"El número invertido es: {numero_invertido}")
else:
    print("Por favor, asegúrate de ingresar un número de tres dígitos.") 
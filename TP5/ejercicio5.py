"""
La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo.
"""

import math

def calcular_raiz(numero_str) -> float:
    try:
        numero = float(numero_str)

        if numero < 0:
            raise ValueError("No se puede calcular la raiz cuadrada de un numero negativo.")

        return math.sqrt(numero)

    except ValueError:
        return -1

# Bloque principal
if __name__ == "__main__":
    entrada = input("Ingrese un numero para calcular su raiz cuadrada: ")
    resultado = calcular_raiz(entrada)

    if resultado == -1:
        print("Error: No se pudo calcular la raiz cuadrada. Verifique que el numero sea valido y no negativo.")
    else:
        print(f"La raiz cuadrada del numero es: {resultado}")

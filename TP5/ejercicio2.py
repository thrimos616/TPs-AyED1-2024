"""
Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error.
"""

def agregar_valores(texto1, texto2) -> float:
    try:
        valor1 = float(texto1)
        valor2 = float(texto2)
        return valor1 + valor2

    except ValueError:
        return -1


# Bloque principal
if __name__ == "__main__":
    entrada1 = input("Por favor, introduzca el primer numero real: ")
    entrada2 = input("Por favor, introduzca el segundo numero real: ")

    resultado = agregar_valores(entrada1, entrada2)

    if resultado == -1:
        print(
            f"Error: El resultado es {resultado}, ya que al menos uno de los textos no contiene un numero valido."
        )
    else:
        print(f"La suma de los valores ingresados es: {resultado}")

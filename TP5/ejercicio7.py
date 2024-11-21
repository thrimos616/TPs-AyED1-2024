"""
Escribir un programa que juegue con el usuario a adivinar un número. El programa
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar
el número. Si el usuario introduce algo que no sea un número se mostrará un
mensaje en pantalla y se lo contará como un intento más.
"""

import random

def generar_numero_aleatorio() -> int:
    return random.randint(1, 500)

def obtener_numero_usuario() -> int:
    try:
        return int(input("Ingrese un numero entre 1 y 500: "))
    except ValueError:
        raise ValueError("Debe ingresar un numero valido.")

def main():
    numero_secreto = generar_numero_aleatorio()
    intentos = 0

    print("Adivina el numero! Está entre 1 y 500.")

    while True:
        intentos += 1
        try:
            numero_usuario = obtener_numero_usuario()

            if numero_usuario < numero_secreto:
                print("El numero es mayor que el ingresado.")
            elif numero_usuario > numero_secreto:
                print("El numero es menor que el ingresado.")
            else:
                print(f"Felicidades! Adivinaste el numero con {intentos} intentos.")
                break

        except ValueError as error:
            print(f"Error: {error}. Esto cuenta como un intento mas.")

if __name__ == "__main__":
    main()

"""
Utilizar la técnica de listas por comprensión para construir una lista con todos los
números impares comprendidos entre 100 y 200
"""

import random as rn

def generar_lista_aleatoria() -> list:
    # Crea la lista de numeros aleatorios entre 100 y 200
    lista_numeros = [rn.randint(100, 200) for _ in range(rn.randint(1, 15))]
    return lista_numeros

def filtrar_impares(numeros: list) -> list:
    # Filtra los numeros impares entre 100 y 200
    return [n for n in numeros if 100 <= n <= 200 and n % 2 != 0]

def ejecutar_programa():
    lista = []

    while True:
        continuar = input(
            "Ingrese 0 para salir, o cualquier tecla para continuar: "
        )
        if continuar == "0":
            print("Fin del programa.")
            break

        lista = generar_lista_aleatoria()

        print("Lista generada aleatoriamente:\n")
        print(f"{lista}\n")

        impares = filtrar_impares(lista)
        print(
            "Lista con los números impares entre 100 y 200:\n"
        )
        print(impares)

if __name__ == "__main__":
    ejecutar_programa()

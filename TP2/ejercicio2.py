"""
2. Escribir funciones para:

a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa
a través del teclado.

b. Recibir una lista como parámetro y devolver True si la misma contiene algún
elemento repetido. La función no debe modificar la lista.

c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
únicos de la lista original, sin importar el orden.

Combinar estas tres funciones en un mismo programa.
"""

import random as rn

# Ejercicio a
def lista_al_aleatoria(num) -> list:
    lista_al_azar = []
    for i in range(num):
        lista_al_azar.append(rn.randint(1, 100))
    return lista_al_azar

# Ejercicio b
def repetido(lista) -> bool:
    repetido = False
    for i in range(len(lista)):
        if lista[i] == lista[-i-1]:
            repetido = True
    print(repetido)  

# Ejercicio c
def obtener_elementos_unicos(lista) -> list:
    return list(set(lista))

# Bloque principal
def main():
    try:
        num = int(input("Introduzca la cantidad de números aleatorios: "))
        if num <= 0:
            raise ValueError("El número debe ser positivo.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    lista = lista_al_aleatoria(num)
    print(f"Lista generada: {lista}")

    print("Elementos repetidos?:")
    repetido(lista)  

    lista_unica = obtener_elementos_unicos(lista)
    print(f"Lista con elementos unicos: {lista_unica}")

if __name__ == "__main__":
    main()
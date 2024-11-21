"""
Escribir una función que reciba una lista de números enteros como parámetro y la
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones 
relativas que cada elemento tiene en la lista original. Desarrollar también
un programa que permita verificar el comportamiento de la función. Por ejemplo,
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""

import random as rn

def generar_lista_aleatoria() -> list:
    lista_generada = []
    cantidad_elementos = rn.randint(1, 10)
    for _ in range(cantidad_elementos):
        lista_generada.append(rn.randint(1, 10))
    return lista_generada

def ajustar_lista(lista: list) -> list:
    total_suma = sum(lista)
    if total_suma == 0:
        raise ValueError("La suma de los elementos no puede ser 0.")
    return [numero / total_suma for numero in lista]

def comprobar_normalizacion():
    lista_inicial = generar_lista_aleatoria()
    print("Lista generada:", lista_inicial)

    try:
        lista_ajustada = ajustar_lista(lista_inicial)
        print("Lista ajustada:", lista_ajustada)
        print("Suma de los elementos de la lista ajustada:", sum(lista_ajustada))
    except ValueError:
        print("No es posible ajustar una lista cuya suma total es 0.")

if __name__ == "__main__":
    comprobar_normalizacion()

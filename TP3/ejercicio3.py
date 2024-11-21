"""
Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N^2), 
de tal forma que ningún número se repita. Imprimir la matriz por pantalla
"""

import random as rn

def crear_matriz_aleatoria(tamano: int) -> list[list[int]]:
    # Genera una lista de numeros aleatorios unicos
    numeros_disponibles = list(range(tamano * tamano))
    rn.shuffle(numeros_disponibles)

    # Craftea la matriz 
    matriz_resultante = [numeros_disponibles[i * tamano:(i + 1) * tamano] for i in range(tamano)]
    return matriz_resultante

def mostrar_matriz(matriz: list[list[int]]) -> None:
    # Imprime la matriz 
    for fila in matriz:
        print(" ".join(f"{num:2}" for num in fila))

if __name__ == "__main__":
    tamano_matriz = int(input("Ingrese el tamaño de la matriz: "))
    matriz_generada = crear_matriz_aleatoria(tamano_matriz)
    mostrar_matriz(matriz_generada)

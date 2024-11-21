"""
Las siguientes matrices responden distintos patrones de relleno. Desarrollar funciones que generen cada una de ellas sin intervención humana y escribir un programa
que las invoque e imprima por pantalla. El tamaño de las matrices debe establecerse como N x N, donde N se ingresa a través del teclado.
"""

from tabulate import tabulate

def crear_matriz(tamanio):
    matriz = [[0 for _ in range(tamanio)] for _ in range(tamanio)]
    for fila in range(tamanio):
        for columna in range(tamanio - fila):
            matriz[fila][columna] = tamanio - fila - columna
    return matriz

def ejecutar_programa():
    tamano = int(input("Ingrese el tamaño de la matriz (N x N): "))
    print(tabulate(crear_matriz(tamano)))

if __name__ == "__main__":
    ejecutar_programa()

"""
1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
teclado.
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
una lista con los números de las mismas.
"""

def crear_matriz(tamanio):
    matriz_resultante = []
    for i in range(tamanio):
        fila_temp = []
        for j in range(tamanio):
            valor = int(input(f"Ingrese el valor para la posicion [{i}][{j}]: "))
            fila_temp.append(valor)
        matriz_resultante.append(fila_temp)
    return matriz_resultante

def ordenar_columnas(matriz):
    for fila in matriz:
        fila.sort()
    return matriz

def intercambiar_posiciones(matriz, index1, index2):
    matriz[index1], matriz[index2] = matriz[index2], matriz[index1]
    return matriz

def ejecutar_programa():
    tamanio = int(input("Ingrese el tamaño de la matriz cuadrada: "))
    matriz = crear_matriz(tamanio)
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    matriz_ordenada = ordenar_columnas(matriz)
    print("Matriz con filas ordenadas:")
    for fila in matriz_ordenada:
        print(fila)

    index1 = int(input("Ingrese el numero de la primera fila a intercambiar: "))
    index2 = int(input("Ingrese el numero de la segunda fila a intercambiar: "))
    matriz_intercambiada = intercambiar_posiciones(matriz, index1, index2)
    print("Matriz despues de intercambiar las filas:")
    for fila in matriz_intercambiada:
        print(fila)

if __name__ == "__main__":
    ejecutar_programa()

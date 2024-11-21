"""
Eliminar de una lista de números enteros aquellos valores que se encuentren en
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
resultante. La función debe modificar la lista original sin crear una copia modificada.
"""

def filtrar_elementos(lista_base, elementos_a_eliminar):
    for elemento in elementos_a_eliminar:
        while elemento in lista_base:
            lista_base.remove(elemento)

def procesar_listas():
    # Crea la lista principal
    numeros_principales = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Lista principal:", numeros_principales)

    # Crea la lista de elementos por filtrar
    elementos_a_eliminar = [2, 4, 6, 8]
    print("Elementos a eliminar:", elementos_a_eliminar)

    # Invoca la funcion para filtrar los elementos
    filtrar_elementos(numeros_principales, elementos_a_eliminar)

    # Muestra la lista filtrada
    print("Lista final:", numeros_principales)

if __name__ == "__main__":
    procesar_listas()
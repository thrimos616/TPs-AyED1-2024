"""
El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la
posición que ocupan, utilizando el método index. Si el número no pertenece a la
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
"""

def cargar_lista() -> list[int]:
    numeros = []
    print("Ingrese numeros enteros para la lista (termine con -1):")
    while True:
        try:
            valor = int(input("> "))
            if valor == -1:
                break
            numeros.append(valor)
        except ValueError:
            print("Error: Debe ingresar un numero entero. Intente nuevamente.")
    return numeros


def buscar_indice(lista: list[int], objetivo: int) -> int:
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    raise ValueError("El numero no esta en la lista.")


def main():
    lista_numeros = cargar_lista()
    print(f"\nLista cargada: {lista_numeros}")

    errores = 0

    while errores < 3:
        try:
            numero_buscar = int(input("\nIngrese el numero que desea buscar en la lista: "))
            posicion = buscar_indice(lista_numeros, numero_buscar)
            print(f"El número {numero_buscar} se encuentra en la posicion {posicion}.")
        except ValueError as error:
            errores += 1
            print(f"Error: {error}. Intentos fallidos: {errores}/3.")

        if errores == 3:
            print("\nSe han alcanzado tres errores consecutivos. Finalizando programa.")
            break


if __name__ == "__main__":
    main()

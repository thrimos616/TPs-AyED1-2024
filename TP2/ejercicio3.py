"""
Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista. 
"""

# Genera una lista con los cuadrados de los numeros entre 1 y N
def lista_cuadrados(n) -> list:
    lista_cuadrados = []
    for i in range(1, n + 1):
        lista_cuadrados.append(i ** 2)
    return lista_cuadrados

# Imprime los ultimos 10 valores de la lista
def imprimir_ultimos_10(lista):
    print("Últimos 10 valores de la lista:")
    print(lista[-10:])

# Bloque principal
def main():
    try:
        n = int(input("Ingrese el valor de N: "))
        if n <= 0:
            raise ValueError("El número debe ser positivo.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    lista = lista_cuadrados(n)
    print(f"Lista generada: {lista}")

    imprimir_ultimos_10(lista)

if __name__ == "__main__":
    main()
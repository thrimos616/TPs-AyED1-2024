"""
Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función. 
"""

def esta_en_orden(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

def probar_listas():
    # Listas de prueba
    listas_a_probar = [
        ([1, 2, 3], "Lista A"),
        ([3, 2, 1], "Lista B"),
        (['b', 'a'], "Lista C"),
        (['a', 'b', 'c'], "Lista D"),
        ([1, 2, 2, 3], "Lista E"),
        ([10, 20, 30, 40, 50], "Lista F")
    ]
    
    print("Comprobando si las listas están ordenadas:")
    for lista, nombre in listas_a_probar:
        print(f"{nombre}: {lista} -> Ordenada: {esta_en_orden(lista)}")

if __name__ == "__main__":
    probar_listas()

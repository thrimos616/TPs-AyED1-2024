"""
Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario
y una lista de claves. La función debe eliminar del diccionario todas las claves
contenidas en la lista, devolviendo el diccionario modificado y un número entero
que represente la cantidad de claves eliminadas. Desarrollar también un programa
para verificar su comportamiento
"""

def eliminarclaves(diccionario, claves_a_eliminar):
    claves_eliminadas = 0
    
    for clave in claves_a_eliminar:
        if clave in diccionario:
            diccionario[clave] = None  
            claves_eliminadas += 1
    
    diccionario = {k: v for k, v in diccionario.items() if v is not None}
    
    return diccionario, claves_eliminadas

# Bloque principal
def main():
    diccionario = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5
    }
    
    claves_a_eliminar = ['b', 'd', 'z']
    
    print("Diccionario original:", diccionario)
    
    diccionario_modificado, claves_eliminadas = eliminarclaves(diccionario, claves_a_eliminar)
    
    print("\nDiccionario despues de eliminar claves:", diccionario_modificado)
    print(f"\nNumero de claves eliminadas: {claves_eliminadas}")

if __name__ == "__main__":
    main()

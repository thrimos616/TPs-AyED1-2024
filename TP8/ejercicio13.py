"""
Escribir una función buscarclave() que reciba como parámetros un diccionario y un
valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el diccionario. Comprobar el comportamiento de la función mediante un programa apropiado.
"""

def buscarclave(diccionario, valor):
    lista_claves = []  
    for clave in diccionario:  
        if diccionario[clave] == valor:  
            lista_claves.append(clave) 
    return lista_claves

# Bloque principal
def main():
    diccionario_precios = {
        "cuaderno": 100,
        "lapiz": 20,
        "goma": 20,
        "resma": 150,
        "lapicera": 30,
        "fibron": 30
    }
    
    valor_buscar = 20
    
    claves_encontradas = buscarclave(diccionario_precios, valor_buscar)
    
    if claves_encontradas:
        print(f"Las claves que apuntan al valor {valor_buscar} son: {claves_encontradas}")
    else:
        print(f"No se encontraron claves para el valor {valor_buscar}.")

if __name__ == "__main__":
    main()

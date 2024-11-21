"""
Una librería almacena su lista de precios en un diccionario. Diseñar un programa
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
costoso que venden en el comercio.
"""

def incrementar_precio_cuadernos(diccionario_precios):
    for producto, precio in diccionario_precios.items():
        if "cuaderno" in producto.lower():  
            diccionario_precios[producto] = precio * 1.15  
    
    return diccionario_precios

def item_mas_costoso(diccionario_precios):

    producto_mas_costoso = max(diccionario_precios, key=diccionario_precios.get)
    precio_mas_costoso = diccionario_precios[producto_mas_costoso]
    
    return producto_mas_costoso, precio_mas_costoso

# Bloque principañ
def main():
    precios = {
        "cuaderno A5": 150,
        "cuaderno A4": 200,
        "lapiz": 30,
        "lapicera": 50,
        "resma de A4": 450,
        "cuaderno de notas": 120
    }
    
    precios_actualizados = incrementar_precio_cuadernos(precios)
    
    print("Listado de precios actualizados:")
    for producto, precio in precios_actualizados.items():
        print(f"{producto}: ${precio:.2f}")
    
    producto_mas_costoso, precio_mas_costoso = item_mas_costoso(precios_actualizados)
    
    print(f"\nEl item mas costoso es '{producto_mas_costoso}' con un precio de ${precio_mas_costoso:.2f}")


if __name__ == "__main__":
    main()

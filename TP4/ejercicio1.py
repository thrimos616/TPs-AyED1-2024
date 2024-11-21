"""
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita
verificar su funcionamiento.
"""

def verificar_capicua(texto):
    comienzo = 0
    final = len(texto) - 1
    
    while comienzo < final:
        if texto[comienzo] != texto[final]:
            return False
        comienzo += 1
        final -= 1
    
    return True

# Bloque principal
if __name__ == "__main__":
    texto = input("Ingrese una cadena de caracteres: ")
    if verificar_capicua(texto):
        print(f"La cadena '{texto}' es capicúa.")
    else:
        print(f"La cadena '{texto}' no es capicúa.")

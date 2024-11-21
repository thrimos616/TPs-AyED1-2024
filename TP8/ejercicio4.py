"""
Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento. Considerar
el uso de conjuntos para resolver este ejercicio
"""

def encajan(ficha1, ficha2):
    return bool(set(ficha1) & set(ficha2))

# Bloque principal
def main():
    ficha1 = tuple(map(int, input("Ingrese los numeros de la primera ficha (formato: a,b): ").split(',')))
    ficha2 = tuple(map(int, input("Ingrese los numeros de la segunda ficha (formato: a,b): ").split(',')))
    
    if encajan(ficha1, ficha2):
        print(f"Las fichas {ficha1} y {ficha2} encajan.")
    else:
        print(f"Las fichas {ficha1} y {ficha2} no encajan.")

if __name__ == "__main__":
    main()

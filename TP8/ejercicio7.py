"""
Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
inexistentes.
"""

def eliminar_numero_conjunto(conjunto):
    while True:
        try:
            numero = int(input("Ingrese un numero entre 0 y 9 para eliminar (o -1 para finalizar): "))
            
            if numero == -1:
                print("Proceso finalizado.")
                break
            
            if numero < 0 or numero > 9:
                print("Por favor, ingrese un numero entre 0 y 9.")
                continue
            
            conjunto.remove(numero)
            
            print(f"Conjunto despues de la eliminacion: {conjunto}")
        
        except ValueError:
            print("Error: Por favor ingrese un numero entero valido.")
        except KeyError:
            print("Error: El numero no esta en el conjunto.")
    
# Bloque principal
def main():
    conjunto = set(range(10))
    
    print(f"Conjunto inicial: {conjunto}")
    
    eliminar_numero_conjunto(conjunto)

if __name__ == "__main__":
    main()

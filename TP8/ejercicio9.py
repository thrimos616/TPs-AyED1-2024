"""
Escribir un programa que permita ingresar un número entero N y genere un
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la
tabla de multiplicar con el formato apropiado.
"""

def generar_tabla_multiplicar(n):
    return {i: n * i for i in range(1, 13)}

# Bloque pincipal
def main():
    numero = int(input("Ingrese un numero entero para ver su tabla de multiplicar: "))
    
    tabla = generar_tabla_multiplicar(numero)
    
    print(f"\nTabla de multiplicar de {numero}:")
    for i in range(1, 13):
        print(f"{numero} x {i} = {tabla[i]}")

if __name__ == "__main__":
    main()

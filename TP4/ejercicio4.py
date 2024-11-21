"""
Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En
qué cambiaría la función si el rango de valores fuese diferente?
"""

def convertir_a_romano(numero):
    simbolos_romanos = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    romanizado = ""
    
    for valor, simbolo in simbolos_romanos:
        while numero >= valor:
            romanizado += simbolo
            numero -= valor
    
    return romanizado

def ejecutar_conversion():
    numero = int(input("Introduce un numero entre 0 y 3999: "))
    print(f"El numero en formato romano es: {convertir_a_romano(numero)}")

if __name__ == "__main__":
    ejecutar_conversion()

"""
Los números de claves de dos cajas fuertes están intercalados dentro de un número
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa
para obtener ambas claves, donde la primera se construye con los dígitos ubicados
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en
posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89
"""

def extraer_claves(clave_maestra):
    clave_a = ""
    clave_b = ""
    
    for indice in range(len(clave_maestra)):
        if (indice + 1) % 2 != 0:
            clave_a += clave_maestra[indice]
        else:
            clave_b += clave_maestra[indice]
    
    return clave_a, clave_b

clave_maestra = input("Introduce el código maestro: ")
clave_a, clave_b = extraer_claves(clave_maestra)
print(f"Clave A: {clave_a}")
print(f"Clave B: {clave_b}")

"""
Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
misma tiene 80 columnas.
"""

def alinear_cadena(cadena: str) -> None:
    ancho = 80
    longitud_cadena = len(cadena)
    espacios_izquierda = (ancho - longitud_cadena) // 2
    cadena_centrada = (" " * espacios_izquierda) + cadena
    print(cadena_centrada)

def ejecutar_programa():
    while True:
        entrada = input("Ingrese una cadena o '0' para salir: ")
        if entrada == '0':
            print("\nFinalizando programa.")
            break
        alinear_cadena(entrada)

if __name__ == "__main__":
    ejecutar_programa()

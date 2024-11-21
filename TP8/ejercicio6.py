"""
Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
ordenadas según su longitud. Los signos de puntuación no deben afectar el
proceso.
"""

def procesar_frase(frase):
    signos_puntuacion = ".,!?;:()[]{}\"'"

    # Eliminar los signos de la frase
    frase_sin_puntuacion = ''.join(caracter for caracter in frase if caracter not in signos_puntuacion)
    
    palabras = frase_sin_puntuacion.split()

    conjunto_palabras = set(palabras)
    
    palabras_ordenadas = sorted(conjunto_palabras, key=len)
    
    return palabras_ordenadas

# Bloque principal
def main():


    frase = input("Ingrese una frase: ")

    resultado = procesar_frase(frase)
    
    print("Palabras ordenadas por longitud:")
    for palabra in resultado:
        print(palabra)

if __name__ == "__main__":
    main()

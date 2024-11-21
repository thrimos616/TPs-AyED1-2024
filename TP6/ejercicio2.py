"""
Escribir un programa que permita dividir un archivo de texto cualquiera en partes
que se puedan enviar por correo electrónico. El tamaño máximo de las partes se
ingresa por teclado. Los nombres de los archivos generados deben respetar el
nombre original con el agregado de un sufijo que indique de qué parte se trata.
Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuarse después del delimitador del mismo. Mostrar un mensaje de error si el proceso no
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en
memoria.
"""

def dividir_archivo(nombre_archivo, tamano_maximo) -> None:
    try:
        parte = 1  # Contador para los archivos de salida
        tamano_actual = 0  # Tamaño acumulado de la parte actual

        with open(nombre_archivo, "r", encoding="utf-8") as archivo_entrada:
            nombre_base = nombre_archivo.rsplit(".", 1)[0]
            archivo_salida = open(f"{nombre_base}_parte{parte}.txt", "w", encoding="utf-8")

            for linea in archivo_entrada:
                if tamano_actual + len(linea) > tamano_maximo:
                    archivo_salida.close()  
                    parte += 1  
                    tamano_actual = 0 
                    archivo_salida = open(f"{nombre_base}_parte{parte}.txt", "w", encoding="utf-8")

                archivo_salida.write(linea)
                tamano_actual += len(linea)

            archivo_salida.close()

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
    except IOError as e:
        print(f"Error de lectura/escritura: {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

# Bloque principal
def main() -> None:
    try:
        archivo = input("Ingrese el nombre del archivo a dividir: ")
        tamano = int(input("Ingrese el tamaño maximo por parte (en bytes): "))

        if tamano <= 0:
            raise ValueError("El tamaño maximo debe ser mayor a 0.")

        dividir_archivo(archivo, tamano)
        print("El archivo fue dividido exitosamente.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

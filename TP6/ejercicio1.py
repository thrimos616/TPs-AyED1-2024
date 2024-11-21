"""
Escribir un programa que lea un archivo de texto conteniendo un conjunto de apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los
terminados en "EZ".
"""

def leer_archivo(nombre_archivo) -> list:
    try:
        with open(nombre_archivo, "r") as archivo:
            return [linea.strip() for linea in archivo]
    except FileNotFoundError:
        raise FileNotFoundError(f"No se pudo encontrar el archivo: {nombre_archivo}")


def clasificar_registro(registro) -> str:
    apellido = registro.split(",")[0].strip()
    if apellido.endswith("IAN"):
        return "ARMENIA.TXT"
    elif apellido.endswith("INI"):
        return "ITALIA.TXT"
    elif apellido.endswith("EZ"):
        return "ESPAÑA.TXT"
    else:
        return None


def escribir_archivo(nombre_archivo, registros) -> None:
    with open(nombre_archivo, "w") as archivo:
        for registro in registros:
            archivo.write(registro + "\n")


def procesar_archivo(nombre_archivo) -> None:
    registros_armenia = []
    registros_italia = []
    registros_espana = []

    registros = leer_archivo(nombre_archivo)
    for registro in registros:
        archivo_destino = clasificar_registro(registro)
        if archivo_destino == "ARMENIA.TXT":
            registros_armenia.append(registro)
        elif archivo_destino == "ITALIA.TXT":
            registros_italia.append(registro)
        elif archivo_destino == "ESPAÑA.TXT":
            registros_espana.append(registro)

    escribir_archivo("ARMENIA.TXT", registros_armenia)
    escribir_archivo("ITALIA.TXT", registros_italia)
    escribir_archivo("ESPAÑA.TXT", registros_espana)

# Bloque principal
if __name__ == "__main__":
    archivo_entrada = input("Ingrese el nombre del archivo con los registros: ")
    try:
        procesar_archivo(archivo_entrada)
        print("Los registros han sido clasificados y escritos en los archivos correspondientes.")
    except FileNotFoundError as error:
        print(f"Error: {error}")

"""
Muy larga la consgina ajdhkajsdhakj
"""

def GrabarRangoAlturas(nombre_archivo) -> None:
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            while True:
                disciplina = input("Ingrese el nombre de la disciplina (o 'fin' para terminar): ")
                if disciplina.lower() == "fin":
                    break
                
                archivo.write(disciplina + "\n")
                while True:
                    try:
                        altura = input(f"Ingrese la altura de un atleta para {disciplina} (o 'fin' para terminar): ")
                        if altura.lower() == "fin":
                            break
                        archivo.write(altura + "\n")
                    except ValueError:
                        print("Error: Ingrese un numero valido.")
    except Exception as e:
        print(f"Error al grabar los datos: {e}")


def GrabarPromedio(nombre_archivo, archivo_promedio) -> None:
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo_entrada:
            with open(archivo_promedio, "w", encoding="utf-8") as archivo_salida:
                disciplina = None
                alturas = []

                for linea in archivo_entrada:
                    if not linea.strip():
                        continue

                    if linea[0].isalpha():  
                        if disciplina:
                            promedio = sum(alturas) / len(alturas) if alturas else 0
                            archivo_salida.write(f"{disciplina}\n")
                            archivo_salida.write(f"{promedio:.2f}\n")
                        disciplina = linea.strip()
                        alturas = []
                    else:
                        try:
                            altura = float(linea.strip())
                            alturas.append(altura)
                        except ValueError:
                            continue 

                if disciplina:  
                    promedio = sum(alturas) / len(alturas) if alturas else 0
                    archivo_salida.write(f"{disciplina}\n")
                    archivo_salida.write(f"{promedio:.2f}\n")
    except Exception as e:
        print(f"Error al grabar los promedios: {e}")


def MostrarMasAltos(archivo_promedio) -> None:
    try:
        total_promedio = 0
        total_disciplinas = 0
        promedios = []

        with open(archivo_promedio, "r", encoding="utf-8") as archivo:
            disciplina = None
            for linea in archivo:
                if not linea.strip():
                    continue
                if linea[0].isalpha():  # Disciplina
                    disciplina = linea.strip()
                else:  # Promedio
                    promedio = float(linea.strip())
                    promedios.append((disciplina, promedio))
                    total_promedio += promedio
                    total_disciplinas += 1

        if total_disciplinas == 0:
            print("No se encontraron disciplinas.")
            return

        promedio_general = total_promedio / total_disciplinas
        print(f"\nPromedio general de alturas: {promedio_general:.2f}\n")

        print("Disciplinas con alturas superiores al promedio general:")
        for disciplina, promedio in promedios:
            if promedio > promedio_general:
                print(f"{disciplina}: {promedio:.2f}")
    except Exception as e:
        print(f"Error al mostrar los atletas mas altos: {e}")

# Bloque principal
def main() -> None:
    try:
        archivo_rango = "rango_alturas.txt"
        archivo_promedio = "promedios_alturas.txt"

        GrabarRangoAlturas(archivo_rango)
        GrabarPromedio(archivo_rango, archivo_promedio)
        MostrarMasAltos(archivo_promedio)

    except Exception as e:
        print(f"Error en el proceso: {e}")


if __name__ == "__main__":
    main()

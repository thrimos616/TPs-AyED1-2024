"""
Desarrollar una función que devuelva una cadena de caracteres con el nombre del
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
Devolver una cadena vacía si el número de mes es inválido. La detección de meses
inválidos deberá realizarse a través de excepciones.
"""

def nombre_mes(numero_mes) -> str:
    try:
        meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]

        indice = int(numero_mes) - 1

        if indice < 0 or indice >= len(meses):
            raise ValueError("Numero de mes fuera de rango")

        return meses[indice]

    except ValueError:
        return ""


# Bloque principal
if __name__ == "__main__":
    numero = input("Ingrese el numero del mes (1-12): ")
    mes = nombre_mes(numero)

    if mes == "":
        print("Error: El numero ingresado no corresponde a un mes valido.")
    else:
        print(f"El mes correspondiente es: {mes}")

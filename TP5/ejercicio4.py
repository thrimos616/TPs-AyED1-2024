"""
Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
un programa para imprimir los números enteros entre 1 y 100000, y que solicite
confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
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

"""
Escribir una función que reciba como parámetro una tupla conteniendo una fecha
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. La función debe contemplarse que el año se ingrese en dos
dígitos, los que serán interpretados según un año de corte definido dentro del
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030"
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y
mostrar el resultado.
"""

def fecha_extendida(fecha, anio_corte=30):
    dia = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31",]
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    dia, mes, anio = fecha
    
    if anio <= anio_corte:
        anio = 2000 + anio
    elif anio > 30:
        if anio < 100:
            anio = 1900 + anio
    return f"{dia} de {meses[mes-1]} de {anio}"

# Bloque principal
def main():
    try:
        # Ingresar la fecha (dia, mes, año)
        dia = int(input("Ingrese el dia: "))
        mes = int(input("Ingrese el mes (numero): "))
        anio = int(input("Ingrese el año (puede ser de 2 o 4 digitos): "))
        
        if 1 <= dia <= 31 and 1 <= mes <= 12:
            fecha = (dia, mes, anio)
            print(fecha_extendida(fecha))
        else:
            print("Fecha invalida. Dia o mes incorrecto/s.")
    except ValueError:
        print("Error: Por favor ingrese numeros validos.")

if __name__ == "__main__":
    main()

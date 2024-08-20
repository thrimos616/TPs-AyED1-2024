def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def fecha_valida(dia, mes, anio):
    # Verifica si el año es valido
    if anio < 0:
        print("Introduzca un año que sea después de Cristo")
        return False

    # Verifica si el mes es valido
    if mes < 1 or mes > 12:
        print("El mes es invalido")
        return False

    # Determina el numero de dias del mes
    if mes in [1, 3, 5, 7, 8, 10, 12]:  # Meses con 31 dias
        max_dias = 31
    elif mes in [4, 6, 9, 11]:  # Meses con 30 dias
        max_dias = 30
    elif mes == 2:  # Febrero
        if es_bisiesto(anio):
            max_dias = 29  
        else:
            max_dias = 28  

    # Verifica si el dia es valido para el mes dado
    if dia < 1 or dia > max_dias:
        print("El día es inválido")
        return False

    return True

def verificacionPrograma():
    if fecha_valida(dia, mes, anio) == True:
        print("La fecha introducida es válida")
    else:
        print("La fecha introducida es inválida")

# Bloque principal
dia = int(input("Introduzca un día: "))
mes = int(input("Introduzca un mes: "))
anio = int(input("Introduzca un año: "))

# Programa para verificar
verificacionPrograma()
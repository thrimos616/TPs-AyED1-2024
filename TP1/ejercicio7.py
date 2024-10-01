def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def dias_en_mes(mes, anio):
    if mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28
    elif mes in {4, 6, 9, 11}:
        return 30
    else:
        return 31

def dia_siguiente(dia, mes, anio):
    dia += 1
    
    if dia > dias_en_mes(mes, anio):
        dia = 1
        mes += 1
        
        if mes > 12:
            mes = 1
            anio += 1
    
    return dia, mes, anio

def sumar_dias(dias, mes, anio):
    for _ in range():
        dias, mes, anio = dia_siguiente(dias, mes, anio)
    return dia, mes, anio

# Bloque principal
dia = int(input("Introduzca un día: "))
mes = int(input("Introduzca un mes: "))
anio = int(input("Introduzca un año: "))
print(dia_siguiente(dia, mes, anio))
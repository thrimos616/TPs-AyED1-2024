"""
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas
"""

from datetime import datetime, timedelta

def ingresar_fecha():
    while True:
        try:
            fecha_str = input("Ingrese una fecha en formato DDMMAAAA: ")
            # Validación del formato de fecha
            fecha = datetime.strptime(fecha_str, "%d%m%Y")
            # Retorna la fecha como una tupla (día, mes, año)
            return (fecha.day, fecha.month, fecha.year)
        except ValueError:
            print("Error: Fecha invalida. Asegurese de seguir el formato DDMMAAAA.")

def sumar_dias(fecha, dias):
    try:
        fecha_dt = datetime(fecha[2], fecha[1], fecha[0])  # Convertir la tupla a datetime
        nueva_fecha = fecha_dt + timedelta(days=dias)  # Sumar los dias
        return (nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)
    except Exception as e:
        print(f"Error al sumar los dias: {e}")
        return None

def ingresar_horario():
    while True:
        try:
            horario_str = input("Ingrese un horario en formato HH:MM: ")
            # Validación del formato de hora
            horario = datetime.strptime(horario_str, "%H:%M")
            return (horario.hour, horario.minute)
        except ValueError:
            print("Error: Horario invalido. Asegurese de seguir el formato HH:MM.")

def diferencia_horarios(hora1, hora2):
    try:
        hora1_dt = datetime(2023, 1, 1, hora1[0], hora1[1])  
        hora2_dt = datetime(2023, 1, 1, hora2[0], hora2[1])
        
        diferencia = hora1_dt - hora2_dt
        
        
        if diferencia.total_seconds() < 0:
            diferencia = hora1_dt - (hora2_dt + timedelta(days=1)) 

        # Asegurarse de que la diferencia no exceda las 24 horas
        if diferencia.total_seconds() > 86400:  
            print("Error: La diferencia no puede superar las 24 horas.")
            return None

        horas_diferencia = diferencia.total_seconds() // 3600  # Obtener las horas
        minutos_diferencia = (diferencia.total_seconds() % 3600) // 60  # Obtener los minutos
        return (int(horas_diferencia), int(minutos_diferencia))
    except Exception as e:
        print(f"Error al calcular la diferencia de horarios: {e}")
        return None

# Bloque principal
def main():

    print("Ingresando fecha...")
    fecha = ingresar_fecha()
    print(f"Fecha ingresada: {fecha[0]:02d}/{fecha[1]:02d}/{fecha[2]}")

    dias_a_sumar = int(input("Ingrese la cantidad de dias a sumar a la fecha: "))
    nueva_fecha = sumar_dias(fecha, dias_a_sumar)
    print(f"Fecha después de sumar {dias_a_sumar} días: {nueva_fecha[0]:02d}/{nueva_fecha[1]:02d}/{nueva_fecha[2]}")

    print("\nIngresando primer horario...")
    hora1 = ingresar_horario()
    print(f"Primer horario ingresado: {hora1[0]:02d}:{hora1[1]:02d}")

    print("\nIngresando segundo horario...")
    hora2 = ingresar_horario()
    print(f"Segundo horario ingresado: {hora2[0]:02d}:{hora2[1]:02d}")

    diferencia = diferencia_horarios(hora1, hora2)
    if diferencia:
        print(f"La diferencia entre los horarios es: {diferencia[0]} horas y {diferencia[1]} minutos")

if __name__ == "__main__":
    main()

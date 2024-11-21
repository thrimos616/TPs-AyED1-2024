"""
Demasiado larga la consigna ajdhsajk
"""

import csv
from datetime import datetime

# Función para registrar huéspedes en un archivo CSV
def registrar_huespedes():
    """
    Registra huespedes en un archivo CSV. La entrada termina cuando el DNI ingresado es -1.
    """
    with open('huespedes.csv', mode='w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["DNI", "Apellido y Nombre", "Fecha de Ingreso", "Fecha de Egreso", "Cantidad de Ocupantes"])
        
        while True:
            dni = int(input("Ingrese DNI del huésped (ingrese -1 para finalizar): "))
            if dni == -1:
                break
            
            apellido_nombre = input("Ingrese el apellido y nombre del huésped: ")
            fecha_ingreso = input("Ingrese la fecha de ingreso (DDMMAAAA): ")
            fecha_egreso = input("Ingrese la fecha de egreso (DDMMAAAA): ")
            cantidad_ocupantes = int(input("Ingrese la cantidad de ocupantes: "))
            
            try:
                fecha_ingreso = datetime.strptime(fecha_ingreso, "%d%m%Y")
                fecha_egreso = datetime.strptime(fecha_egreso, "%d%m%Y")
                if fecha_egreso <= fecha_ingreso:
                    print("Error: La fecha de egreso debe ser mayor que la de ingreso.")
                    continue
            except ValueError:
                print("Error: Las fechas ingresadas no son validas.")
                continue
            
            writer.writerow([dni, apellido_nombre, fecha_ingreso.strftime("%d%m%Y"), fecha_egreso.strftime("%d%m%Y"), cantidad_ocupantes])
            print("Huesped registrado correctamente.")

# Función para leer el archivo de huéspedes y asignar habitaciones
def asignar_habitaciones():
   
    habitaciones_disponibles = [(piso, habitacion) for piso in range(1, 11) for habitacion in range(1, 7)]
    asignaciones = []
    
    with open('huespedes.csv', mode='r') as archivo:
        reader = csv.reader(archivo)
        next(reader)  
        
        for fila in reader:
            dni, apellido_nombre, fecha_ingreso, fecha_egreso, cantidad_ocupantes = fila
            dni = int(dni)
            cantidad_ocupantes = int(cantidad_ocupantes)
            
            # Asignar habitación
            if habitaciones_disponibles:
                asignacion = habitaciones_disponibles.pop(0)
                asignaciones.append((dni, apellido_nombre, asignacion, cantidad_ocupantes, fecha_ingreso, fecha_egreso))
            else:
                print(f"No hay mas habitaciones disponibles para {apellido_nombre}.")
    
    return asignaciones

# Funcion para mostrar el piso con más habitaciones ocupadas
def piso_con_mayor_ocupacion(asignaciones):
    pisos_ocupados = [0] * 10 
    for _, _, asignacion, _, _, _ in asignaciones:
        piso, _ = asignacion
        pisos_ocupados[piso - 1] += 1
    
    max_ocupacion = max(pisos_ocupados)
    piso_maximo = pisos_ocupados.index(max_ocupacion) + 1
    print(f"El piso con mas habitaciones ocupadas es el piso {piso_maximo} con {max_ocupacion} habitaciones ocupadas.")


def contar_habitaciones_vacias():
    total_habitaciones = 60
    ocupadas = 0
    with open('huespedes.csv', mode='r') as archivo:
        reader = csv.reader(archivo)
        next(reader)  
        ocupadas = sum(1 for _ in reader)
    
    habitaciones_vacias = total_habitaciones - ocupadas
    print(f"Hay {habitaciones_vacias} habitaciones vacias en todo el hotel.")


def piso_con_mas_personas(asignaciones):
    personas_por_piso = [0] * 10  
    for _, _, asignacion, cantidad_ocupantes, _, _ in asignaciones:
        piso, _ = asignacion
        personas_por_piso[piso - 1] += cantidad_ocupantes
    
    max_personas = max(personas_por_piso)
    piso_maximo = personas_por_piso.index(max_personas) + 1
    print(f"El piso con mas personas alojadas es el piso {piso_maximo} con {max_personas} personas.")

def proxima_habitacion_desocuparse(asignaciones, fecha_actual):
    fecha_actual = datetime.strptime(fecha_actual, "%d%m%Y")
    habitaciones_desocupadas = [(dni, apellido_nombre, asignacion, fecha_egreso) 
                                for dni, apellido_nombre, asignacion, _, _, fecha_egreso in asignaciones 
                                if datetime.strptime(fecha_egreso, "%d%m%Y") <= fecha_actual]
    
    if habitaciones_desocupadas:
        print("Las siguientes habitaciones se desocuparan pronto:")
        for dni, apellido_nombre, asignacion, fecha_egreso in habitaciones_desocupadas:
            print(f"{apellido_nombre} (DNI: {dni}) - Habitacion {asignacion} - Fecha de Egreso: {fecha_egreso}")
    else:
        print("No hay habitaciones que se desocuparan en el dia actual.")

def mostrar_huespedes_por_dias(asignaciones):
    asignaciones.sort(key=lambda x: (datetime.strptime(x[5], "%d%m%Y") - datetime.strptime(x[4], "%d%m%Y")).days)
    
    print("Lista de huespedes ordenada por cantidad de dias de alojamiento:")
    for _, apellido_nombre, asignacion, _, fecha_ingreso, fecha_egreso in asignaciones:
        dias = (datetime.strptime(fecha_egreso, "%d%m%Y") - datetime.strptime(fecha_ingreso, "%d%m%Y")).days
        print(f"{apellido_nombre} - Habitacion {asignacion} - {dias} dias de alojamiento")

# Bloque principal
def main():
    registrar_huespedes()  # Paso 1: Registrar huespedes
    asignaciones = asignar_habitaciones()  # Paso 2: Asignar habitaciones
    piso_con_mayor_ocupacion(asignaciones)  # Paso 3: Piso con mas habitaciones ocupadas
    contar_habitaciones_vacias()  # Paso 4: Habitaciones vacias
    piso_con_mas_personas(asignaciones)  # Paso 5: Piso con mas personas
    fecha_actual = input("Ingrese la fecha actual (DDMMAAAA): ")
    proxima_habitacion_desocuparse(asignaciones, fecha_actual)  # Paso 6: Proxima habitación en desocuparse
    mostrar_huespedes_por_dias(asignaciones)  # Paso 7: Mostrar huespedes por dias

if __name__ == "__main__":
    main()

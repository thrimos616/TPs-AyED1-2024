def tarifaViajes(viajes):
    viajes = 0
    precioBase = 650
    if viajes > 1:
        if viajes <= 20:
            print(f"La tarifa del viaje es de {precioBase}")
        elif viajes >= 21 or viajes <= 30:
            print(f"La tarifa del viaje es de {precioBase - (precioBase * 0.2)}") 
        elif viajes >= 31 or viajes <= 40:
            print(f"La tarifa del viaje es de {precioBase - (precioBase * 0.3)}")
        elif viajes > 40:
            print(f"La tarifa del viaje es de {precioBase - (precioBase * 0.4)}")
    else:
        print("La cantidad de viajes es invalida, por favor, vuelva a intentarlo...")

# Bloque principal
viajes = input(int("Introduzca la cantidad de viajes realizados: "))
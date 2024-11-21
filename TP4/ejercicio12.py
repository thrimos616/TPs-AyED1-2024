"""
Escribir un programa para crear una lista por comprensión con los naipes de la baraja española. La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros", "2
Oros"... ]. Imprimir la lista por pantalla. 
"""

def generar_baraja():
    palos_de_cartas = ['Oros', 'Bastos', 'Espadas', 'Copas']
    return [' '.join([str(numero), palo]) for palo in palos_de_cartas for numero in range(1, 13)]

def ejecutar():
    baraja = generar_baraja()
    print("Cartas de la baraja española:")
    for carta in baraja:
        print(carta)

if __name__ == "__main__":
    ejecutar()

""" 
Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea
correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma.
"""

def solicitar_numero_positivo() -> int:
    while True:
        try:
            entrada = input("Por favor, introduzca un numero positivo: ")
            numero = int(entrada)

            if numero <= 0:
                raise ValueError("El valor debe ser un numero mayor que 0.")

            return numero

        except ValueError as e:
            print(f"Error: {e}. Por favor, intente de nuevo.")


if __name__ == "__main__":
    resultado = solicitar_numero_positivo()
    print(f"El numero proporcionado '{resultado}' es valido.")

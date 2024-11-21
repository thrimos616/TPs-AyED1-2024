"""
Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
formatos de fecha inválidos y devolver una tupla vacía
"""

def separar_correo(correo):
    try:
        if correo.count('@') != 1 or correo.count('.') < 1:
            raise ValueError("Formato de correo inválido")

        usuario, dominio_completo = correo.split('@')
        
        partes_dominio = dominio_completo.split('.')
        
        if len(partes_dominio) < 2:
            raise ValueError("Dominio o extensión invalidos")

        return (usuario, partes_dominio[0], partes_dominio[1], partes_dominio[2])

    except ValueError:
        return ()

# Bloque principal
def main():
    correo = input("Ingrese una direccion de correo electronico: ")

    resultado = separar_correo(correo)
    
    if resultado:
        print(f"Las partes del correo son: {resultado}")
    else:
        print("El formato del correo electronico es invalido.")

if __name__ == "__main__":
    main()

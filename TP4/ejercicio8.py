'''
Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
'''

def obtener_ultimos_n_caracteres(texto, cantidad):
    if cantidad < 0:  
        return ""
    
    return texto[-cantidad:]

def ejecutar() -> None:
    texto = "El número de teléfono es 3423-2132"
    cantidad = 9  

    resultado = obtener_ultimos_n_caracteres(texto, cantidad)
    
    print(f"Texto original: {texto}")
    print(f"\nUltimos {cantidad} caracteres: {resultado}")

if __name__ == "__main__":
    ejecutar()

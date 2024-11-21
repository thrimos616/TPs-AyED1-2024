"""
Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales
contiene, identificando la cantidad de cada una. Devolver un diccionario con los
resultados. Luego desarrollar un programa para leer una frase e invocar a la
función por cada palabra que contenga la misma. Imprimir las palabras y la
cantidad de vocales hallada.
"""

def contarvocales(palabra):
    vocales = 'aeiou'
    conteo_vocales = {v: 0 for v in vocales}  

    for letra in palabra.lower():
        if letra in vocales:
            conteo_vocales[letra] += 1
    
    return conteo_vocales

# Bloque principal
def main():
    frase = input("Ingrese una frase: ")
    
    palabras = frase.split()
    
    for palabra in palabras:
        resultado_vocales = contarvocales(palabra)
        print(f"Palabra: {palabra} - Cantidad de vocales: {resultado_vocales}")

if __name__ == "__main__":
    main()
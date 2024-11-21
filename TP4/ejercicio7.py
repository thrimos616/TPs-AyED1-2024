'''
Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
'''

def eliminar_con_rebanadas(texto, inicio, longitud):
    if inicio < 0:  
        inicio = 0
    if longitud < 0:  
        longitud = 0
    if inicio + longitud > len(texto):  
        longitud = len(texto) - inicio

    return texto[:inicio] + texto[inicio + longitud:]

def eliminar_sin_rebanadas(texto, inicio, longitud):
    resultado = "" 
    for i in range(len(texto)):
        if (i < inicio) or (i >= inicio + longitud):  
            resultado += texto[i]
    return resultado

texto_prueba = "El número de teléfono es 1234-4321"
inicio_subcadena = 25
longitud_subcadena = 9

print(f"Cadena después de eliminar con rebanadas: {eliminar_con_rebanadas(texto_prueba, inicio_subcadena, longitud_subcadena)}") 
print(f"Cadena después de eliminar sin rebanadas: {eliminar_sin_rebanadas(texto_prueba, inicio_subcadena, longitud_subcadena)}")  

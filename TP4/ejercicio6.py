'''
Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comportamiento
de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-7890" extraer la
subcadena que comienza en la posición 25 y tiene 9 caracteres, resultando la subcadena
"4356-7890". Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
'''

def usando_rebanadas(texto, inicio, longitud):
    if inicio < 0:
        inicio = 0  
    if longitud < 0:
        longitud = 0  
    if inicio + longitud > len(texto):
        longitud = len(texto) - inicio  
    
    return texto[inicio:inicio + longitud]

def sin_rebanadas(texto, inicio, longitud):

    resultado = "" 
    for i in range(inicio, inicio + longitud):  
        if i < len(texto):  
            resultado += texto[i]  
    return resultado

texto_prueba = "El numero de teléfono es 2284-4970"
inicio_subcadena = 25
longitud_subcadena = 9

print(f"Subcadena usando rebanadas: {usando_rebanadas(texto_prueba, inicio_subcadena, longitud_subcadena)}") 
print(f"Subcadena sin rebanadas: {sin_rebanadas(texto_prueba, inicio_subcadena, longitud_subcadena)}")  

import random as rn

#Ejercicio 1a
def cargar_lista_al_azar(lista):
    cantidad_elementos = rn.randint(10,99)
    print(f"Cantidad de elementos: {cantidad_elementos}")

    for i in range(cantidad_elementos):
        lista.append(rn.randint(1000,9999))

    return lista    

#Ejercicio 1b
def calcular_producto(lista):
    total = 0
    for numero in lista:
        if total == 0:
            total = numero
        else:
            total = total * numero
    return total

#Ejercicio 1c
def eliminar_numero(lista):
    n = int(input("Ingrese un numero: "))
    
    for numero in reversed(lista):
        if numero == n:
            lista.remove(numero)

#Ejercicio 1d
def is_capicua(lista = [50, 17,1,91, 17, 50]):
    capicua = True
    for i in range(len(lista)):
        if lista[i] != lista[-i-1]:
            capicua = False
    
    return capicua

print(is_capicua())
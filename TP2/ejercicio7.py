"""
Intercalar los elementos de una lista entre los elementos de otra. La intercalación
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden
tener distintas longitudes.
"""

def combinar_listas(lista_a, lista_b):
    longitud_minima = min(len(lista_a), len(lista_b))
    
    for i in range(longitud_minima):
        lista_a[2 * i + 1: 2 * i + 1] = [lista_b[i]]
    
    if len(lista_b) > longitud_minima:
        lista_a.extend(lista_b[longitud_minima:])

# Listas con valores de prueba
lista_a = [10, 3, 5]
lista_b = [2, 6, 8]
combinar_listas(lista_a, lista_b)
print(lista_a)

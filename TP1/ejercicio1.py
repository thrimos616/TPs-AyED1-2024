def mayor_estricto(a, b, c):
    #Recibe tres números y devuelve el mayor de estos, en caso de que se repita devuelve -1
    if a > b:
        if a > c:
            return a
        elif a < c:
            return c
    elif b > a:
        if b > c:
            return b
        elif b < c:
            return c
    elif c > a:
        if c > b:
            return c
        elif c < b:
            return b
    return -1


def valores():
    a = int(input("Ingrese el primer valor POSITIVO: "))
    b = int(input("Ingrese el segundo valor POSITIVO: "))
    c = int(input("Ingrese el tercer valor POSITIVO: "))
    mayor = mayor_estricto(a, b, c)
    if mayor != -1:
        print(f"El número mayor es {mayor}")
    else:
        print("No existe un número mayor estricto.")

valores()
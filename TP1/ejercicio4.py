def vuelto_cajero(venta, pago):
    if pago > venta:
        vuelto = venta - pago
        billete_5000 = 0
        billete_1000 = 0
        billete_500 = 0
        billete_200 = 0
        billete_100 = 0
        billete_50 = 0
        billete_10 = 0
        print(f"El vuelto que se debe dar es de {vuelto}")
        while vuelto > 0:
            if vuelto >= 5000:
                billete_5000 += 1
            elif vuelto >= 1000:
                billete_1000 += 1
            elif vuelto >= 500:
                billete_500 += 1
            elif vuelto >= 200:
                billete_200 += 1
            elif vuelto >= 100:
                billete_100 += 1
            elif vuelto >= 50:
                billete_50 += 1
            elif vuelto >= 10:
                billete_10 += 1
        
    elif pago == venta:
        print("Pago con el dinero justo, no debe dar vuelto")
    elif (venta - pago) < 10 and pago > venta:
        print("El vuelto no puede entregarse por falta de billetes con denominación adecuada")
    else:
        print("El dinero recibido es insuficiente")
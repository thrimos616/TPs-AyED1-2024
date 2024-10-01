def diadelasemana(dia, mes, anio):
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26 * mes - 2) // 10) + dia + anio2 + (anio2 // 4) + (siglo // 4 ) - 2 * siglo) % 7
    if diasem < 0:
        diasem = diasem + 7
    return diasem
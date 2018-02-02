def sumarDeValores(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma +lista[i]
    return suma


def ValorMayor(lista):
    may = lista[0]
    for i in range(1,len(lista)):
        if lista[i] >may:
            may = lista[i]
    return may


def ValorMenor(lista):
    men = lista[0]
    for i in range(1,len(lista)):
        if lista[i] <men:
            men = lista[i]
    return men


datos=[5454, 43430 , 3222 , 12222 , 6666, 545 , 2333, 21212 , 23 , 6565]
print("Total de datos : ")
print(datos)
print("El total de sumar los valores del array es : ",sumarDeValores(datos))
print(" Valor mayor del array : ",ValorMayor(datos))
print(" Valor menor del array : ",ValorMenor(datos))

"""
PARAMETROS TIPO LISTA
"""

def sumarizar(lista):
    suma=0
    for i in range(len(lista)):
        suma=suma+lista[i]
    return suma

def mayor(lista):
    may=lista[0]
    for i in range(1,len(lista)):
        if lista[i]>may:
            may=lista[i]
    return may

def menor(lista):
    men=lista[0]
    for i in range(1,len(lista)):
        if lista[i]<men:
            men=lista[i]
    return men


listaValores=[10,56,23,34,190,298]

print("Lista completa ")
print(listaValores)
print("Suma de los elementos : ",sumarizar((listaValores)))
print("El numero mayor es : ",mayor(listaValores))
print("El numero menor es : ",menor(listaValores))
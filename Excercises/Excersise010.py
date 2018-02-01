"""
Ejemplo 4

PARAMETRO ARBITRARIOS
"""

def sumar(v1,v2,*lista):
    suma=v1+v2
    for i in range(len(lista)):
        suma=suma+lista[i]
    return suma
print("Suma de dos valores")
print(sumar(1,2))
print("Suma de cuatro valores")
print(sumar(1,2,3,4))
print("Suma de diez valores")
print(sumar(1,2,3,4,5,6,7,8,9,10))
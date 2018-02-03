"""
IMPORTAR ALGUNAS FUNCIONALIDADES DE UN MODULO

para poder acceder a solo algunas funciones de un modulo utilizaremos :

FROM modulo IMPORT funcion // solo una funcion

FROM = indicacion del modulo donde buscar
IMPORT = funcion del modulo a cargar


Si queremos importar mas de una funcion se debe separar por comas cada funcion.

FROM modulo IMPORT funcion,funcion ....
"""

from math import sqrt, pow

dato=int(input("Ingrese un valor entero : "))
raiz = sqrt(dato)
cubo = pow(dato,3)
print("La raiz cuadrada es : ",raiz)
print("El cubo es : ",cubo)

"""
Tambien podemos asignarle un nombre de uso a las funciones que ocuparemos , como por ejemplo : 

from math import sqrt as raizcuadrada, pow as exponente

dato=int(input("Ingrese un valor entero : "))
raiz = raizcuadrada(dato)
cubo = exponente(dato,3)
print("La raiz cuadrada es : ",raiz)
print("El cubo es : ",cubo)
"""




"""
Ejemplo 2 RETORNO DE DATOS

retorno de datos se devuelven a la llamada de la funcion que recoge los datos
"""

def retorno_superficie(lado):
    sup=lado*lado
    return sup #con la instruccion return se retorna los datos de la funcion

va = int(input("Introduce el valor del lado del cuadrado : "))
superficie = retorno_superficie(va)
print("la superficie del cuadrado es : ",superficie)
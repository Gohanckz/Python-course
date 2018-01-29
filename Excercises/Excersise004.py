"""
Determinar la hipotenusa de un triangulo rectangulo conocidas las longitudes de sus dos catetos.
"""
import math

catetoA = int(input("Ingrese el cateto A : "))
catetoB = int(input("Ingrese el cateto B : "))

hipotenusa = math.sqrt(catetoA+catetoB)

print(hipotenusa)
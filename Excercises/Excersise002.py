"""
Desarrolle un programa que permita leer tres valores y almacenarlos en las variables A , B , C respectivamente.
El algoritmo debe imprimir cual es el mayor y cual es el menor. recuerde que los tres valores introducidos por
el teclado sean valores distintos. Presente un mensaje de alrta en caso de que se detecte la introduccion de valores
iguales
"""

A=int(input("Ingrese el primer valor : "))
B=int(input("Ingrese el segundo valor : "))
while B == A:
    B=int(input("Introduce un valor distinto : "))
C=int(input("Ingrese el tercer valor : "))
while C == A or C == B:
    C = int(input("Introduce un valor distinto : "))
print("El numero mayor es ", (max(A,B,C)))
print("El numero menor es ",(min(A,B,C)))
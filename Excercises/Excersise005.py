"""
Desarrolle un algoritmo que permita determinar el area y volumen de un cilindro dado su radio y altura
"""
import math

radio = int(input("Ingrese el radio del cilindro : "))
altura = int(input("Ingrese la altura del cilindro :"))

volumen = int(math.pi*((radio)**2)*altura)

print("El volumen del cilindro es de : ",volumen," centimetros cubicos.")
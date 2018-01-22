#Programa con bucle while
contador=1
suma=0
while contador<=10:
    valor=int(input("Ingrese un valor : "))
    suma = suma + valor
    contador=contador+1
promedio=suma/10;
print("La suma de los 10 valores es : ")
print(suma)
print("El promedio es : ")
print(promedio)
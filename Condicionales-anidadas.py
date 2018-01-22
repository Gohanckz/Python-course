#Programa que promedia 3 notas y da respuesta a cada situacion
nota1=int(input("Ingrese primera nota : "))
nota2=int(input("Ingrese segunda nota : "))
nota3=int(input("Ingrese tercera nota : "))
prom = (nota1+nota2+nota3)/3
print("Su promedio final es : "+ str(prom))
if prom>=7:
    print("felicidades, usted esta promocionado.")
else:
    if prom>4:
        print("regular.")
    else:
        print("Reprobado.")
#Comparacion de programas que determinan si se es mayor de edad utilizando condiciones if , ademas de usar
#diferentes ciclos , While y For


#UTILIZANDO CICLO FOR
print("CICLO FOR")

for i in range(1,100):
    if i<18:
        print("Es menor de edad")
    else:
        print("Es mayor de edad")


#UTILIZANDO CICLO WHILE

print("CICLO WHILE")

i=1
while i < 100:
    if i<18:
        print("Es menor de edad")
    else:
        print("Es mayor de edad")

    i=i+1
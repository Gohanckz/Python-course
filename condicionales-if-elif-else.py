nota1=int(input("Ingrese primera nota : "))
nota2=int(input("Ingrese segunda nota : "))
nota3=int(input("Ingrese tercera nota : "))
media=(nota1+nota2+nota3)/3

if media == 9 or media == 10:
    print("Sobresaliente")
elif media == 5:
    print("Suficiente")
elif media == 6:
    print("Bien")
elif media == 7 or media == 8:
    print("Regular/bien")
else:
    print("Insuficiente.")
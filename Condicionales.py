#utilizamos funcion input para introducir los valores que queramos por teclado

sueldo = int(input("Introduce el sueldo : "))

#condicional if

if sueldo>3000:
    print("El usuario debe pagar un porcentaje en impuestos.")
if sueldo<=3000:
    print("El usuario esta exento de declarar renta")
if sueldo>6000 and sueldo<10000:
    print("El usuario tiene que pagar una bonificacion de 1000 euros")
if sueldo==20000 or sueldo==30000:
    print("El usuario paga un 10 porciento de su sueldo")
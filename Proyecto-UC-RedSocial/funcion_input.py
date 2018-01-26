#Input nos permite recibir un dato desde el teclado , a contiuacion se mostrara algunos ejemplos

nombre = input("Digite su nombre : ")
nacimiento = int(input("¿En que ano nacio  ? "))
anoActual = int(input("Ingrese el ano actual , ejemplo : 1990 "))
print("Usted tiene  : ",(anoActual-nacimiento), " anos. ")

#para poder calcular con los datos ingresados debemos convertirlos , en este caso los convertimos a enteros 'int'
#esto se hace debido a que los input siempre nos devuelven un string.
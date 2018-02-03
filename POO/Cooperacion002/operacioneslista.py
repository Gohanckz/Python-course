def cargar_datos():
    lista=[]
    for i in range(5):
        valor=int(input("Ingrese valor : "))
        lista.append(valor)
    return lista

def verificar_mayot(lista):
    may=lista[0]
    for i in range(1,len(lista)):
        if lista[i]>may:
            may=lista[i]
    print("Mayor de la lista es : ",may)

def verificar_suma(lista):
    suma=0
    for elemento in lista:
        suma=suma+elemento
    print("Suma de todos sus elementos es  : ",suma)

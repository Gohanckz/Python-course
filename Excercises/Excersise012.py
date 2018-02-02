"""
RETORNO DE LISTA
"""

def cargar_lista():
    li=[]
    for i in range(5):
        valor=int(input("Introduce valor : "))
        li.append(valor)
    return li


def imprimir_mayor(li):
    print("Valores de la lista mayores a 10 : ")
    for i in range(len(li)):
        if li[i]>10:
            print(li[i])
        else:
         print(" NO HAY VALORES MAYORES A 10")
            #CORREGIR BUG DE REPETICION...

lista=cargar_lista()
imprimir_mayor(lista)
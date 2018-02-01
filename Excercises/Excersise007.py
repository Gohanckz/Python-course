def mostrar_mensaje(mensaje):
    #funciones con parametros simple
    print("******************************")
    print(mensaje)
    print("******************************")

def cargar_suma():
    valor1=int(input("Ingresa el primer valor : "))
    valor2=int(input("Ingresa el segundo valor : "))
    suma=valor1+valor2
    print("la suma es : ",suma)
mostrar_mensaje("calculo de suma de dos valores")
cargar_suma()

def presentacion():
    print("Programa para hacer operaciones aritméticas de suma y resta de dos valores.")
    print("*******************************")

def introducirDatos():
    global valor1
    global valor2
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))

def suma():
    suma= valor1 + valor2
    print("La suma de los dos valores es:",suma)

def resta():
    resta=valor1-valor2
    print("La resta de los dos valores es:",resta)

def finalizacion():
    print("*******************************")
    print("Gracias por utilizar este programa")


# programa principal

presentacion()
introducirDatos()
suma()
resta()
finalizacion()
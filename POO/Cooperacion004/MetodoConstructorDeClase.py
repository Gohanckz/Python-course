"""
def __init__(self): es la definicion de una funcion, al igual que cualquier otra

__init__ , python lo reserva para los métodos constructores

-un metodo constructor de una clase, es una funcion que se ejecuta automaticamente
cuando crea un objeto

-
"""

#creamos una clase , en este caso se llama usuario

class Usuario:

    #declaramos nuestro metodo constructor por defecto

    def __init__(self):
        self.usuario=""
        self.ingresos=0
    #declaramos los metodos

    def intro(self):
        self.usuario=input("Ingrese el nombre del usuario : ")
        self.ingresos=float(input("Cantidad de ingresos anual : "))

    def visualizar(self):
        print("Nombre : ", self.usuario)
        print("Ingresos : ",self.ingresos)

    def fiscalidad(self):
        if self.ingresos>3000:
            print("Debe pagar inpuestos")
        else:
            print("No paga inpuestos")


    #BLOQUE PRINCIPAL

usuario=Usuario()
usuario.intro()
usuario.visualizar()
usuario.fiscalidad()

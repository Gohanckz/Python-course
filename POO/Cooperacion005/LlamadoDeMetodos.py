#definimos la clase , en este caso se llamara Operacion

class Operacion:

    #definimos el metodo constructor

    def __init__(self):
        self.valor1=0
        self.valor2=0

    def sumar(self):
        suma=self.valor1+self.valor2
        print("La suma es : ",suma)

    def restar(self):
        resta=self.valor1-self.valor2
        print("La resta es : ",resta)

    def multiplicar(self):
        multi=self.valor1*self.valor2
        print("La multiplicacion es : ",multi)

    def dividir(self):
        div=self.valor1/self.valor2
        print("La division es : ",div)

    def intro_valores(self):
        self.valor1=int(input("Introduce el primer valor : "))
        self.valor2=int(input("Introduce el segundo valor : "))

    def main(self):
        self.sumar()
        self.restar()
        self.dividir()
        self.multiplicar()


#BLOQUE PRINCIPAL

#creamos el objeto

resultado=Operacion()

#llamamos utilizando el objeto
resultado.intro_valores()
resultado.main()
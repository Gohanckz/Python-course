lista =[] #Declaramos la lista vacía.
for k in range(10):
    lista.append(input("Introduce valor en lista : ")) #anadimos los valores de la lista por teclado

print("Los elementos de la lista son : " + str(lista)) # visualizamos los elementos de la lista
valor = int(input("Introduce el valor a modificar de la lista pon el indice : ")) #indice a modificar
nuevo = input("Introduce el nuevo valor : ") #Valor de nuevo indice que se modificara
lista[valor] = nuevo # hacemos la modificacion
print("Los elementos de la lista son : " + str(lista)) # visualizamos la lista para comprobar la modificacion
valor = int(input("Introduce el indice en que se se insertara el nuevo valor : ")) # indice en donde se insertara el nuevo valor
nuevo = input("introduce el nuevo valor : ") #valor a insertar
lista.insert(valor,nuevo)
print("Los elementos de la lista son : " + str(lista)) #visualizamos los elementos para comprobar la modificacion
nuevo = input("Introduce el valor a eliminar : ") #valor a eliminar
lista.remove(nuevo) #eliminamos el valor
print("Los elementos de la lista son : " + str(lista)) #visualizamos la lista
nuevo = input("Introduce el valor a buscar : ")
resultado = (nuevo in lista)
if (resultado):
    print("existe este elemento y su indice es : " + str(lista.index(nuevo)))
else:
    print("No existe el elemento")

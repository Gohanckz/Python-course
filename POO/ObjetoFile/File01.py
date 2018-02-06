#abrimos el archivo utilizando open , asignamos el nombre del archivo , y ponemos
#el metodo de apertura "w+"
archivo = open("archivo.txt", "w+")

#almacenamos la lectura del archivo
contenido = archivo.read()
#calculamos el final del archivo
final_de_archivo = archivo.tell()

#escribimos en el archivo
archivo.write('Nueva linea')

#con seek movemos el puntero al bite indicado (final del archivo)
archivo.seek(final_de_archivo)
#almacenamos el nuevo contenido en el archivo
nuevo_contenido = archivo.read()


#finalmente cerramos el archivo
archivo.close()

#visualizamos el contenido
print(nuevo_contenido)
# EL PROGRAMA SE CREA EN DONDE SE ENCUENTRA ESTE PROGRAMA.
archivo = open("archivo.txt", "w+")
selection = input('introduce el texto para el archivo:')
contenido = archivo.read()
final_de_archivo = archivo.tell()

archivo.write(selection)
archivo.seek(final_de_archivo)
nuevo_contenido = archivo.read()

archivo.close()

print(nuevo_contenido)
# EL UNICO CAMBIO ES QUE EN ESTE ARCHIVO LO QUE SE AGREGARÁ SE INTRODUCIRA POR TECLADO


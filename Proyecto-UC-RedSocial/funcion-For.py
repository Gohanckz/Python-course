#Realiza un programa que convierte temperaturas C° a F°
#Realziarlo utilizando un ciclo FOR

print("F°   C°")
for temp in range(21):
    print(temp,"    ",int((temp-32)*5/9))


"""
    Se puede utilizar la funcion range de diferentes formas.
    
    por ejemplo: range(5,10) -> comenzará desde 5 hasta llegar a 9 (10-1 = 9)

    sin embargo, tambien podemos asignar el aumento que queramos que posea 
    
    por ejemplo: range(5,10,2) -> comenzará desde 5 hasta llegar a 9 pero el aumento es de 2 en 2
"""
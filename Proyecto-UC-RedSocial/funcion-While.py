#Crear un programa que permita obtener las temperaturas en grados celcius y su conbercion a frenheit
#utilizando un ciclo while

temp = 32
print("F°   C°")
while temp < 73:
    print(temp,"    ",int((temp-32)*5/9))
    temp = temp +1

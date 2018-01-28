#Podemos ver si un numero es apr utulizando booleanos junto con una funcion como en el siguiente ejemplo:

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print((es_par(8)))
print((es_par(7)))

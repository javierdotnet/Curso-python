"""

    Funciones VS Generador 

    Generador es una estructura que almacena objetos iterables
    Los valores se almacenan de uno en uno

    Cuando almacenamos un valor este se queda en "suspension de estado"

"""


def num_pares_generador(cantidad):
    num = 1

    while num < cantidad:
        yield num * 2
        num += 1

resultado = num_pares_generador(10)

for i in resultado:
    print(i)


def numeros_pares(cantidad):
    num = 1
    numList = []
    while num < cantidad:
        numList.append(num * 2) 
        num += 1
    return numList

print(numeros_pares(10))
print('*' * 40)


# Generador Yield from 
def devuelve_ciudades(*ciudades):
    # * numero de parametros indefinido
    for elemento in ciudades:
        # yield elemento
        # for subElemento in elemento:
        #    yield subElemento
        yield from elemento

ciudades_devueltas = devuelve_ciudades('Llucmajor', 'Inca', 'Manacor', 'Palma')
print(next(ciudades_devueltas))

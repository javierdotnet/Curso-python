'''
El juego del DADO 20
El usuario tiene que descubir que numero ha salido al tirar el dado de 20 caras
Y se le van a dar pistas si el numero es mayor o menor 
'''

import random
import os
from subprocess import call


def generaNumero():
    return random.randint(1,20)

def consultaNumero(numero):
    pass

def main():
    intentos=1
    numero = generaNumero()
    print(numero)
    while True:
        pregunta = int(input('Introduce un numero '))
        if ( pregunta==numero ):
            #os.system('clear')
            call('clear')
            print(f'Acertaste !!!! . El número es {numero} y lo has intentado {intentos} veces ')
            break
        else:
            if pregunta > numero :
                print(' Error el numero es menor')
                intentos+=1
            else:
                print('Error el numero es mayor')
                intentos+=1
    


if __name__ == "__main__":
    main()
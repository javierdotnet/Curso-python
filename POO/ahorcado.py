'''
    El juego del ahorcado
'''

#Imports
import os
import random

# ACSII ART
IMAGENES = ['''

    +---+
    |   |
        |
        |
        |
        |
        ==========''','''

    +---+
    |   |
    O   |
        |
        |
        |
        ==========''','''

    +---+
    |   |
    O   |
    |   |
        |
        |
        ==========''','''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        ==========''','''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        ==========''','''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        ==========''','''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        ==========''','''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        ==========''','''

''']


# Juego
# palabras para el juego
PALABRAS=[
    'sillas',
    'ordenador',
    'cursos',
    'desarrollador',
    'papelera'
]

# funciones 
# elegir una palabra aleatoria
def palabraAleatoria():
    lista = random.randint(0,len(PALABRAS)-1)
    print(lista)
    return PALABRAS[lista]


def tablero(esconderPalabra , intentos):
    print(IMAGENES[intentos])
    print('')
    print(esconderPalabra)
    print('----*----*----*----*----*----*----*----*')

# iniciar
def run():
    palabra = palabraAleatoria()
    esconderPalabra = ['-'] * len(palabra)
    intentos =0

    #bluce infinito
    while True:
        os.system('clear')
        tablero(esconderPalabra,intentos)
        pedirLetras = input('Adivina una letra : ')

# * Lógica
        indexarLetra=[]
        for i in range(len(palabra)):
            if ( palabra[i]==pedirLetras ):
                indexarLetra.append(i)
        if ( len(indexarLetra)==0 ):
            intentos+=1

# * Perder
            if ( intentos==7 ):
                tablero(esconderPalabra,intentos)
                print('')
                print(f'¡Perdiste! La palabra correcta es {palabra}')
                break
        else:
            for i in indexarLetra:
                esconderPalabra[i]=pedirLetras
        #Vaciar al final 
            indexarLetra=[]
        
        # Ganar
        try:
            esconderPalabra.index('-')
        except ValueError:
            print('')
            print(f'Felicidades la palabra ganadora es :{palabra}')
            break



if __name__ == "__main__":
    run()
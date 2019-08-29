'''
  Bucle FOR

'''



'''

 Bucle WHILE 

 Bucle indeterminado de iteraciones 

'''

import math

if False:
    numero = int(input('Escribe un numero'))

    while numero <0 :
        print('Error debe escribir un numero positivo')
        numero = int(input('intentalo otra vez'))

    print(f'\n su raiz cuadrada es : {(math.sqrt(numero)):.2f}')


i=0
while i<7:
    #pass para seguir programando
    print('hola mundo ' , i)
    i+=1

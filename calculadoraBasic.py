'''
    calculadora

'''

numero1= int(input('Introduce el primer numero '))

numero2= int(input('Introduce el primer numero '))

tipoOperacion=input('Qué tipo de operacion hemos de realizar (suma(1),resta(2),multiplicacion(3),division(4)) ')

if tipoOperacion=='suma' or tipoOperacion=='1':
    print('Resultado de la suma : ',numero1+numero2)
elif tipoOperacion=='resta' or tipoOperacion=='2':
    print('Resultado de la resta : ',numero1-numero2)
elif tipoOperacion=='multiplicacion' or tipoOperacion=='3':
    print('Resultado de la multiplicación : ',numero1*numero2)
elif tipoOperacion=='division' or tipoOperacion=='4':
    print('Resultado de la division :' , numero1/numero2)
else:
    print('Escribe bien por favor ')

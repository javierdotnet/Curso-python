'''
    Cajero automatico

    Saldo : 1000 € 
	Ingresar/Retirar/Mostar/Salir

'''

import sys

saldo=1000
operacionRealizar=''
#input('Operación a realizar : Ingresar(I) ,Retirar(R),Mostar(M),Salir(S)')
print('*** Menu ***')
while operacionRealizar!='S':

	operacionRealizar=input('Operación a realizar : Ingresar(I) ,Retirar(R),Mostar(M),Salir(S) :\t')
	operacionRealizar=operacionRealizar.upper()
	if operacionRealizar=='I':
		importe=int(input('Introduce el importe : '))
		saldo+=importe
	elif operacionRealizar=='R':
		importe=int(input('Importe a retirar : '))
		saldo-=importe
	elif operacionRealizar=='M':
		print('Saldo total : ' , saldo)
	elif operacionRealizar=='S':
		sys.exit('Adeu')
	






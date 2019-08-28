'''
    Variables en Python 3.7

'''

pi = 3.14159
radio = 3
area = pi * radio**2
print(area)

nombre='Javier'
apellidos='Martinez'
altura=1.84

print(' Mi nombre es ' + nombre + ' y apellidos ' + apellidos)


#Concatenar strings
print('Hola me llamo ',nombre, ' , mi apellidos es ' , apellidos, ' y mi altura es ', altura)

print("Hola me llamo {} y me apellido {} y mido {}".format(nombre,apellidos,altura))

print(f"Hola me llamo {nombre} y me apellido {apellidos} y mido {altura}")
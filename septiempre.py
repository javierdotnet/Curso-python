
'''
Convertir la primera letra a mayuscula
'''
#capitalice()
cadena='bienvenido a mi aula'
print(cadena.capitalize())

#Convertir una cadena en minusculas
print('lower',cadena.lower())

#Convertir cadena a mayusculas
print('upper',cadena.upper())

#convertir una cadena a mayusculas si está en minúsculas y viceversa
# swapcase()
print('swapcase',cadena.upper().swapcase())

#Convertir la primera letra de todas las palabras de una frase en mayusculas
print(cadena.title())

#Centrar texto en consola
print(cadena.center(50,'*'))

#Contar cuantos caracteres hay en una cadena de caracteres
print('Cuantas "a" hay ' ,cadena.count('a'))
#Busca la posicion
print('cuantas subcadenas ', cadena.find('aula'))

#Slices
#Obtener un substring
cadena='ibecon'
print(cadena[1:])

print(cadena[1:3])

print(cadena[1:5:2])
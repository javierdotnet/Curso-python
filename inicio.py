'''
    Tipos de datos que acepta python

'''

print("Hello world")

print('Hello world ')

print(""" Hello World """)

print(''' hola mundo de nuevo ''')

#print(' esto tiene comillas "xxx"')


print(type('hola mundo'))


# Enteros
print(30)
print(type(30))

#Floats ( decimales )
print(30.6)
print(type(30.6))


#Boolean 
print(True)
print(type(False))


#Listas 
[5,7,8,10,23]

print([5,7,8,10,23])

listavariada = ['Hola', 20,20.4,False]
print(type(listavariada))

#TUplas 
# Es como una lista pero los datos no pueden modificarse

tupla = (10,20,40,50)

print(type(tupla))

#Diccionarios 
diccionario=(
    {'name':'Pepe'},
    {'apellido':'Viyuela'}
    )
print(diccionario)
print(type(diccionario))

#None - Nonetype
#Tipo de dato no definido
print(type(None))


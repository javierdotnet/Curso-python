'''
CONJUNTOS

'''

#Prepara una variable para almacenar un conjunto vacio

conjuntos =set()
#Es lo mismo que lo anterior
conjuntos={}


conjuntos={1,2,3,4,5,5,'prueba',True,('lunes','martes')}

print('conjuntos :' , conjuntos)

#Agregar nuevos elementos nos lo va a insertar en un lugar desordenado
conjuntos.add('adios')

print('conjuntos :' , conjuntos)

conjuntos.remove('prueba') # Eliminar un solo elemento

#Buscar un elemento dentro de un conjunto
print('ADIOS' in conjuntos)
print('ADIOS' not in conjuntos)

# Borrar todo el contenido 
conjuntos.clear()

# Comprobar si ambos conjuntos son iguales 
conjunto01={1,2,3}
conjunto02={1,3,2,4}
print('son iguales ambos conjuntos : ' , conjunto01==conjunto02)

# Union de dos conjuntos 
union = conjunto01 | conjunto02
print('Union  :' , union)

#Interseccion de dos conjuntos .
union = conjunto01 & conjunto02
print('interseccion  :' , union)

#La diferencia _ Elementos que solo estan en el conjunto A
union = conjunto01-conjunto02
print('diferencia : ' , union)

#Diferencia simetrica . Elementos que estan en A y en B pero NO en ambos 
union = conjunto01 ^ conjunto02
print('union ' , union)

'''
  DICCIONARIO VACIO

'''

#diccionario = {}
#Diccionario    
diccionario = {
    'cama' : 'bed',
    'rojo' : 'red',
    }

print(diccionario,'\n')

#Leer por la clave 
print(diccionario['rojo'])

#Agregar nuevos elementos
diccionario['rojo']='RED'
#Eliminar elemento
del(diccionario['rojo'])

print('diccionario')
print(diccionario,'\n')

agenda01 ={
    'Pepe': [33,1.70] ,
    'Maria':[40 , 1.80] ,
    'Juan':[11,1.20]
}

print(agenda01)

equipoNBA={
    '23':'Michael Jorda',
    '00' : 'Robert Parish',
    '33' : 'Larry Bird' ,
    '21' : 'Dominique Wilkins'
}

print(equipoNBA['00']);

#Sino sabes 
print(equipoNBA.get('99'))

#Busqueda directa
print('33' in equipoNBA)

#Mostrar las keys
print(equipoNBA.keys())

#Mostrar sus valores
print(equipoNBA.values())

#Mostrar llave-valor
print(equipoNBA.items())

#Limpiar contenido
equipoNBA.clear()
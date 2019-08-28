'''
    LISTAS
'''

grupo=['lunes','martes','miercoles','jueves','viernes','sabado','domingo',['sabado','lunes',10,True]]

print('lista ' , grupo ,'\n')

grupo*=3

print('lista *3 ',grupo ,'\n')

print(grupo[2:5],'\n')

n=1
print(grupo[n:n+5],'\n')

print(len(grupo) , '\n')

# AGregar elementos al fnal de la lista
grupo.append('FINAL')
print(grupo,'\n')

#Agregar elementos entre partes de una lista
grupo.insert(2,'CENTRO')
print(grupo,'\n')

#Agregar varios elementos al final 
grupo.extend([30,40,50])
print(grupo,'\n')

#Concatenar listas

otroGrupo=['Tierra','Marte','Jupiter','Mercurio','Kepler','Orion','Ganimedes','Raticulin']
grupo+=otroGrupo;
print(grupo)

#Saber si un valor está dentro de una lista
print('Tierra pertenece a otro grupo','Tierra' in otroGrupo)

#Saber en que indice está un elemento
print('Posicion encontrada : ' , otroGrupo.index('Jupiter'));

#Contar cuantas veces se repite un elemento 
print('sabado esta contenido ' , grupo.count('sabado'))

#Elemento el ultimo elemento de la lista
otroGrupo.pop()
print(otroGrupo)

#Elemento el  elemento de la posicion de una lista
otroGrupo.pop(2)
print(otroGrupo)

#Eliminar un elemento exacto de la lista
otroGrupo.remove('Tierra')
print(otroGrupo)

#Voltear una lista
otroGrupo.reverse()
print(otroGrupo)

#Ordenar una lista
otroGrupo.sort()
otroGrupo.sort(reverse=True)
print(otroGrupo)

# Esto da error
#grupo.sort()
#print(grupo)

#Borra grupo
otroGrupo.clear()
print('otroGrupo ' , otroGrupo)

#Cambiar contenido de un elemento
print('grupo[4]',grupo[4])


'''
   Tuplas
    son mas rapidas en ejecución que las listas
'''

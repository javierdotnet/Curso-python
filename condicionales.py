'''
    Indentación

'''
if (False):
    if 10>0 :
        print('esto es un if')
        print('sigo dentro del if')
    print('No estoy dentro del if')

if (False):
    if 10>100:
        print('esto es un if')
    elif 0==0:
        print('0==0')
    else:
        print('esto es un else')

# if anidados 

if (False):
    edad = int(input('cual es tu edad?'))
    if edad>=0 and edad<120 :
        print('Edad correcta')
        if edad>=18:
            print('Es mayor de edad')
        if edad<18:
            print('Es menor de edad')
    else:
        print('Se ha equivocado introduciendo su edad , vuelva a intentarlo')


'''
    Ejercicio de edades
    Tres personas su edad .
    Qué persona es la mayor porque queremos ponerlo al madno de un grupo de trabajo
'''

if (False):
    lista=[]
    personas=[]
    edades=[]
    for i in [1,2,3]:
        nombre = input('Dime tu nombre : ')
        edad=int(input('Dime tu edad : '))
        personas+=[nombre]
        edades+=[edad]

    print(personas)
    print(edades)

    edadMaxima=0
    posicionEdadMaxima=0
    for i in personas:
        print(i)
    for i in edades:
        if i>edadMaxima:
            edadMaxima=i
            
            posicionEdadMaxima=edades.index(i)
            print(posicionEdadMaxima)


    print('El que tiene mas edad es ' , personas[posicionEdadMaxima])


'''
   xxxx
'''

if (False):
    caracter=input('Insertar una letra : ').lower()

    if caracter=='a' or caracter=='e' or caracter=='i' or caracter=='o' or caracter=='u':
        print('Es una vocal')
    else:
        print('No es una vocal')
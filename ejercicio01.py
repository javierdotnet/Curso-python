import math


#Ecuación de Pitágoras
# a**2 + b**2 = c**2

a= float(input('valor de a : '))
b = float(input('valor de b : '))
#c= float(input('valor de c :'))

a=a**2
b=b**2
#c=c**2

#formula = a + b + c

c=(a+b)**0.5


print(f"Resultado :" ,c)


#Calcular el área y longitud de un círculo 
# Área = pi * r**2
# longitud = 2*pi * r


radio = float(input('Dime el radio : ' ))

area = ( math.pi * radio**2 )

print(f'El área es {area:.2f}')

longitud = 2*math.pi*radio
print(f'La longitud  es {longitud:.2f}')



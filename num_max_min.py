def num_max_min(param1 , param2 , param3 ):
    menor =0
    mayor =0


    if ( param1==param2 ) or ( param1==param3):
        pass

    if (param1<param2) and (param1<param3):
        menor=param1
    elif ( param2<param1) and ( param2<param3) :
        menor = param2
    elif ( param3<param1) and ( param3<param2):
        menor = param3
    
    if (param1>param2) and (param1>param3):
        mayor=param1
    elif ( param2>param1) and ( param2>param3) :
        mayor = param2
    elif ( param3>param1) and ( param3>param2):
        mayor = param3

    return menor,mayor


def main():
    numero1=int(input('Introduce el primer numero '))
    numero2=int(input('Introduce el segundo numero '))
    numero3=int(input('Introduce el tercer numero '))
    lista = num_max_min(numero1,numero2,numero3)
    if lista[0]==0 and lista[0]==0:
        print('Son iguales')
    else:
        print('El menor es ', lista[0] , ' y el mayor es ' , lista[1])

if __name__ == "__main__":
    main()

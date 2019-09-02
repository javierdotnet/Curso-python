def num_max(param1 , param2 , param3):
    if ( param1<param2 ) and ( param1<param3 ):
        return param1
    elif ( param2<param1 ) and ( param2<param3) :
        return param2
    elif ( param3<param1 ) and ( param3<param2 ):
        return param3
    else:
        return 'Ninguno . Son iguales'



def main():
    numero1 = int(input('Introduce primer numero '))
    numero2 = int(input('Introduce segundo numero '))
    numero3 = int(input('Introduce tercer numero '))
    print('El menor numero es ',num_max(numero1, numero2,numero3 ))


if __name__ == "__main__":
    main()
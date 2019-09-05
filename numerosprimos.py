'''
Números primos . son números que se pueden dividir entre uno y uno mismo
'''


def compruebaNumero(numero):
    esPrimo = True
    if numero<2:
       esPrimo=False
    elif numero==2:
        esPrimo=True
    elif numero > 2 and numero %2 ==0:
        esPrimo=False
    else:
        for i in range(3,numero):
            if numero % i ==0:
                esPrimo=True

    return esPrimo



def main():
    print('paso por main')
    numero = int(input('Introduce un número para comprobar si es primo '))
    print(compruebaNumero(numero))



if __name__ == "__main__":
    main()
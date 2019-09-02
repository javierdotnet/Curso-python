def es_mayuscula(param1 ):
    return param1.isupper()

def es_vocal(param1):
    #print(param1.upper())
    param1=param1.upper()
    if param1=='A' or param1=='E' or param1=='I' or param1=='O' or param1=='U':
        return True
    else:
        return False
    

def main():
    letra1=input('Introduce una letra : ')
    if es_vocal(letra1)==False:
        print('no es una vocal')
    else:

        if ( es_mayuscula(letra1) is True ):
            print('La letra es mayusculas')
        else:
            print('La letra es minuscula')


if __name__ == "__main__":
    main()
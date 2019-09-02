def menorque(param1,param2):
    if param1<param2 :
        return param1
    elif param2<param1 :
        return param2
    else:
        return 'ninguno. Son iguales'

def main():
    numero1=float(input('Introduce un numero : '))
    numero2=float(input('Introduce otro numero : '))
    print('El menor de los numeros es ' , menorque(numero1,numero2))

if __name__ == "__main__":
    main()
    


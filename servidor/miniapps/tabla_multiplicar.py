"""
    Tabla de multiplicar
    El usuario nos inserta un número entero y le printamos la tabla 
    de multiplicar de ese número

"""
# from imc import 
import entorno


def numero_a_multiplicar():
    numero = int(input('Introduce un número : '))
    for x in range(1, 11):
        print('Número', numero, ' * ', x, ' = ', numero*x)


def main():
    entorno.diseny('Tabla de multiplicar')
    numero_a_multiplicar()


if __name__ == "__main__":
    main()
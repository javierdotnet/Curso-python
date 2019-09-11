"""
Excepciones

"""


def opinarEdad(edad):
    if edad < 0:
        raise NameError('No se permiten edades negativas')

    if edad < 20:
        return 'eres muy joven'
    elif edad < 40:
        return 'eres joven'
    elif edad < 70:
        return 'eres maduro'
    elif edad < 120:
        return ' Cuidate '


def dividir(numero1, numero2):
    try:
        return numero1/numero2
    except ZeroDivisionError:
        print('No se puede dividir entre 0 ')
        return 'Operación no valida'


def main():
    divisor01 = float(input('Primer número : '))
    divisor02 = float(input('Segundo número : '))

    print(dividir(divisor01, divisor02))
    print('xxx')


if __name__ == "__main__":
    main():
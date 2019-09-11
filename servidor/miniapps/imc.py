"""
App que pida el peso en kilogramos y la altura en metros de una persona .
El imc se cualcula con la formula imc=peso/altura


<18,5	Peso insuficiente
18,5 - 24,9	 Normopeso
25-26,9	Sobrepeso grado I
27-29,9	Sobrepeso grado II (preobesidad)
30-34,9	Obesidad de tipo I
35-39,9	Obesidad de tipo II
40-49,9	Obesidad de tipo III (mórbida)
>50	Obesidad de tipo IV (extrema)

"""
import time
import entorno


def main():
    peso = float(input("Dime tu peso :"))
    altura = float(input("Dime tu altura : "))
    time.sleep(1)
    imc = calcula_imc(peso, altura)
    print('Tu indice de masa corporal es :', imc)
    print(analiza_resulta(imc))


def analiza_resulta(imc):
    result = ''
    if imc < 18.5:
        result = 'Peso insuficiente'
    elif imc >= 18.5 and imc <= 24.9:
        result = 'Peso normal'
    elif imc >= 25 and imc <= 26.9:
        result = 'Sobrepeso grado I'
    elif imc >= 27 and imc <= 29.9:
        result = 'Sobrepeso grado II (preobesidad)'
    elif imc >= 35 and imc <= 39.9:
        result = 'Obesidad de tipo I'

    return result


def calcula_imc(peso, altura):
    imc = peso/altura**2
    return imc


if __name__ == "__main__":
    entorno.diseny('CÁLCULO DEL ÍNDICE DE MASA CORPORAL (IMC)')
    main()
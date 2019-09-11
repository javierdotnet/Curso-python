"""
    FORMATEAR NÚMERO DE TELÉFONO 
    Hemos de pasarle el usuario y el pais

    666111222
    (+34)666-111-222
    (+34)666 111 222
"""


def formatea(numero, pais):
    my_string = "({}){}-{}-{} "
    my_string2 = "({}){} {} {}"
    # my_string.format("GeeksforGeeks", "computer", "geeks")
    pais = pais.lower()
    if pais == 'españa':
        codigopais = '+34'
    elif pais == 'francia':
        codigopais = '+33'
    elif pais == 'china':
        codigopais = '+87'
    num0 = codigopais
    num1 = numero[0:3]
    num2 = numero[3:6]
    num3 = numero[6:9]

    resultado_final1 = my_string.format(num0, num1, num2, num3) 
    resultado_final2 = my_string2.format(num0, num1, num2, num3)

    resultado = resultado_final1 + resultado_final2
    return resultado


def main():
    nombre = input('Dime tu nombre : ')
    pais = input('Dime tu pais : ')
    telefono = input('Dime tu telefono : ')
    print(formatea(telefono, pais))


if __name__ == "__main__":
    main()

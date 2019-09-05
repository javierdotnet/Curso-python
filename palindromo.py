import os

#funciones

def palindromo(palabra):
    os.system('clear')
    palabraInvertida=palabra[::-1]

    if palabraInvertida==palabra :
        return True
    else :
        return False

def main():
    while True:
        palabra = input('Escribe tu palabra favorita : ')

        if palabra=='exit':
            break

        resultado = palindromo(palabra)
        if resultado == True:
            print(f'Tu {palabra} es un palíndromo ')
        else:
            print(f' No es un palíndromo tu palabra : {palabra}')


if __name__ == "__main__":
    main()
import os

from colorama import Fore, Style, Back


class Pantalla:
    titulo = ''
    texto = ''

    def pintaPantalla(self):
        print(f"""{Fore.RED}
                {Back.BLACK}Bienvenido a la AGENDA 
                {Back.RESET}{Fore.RESET}
                [a]ñadir contacto
                [b]uscar contacto
                [e]ditar contacto
                [B]orrar contacto
                [v]er todos contactos
                [s]alir

        """)
        print(Back.RESET + Fore.RESET)

    def preguntaOpciones(self):
        opcion = input('Introduce una opción : ')
        return opcion

    def borrarPantalla(self):
        os.system('clear')

    def __init__(self):
        print('inicio')

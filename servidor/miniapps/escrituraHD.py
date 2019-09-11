"""
    Python escritura en disco

    Puede leer y escribir archivo con la funcion (open)
    Los archivos pueden ser de texto o binarios 

    Manejadores :
    * r = read
    * w = write
    * a = append
    * r+ = lee y escribe

    Se deben cerrar los archivos con el método (close)
"""

archivo = '/Users/javier/file.txt'

def main():
    nombre = input('Tu nombre : ')
    archivo = '/Users/javier/file.txt'
    with open(archivo, 'w') as f:
        for i in range(5):
            f.write(f'{nombre}\n')
        f.close()
    f = open(archivo, 'a')
    f.write('ULTIMO')
    f.close()


def lectura():
    with open(archivo, 'r') as f:
        for linea in f:
            print(linea)
        f.close()

if __name__ == "__main__":
    main()
    lectura()

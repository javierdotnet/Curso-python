'''
    primer caracter no se repite

'''
from subprocess import call

debug=True
 
def main():
    call('clear')
    texto = input('Introduce un texto a comprobar ')
    caracterAnterior = ''
    for char in texto:
        if debug==True :print(char) 
        if char!=caracterAnterior and len(caracterAnterior)>0 :
            print('Texto diferente detectado :',char)
            break
        else:
            caracterAnterior=char


if __name__ == "__main__":
    main()
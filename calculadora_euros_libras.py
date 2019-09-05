'''
Calculadora

'''

import tkinter as tk 


def convierte(importe , moneda) :
    # 1 Libra es 1.10694 €
    # 1 Euro es 0.903390 Libras 
    GBP=1.10694
    EUR=0.903390
    moneda=moneda.upper()
    if moneda=='E':
        resultado = float(importe/GBP)
    elif moneda=='L':
        resultado = float(importe/EUR)
    return resultado


def main():
    while True :
        importe=float(input('Importe :'))
        moneda = input('(E)uros , (L)ibras :')
        if importe==0 or moneda=='salir':
            break
        resultado = convierte(importe,moneda)
        print(f'El resultado de la conversión es {resultado:.2f}')


if __name__ == "__main__":
    '''
    r = tk.Tk() 
    r.title('Counting Seconds') 
    button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
    button.pack() 
    '''
    main()
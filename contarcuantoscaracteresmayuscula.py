'''
Contador de caracteres en mayusculas y minuscula

'''


def contador(param1):
    dic={'mayusculas':0,'minusculas':0}
    for c in param1:
        #print(c)
        if c.isupper():
            dic['mayusculas'] =dic['mayusculas']+1
        elif c.islower() and len(c)>0:
            dic['minusculas'] =dic['minusculas']+1
        else:
            pass
    return dic



def main():
    frase=input('Introduce una frase : ')
    lista=contador(frase)
    print('Hay un total de mayusculas', lista['mayusculas'], ' y minusculas ' , lista['minusculas'])


if __name__ == "__main__":
    main()
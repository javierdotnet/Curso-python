'''
FUNCIONES
'''
import turtle


def suma(num1,num2):
    return num1+num2




def main():
    window = turtle.Screen()
    tortuguita = turtle.Turtle()

    haz_rectangulo(tortuguita)
    window.mainloop()

def haz_rectangulo(tortuguita):
    largo = int(input('Largo : '))
    alto = int(input('Alto : '))
    for i in range(2):
        haz_linea(tortuguita,largo)
        haz_alto(tortuguita,alto)

    

def haz_linea(tortuguita,largo):
    tortuguita.forward(largo)
    tortuguita.left(90)

def haz_alto(tortuguita,alto):
    tortuguita.forward(alto)
    tortuguita.left(90)


if __name__ == "__main__":
    main()
    print(suma(2,3))
    
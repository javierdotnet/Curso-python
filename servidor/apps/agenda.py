"""

 AGENDA
 =====

 Añadir contactos ( nombre / telefono / email )
 Actualizar
 Buscar 
 Eliminar
 Listar
 Salir


 [a]ñadir contacto
            [b]uscar contacto
            [e]ditar contacto
            [B]orrar contacto
            [s]alir
        

====
  v1.0 (almacenará contenido en memoria)
  v2.0 ( escritura en disco )

"""
import os
import time
import Contacto as contact
import Pantalla as pantalla

contactos = []


def main():
    # contacto = contact.Contacto('javier', 'martinez', '1212122', 'email')
    contacto = contact.Contacto()
    contacto.nombre = 'javier'
    contacto.apellidos = 'martinez'
    print(contacto.nombre)


def crearContacto():
    nombre = input("Dime el nombre : ")
    apellidos = input("Dime los apellidos : ")
    telefono = input("Dime el telefono : ")
    email = input("Dime el email : ")
    contacto = contact.Contacto()
    contacto.nombre = nombre
    contacto.apellidos = apellidos
    contacto.email = email
    contacto.telefono = telefono
    contactos.append(contacto)


def buscarContacto():
    pass


def editarContacto():
    pass


def eliminarContacto():
    pass


def verContactos():
    for elemento in contactos:
        print('Nombre : ', elemento.nombre, ' Apellidos :', elemento.apellidos, ' Teléfono : ',elemento.telefono)


def salirAplicacion():
    pass


def run():
    screen = pantalla.Pantalla()
    screen.pintaPantalla()
    resultado = screen.preguntaOpciones()
    while resultado != 's':
        if resultado == 'a':
            crearContacto()
            resultado = ''
        elif resultado == 'b':
            buscarContacto()
            resultado = ''
        elif resultado == 'v':
            screen.borrarPantalla()
            verContactos()
            time.sleep(2)
            resultado = ''
        else:
            screen.borrarPantalla()
            screen.pintaPantalla()
            resultado = screen.preguntaOpciones()

if __name__ == "__main__":
    run()
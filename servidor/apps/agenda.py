"""

 AGENDA
 =====

 Añadir contactos ( nombre / telefono / email )
 Actualizar
 Buscar 
 Eliminar
 Listar
 Salir

====
  v1.0 (almacenará contenido en memoria)
  v2.0 ( escritura en disco )


"""

import Contacto as contact

def main():
    #contacto = contact.Contacto('javier', 'martinez', '1212122', 'email')
    contacto = contact.Contacto()
    contacto.nombre = 'javier'
    contacto.apellidos = 'martinez'
    print(contacto.nombre)


if __name__ == "__main__":
    main()
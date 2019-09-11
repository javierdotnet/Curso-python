class Contacto:
    nombre = ''
    apellidos = ''
    telefono = ''
    email = ''

    def f(self):
        print('nombre : ', nombre, ' apellidos ', apellidos, 'telefono',
              telefono)
        return 'contacto'

    def __init__(self):
        print('inicio')

    '''
    def __init__(self, nombre, apellidos, telefono, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
    '''
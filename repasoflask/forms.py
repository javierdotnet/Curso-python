from wtforms import Form, StringField, TextField, validators, HiddenField
from wtforms.fields.html5 import EmailField


# Crear una validacion propia
def honeyPot():
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')


class formularioContactar(Form):
    nombre = StringField('nombre: ', [
        validators.Required('Estas obligado a rellenar este campo'),
        validators.length(min=3, max=25, message='Nombre incorrecto')
    ])

    email = EmailField('correo electronico: ', [
        validators.Required('Estas obligado a rellenar este campo'),
        validators.Email('Correo incorrecto')
    ])

    comentario = TextField('comentarios : ')

    senyuelo = HiddenField('', [honeyPot])

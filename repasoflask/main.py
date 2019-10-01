from flask import Flask, request, make_response, redirect, render_template
from forms import formularioContactar
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    contactar = formularioContactar(request.form)
    if request.method == 'POST':
        print('nombre : {contactar.nombre.data}')
        print(contactar.email.data)
        print(contactar.comentario.data)
    # dentro de usuario ya podemos utilizar formiularios en Flask
    # return 'home'
    return render_template('contactar.html', form=contactar)


@app.route('/parametros')
@app.route('/parametros/<otraruta>')
@app.route('/parametros/<otraruta>/<int:numero>')
def param(otraruta):
    return (f'El parametro enviados es :{otraruta}')


@app.route('/usuario/<nombre>')
def param2(nombre=''):
    return render_template('usuario.html', usuario=nombre)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)

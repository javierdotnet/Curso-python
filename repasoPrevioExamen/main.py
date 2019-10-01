from flask import Flask, render_template, request, redirect, url_for
import logging
from horoscopo import HoroscopoChino  # OJO


app = Flask(__name__)


@app.route('/')
def index():
    logging.warning("See this message in Flask Debug Toolbar!")
    return render_template('index.html')


@app.route('/', methods=['POST'])
def logica():
    # recuperar desde el formulario la variable anyo
    anyo = int(request.form['anyo'])
    logging.warning('************************************')
    logging.warning(request.form['anyo'])
    logging.warning('************************************')

    persona = HoroscopoChino(anyo)

    global signo_usuario
    # llamar a nuestro metodo signo
    signo_usuario = persona.signo()

    # return render_template('signo.html')
    return redirect(url_for('signo'))


@app.route('/signo')
def signo():
    logging.warning("See this message in Flask Debug Toolbar!")
    return render_template('signo.html', signo_usuario=signo_usuario)


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
    app.debug = True
    app.secret_key = 'development key'

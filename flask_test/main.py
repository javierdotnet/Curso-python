from flask import Flask, request, make_response, redirect, render_template
app = Flask(__name__)


@app.route("/")
def home():
    ip = request.remote_addr
    respuesta = make_response(redirect('/info'))
    respuesta.set_cookie('user_ip', ip)
    # return (f'Hola mundo {ip}')
    return respuesta


@app.route('/info')
def info():
    usuario_ip = request.cookies.get('user_ip')
    context = {
        'ip': usuario_ip,
        'cosa': 'cosa'
    }
    # return (f'Ya estoy en la página INFO y la IP de tu cookie es {usuario_ip}')
    # return render_template('info.html', ip=usuario_ip)
    return render_template('info.html', **context)


@app.route('/cookie')
def cookie():
    usuario_ip = request.cookies.get('user_ip')
    return (f'Ya estoy en la página COOKIE y la IP de tu cookie es {usuario_ip}')


@app.route('/contactar')
def contactar():
    return render_template('contactar.html')


@app.route('/galeria')
def galeria():
    return render_template('galeria.html')


@app.errorhandler(404)
def error404(error):
    return '<h1>Página no encontrada...</h1>'

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
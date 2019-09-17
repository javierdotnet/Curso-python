# imports
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# instancias
app = Flask(__name__)
bootstrap = Bootstrap(app)

datos = {
    'columna01': {
        'img': 'icono01.png',
        'titulo': 'Core',
        'subitulo': 'Everythings you need ...',
        'precio': 'Free',
        'enlace': 'All core features',
        'boton': 'Included'
    },
    'columna02': {
        'img': 'icono02.png',
        'titulo': 'Adapt',
        'subitulo': 'Customize your data...',
        'precio': '99',
        'enlace': 'Rows, types ,subscriptions & digital',
        'boton': 'Add'
    },
    'columna03': {
        'img': 'icono03.png',
        'titulo': 'Localize',
        'subitulo': 'Add multiple languages,currencies and more',
        'precio': '49',
        'enlace': 'Multilangual , Multicurrency, Live Exchange rates & Locales',
        'boton': 'Removed'
    },
}
# rutas 
@app.route('/')
def home():
    return render_template('precios.html', **datos)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)


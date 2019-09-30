# imports
from flask import Flask, render_template, request

# instancias
app = Flask(__name__)


# rutas 
@app.route('/', methods=['POST', 'GET'])
def home():
    anyo = request.form['anyo']
    return render_template('index.html')

@app.route('/rata')
def rata():
    return render_template('index.html')


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)


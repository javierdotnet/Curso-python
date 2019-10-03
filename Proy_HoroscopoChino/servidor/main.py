from flask import Flask, render_template, request
app = Flask(__name__)

# rutas

@app.route("/", methods=["GET","POST"])
def home():
    # anyo = request.form["anyo"]
    return render_template("index.html")

@app.route("/rata", methods=["GET","POST"])
def rata():
    #anyo = request.form["anyo"]
    return render_template("rata.html")

@app.route("/buey", methods=["GET","POST"])
def buey():
    anyo = request.form["anyo"]
    return render_template("buey.html")

@app.route("/tigre", methods=["GET","POST"])
def tigre():
    anyo = request.form["anyo"]
    return render_template("tigre.html")

@app.route("/conejo", methods=["GET","POST"])
def conejo():
    anyo = request.form["anyo"]
    return render_template("conejo.html")

@app.route("/dragon", methods=["GET","POST"])
def dragon():
    anyo = request.form["anyo"]
    return render_template("dragon.html")

@app.route("/serpiente", methods=["GET","POST"])
def serpiente():
    anyo = request.form["anyo"]
    return render_template("serpiente.html")

@app.route("/caballo", methods=["GET","POST"])
def caballo():
    anyo = request.form["anyo"]
    return render_template("caballo.html")

@app.route("/cabra", methods=["GET","POST"])
def cabra():
    anyo = request.form["anyo"]
    return render_template("cabra.html")

@app.route("/mono", methods=["GET","POST"])
def mono():
    anyo = request.form["anyo"]
    return render_template("mono.html")

@app.route("/gallo", methods=["GET","POST"])
def gallo():
    anyo = request.form["anyo"]
    return render_template("gallo.html")

@app.route("/perro", methods=["GET","POST"])
def perro():
    anyo = request.form["anyo"]
    return render_template("perro.html")

@app.route("/cerdo", methods=["GET","POST"])
def cerdo():
    anyo = request.form["anyo"]
    return render_template("cerdo.html")




if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
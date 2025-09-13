# flask run --debug

from flask import Flask, render_template, request
from markupsafe import escape
import math

# Iniciando Flask
app = Flask(__name__)

# Rota Index
@app.route('/')
def rootRoute():
    return render_template("index.html") # Rendering HTML page

# Rota página de cálculo de equação de 2°
@app.route('/pageCalc2Grau')
def renderCalc2Grau():
    return render_template("calculo2grau.html")

# Rota página de cálculo de conversão de fahrenheit
@app.route('/pageCalcFahr')
def renderCalcFahr():
    return render_template("fahrenheit.html")

@app.route("/calc2grau", methods=["POST"])
def calc2grau():
    a = float(request.form["a"])
    b = float(request.form["b"])
    c = float(request.form["c"])

    delta = (b ** 2) - (4 * a * c)
    if delta <= 0:
        return render_template("calculo2grau.html", delta = delta) 
    
    x1 = ((b * -1) + math.sqrt(delta)) / (a * 2)
    x2 = ((b * -1) - math.sqrt(delta)) / (a * 2)
    return render_template("calculo2grau.html", x1 = x1, x2 = x2, delta = "") 

@app.route("/calc_fahrenheit", methods=["POST"])
def calcFahr():
    c = float(request.form["celsius"])
    fahr = (c * 1.8) + 32

    return render_template("fahrenheit.html", f = fahr) 
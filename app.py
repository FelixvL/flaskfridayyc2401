from flask import Flask
from flask_cors import CORS

import calculator
import hondenfeiten
import telletter
import grap

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hij doet  het YC 2401</p>"

@app.route("/calculator")
def calculatorfunc():
    return calculator.functie_een()

@app.route("/hondenfeiten")
def hondenfeitenfunc():
    return hondenfeiten.functie_een()


@app.route("/telletter")
def telletterfunc():
    return telletter.functie_een()   

@app.route("/grap")
def grapfunc():
    return grap.functie_een()             

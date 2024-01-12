from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hij doet  het YC 2401</p>"

@app.route("/calculator")
def calculator():
    input_user = int(input("vul een getal: "))
    output_user = input_user + 5
    return str(output_user)
                     

#!/usr/bin/python3.7
from route.paypal import *
from flask import Flask
from flask_cors import CORS
app = Flask(__name__,
            static_folder="./templates/static",
            template_folder="./templates")
CORS(app)

# @app.route("/")
# def home():
#     return "Hello, World!"

app.register_blueprint(paypal)

if __name__ == "__main__":
    app.run(debug=True)

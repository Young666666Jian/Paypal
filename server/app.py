#!/usr/bin/python3.7
from route.payment import *
from flask import Flask
from flask_cors import CORS
app = Flask(__name__,
            static_folder="./templates/static",
            template_folder="./templates")
CORS(app)

# @app.route("/")
# def home():
#     return "Hello, World!"

app.register_blueprint(payment)

if __name__ == "__main__":
    app.run(debug=True)

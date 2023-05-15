#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    t = text.replace("_", " ")
    return "C" + " " + t


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text="is cool"):
    return "Python" + " " + text.replace("_", " ")


@app.route('/number/<n>', strict_slashes=False)
def display_int(n):
    if type(n) is int:
        return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

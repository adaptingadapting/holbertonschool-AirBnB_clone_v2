#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from flask import render_template


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


@app.route('/number/<int:n>', strict_slashes=False)
def display_int(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def print_int_html(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def print_if_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""
creates a flask web app and sets a few returns for 2 index pages
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashing=False)

def index():
    """
    in the home page displays hello hbnb
    """
    return "Hello HBNB"

@app.route("/", strict_slashing=False)

def HBNB():
    """
    in the hbnb index page returns hbnb
    """
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""
starts a Flask web application:
Its listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashing=False)

def index():
    """ in the home page displays hello hbnb """
    
    return "Hello HBNB"

@app.route("/", strict_slashing=False)

def HBNB():
    """ in the hbnb index page returns hbnb """
    
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def show_states():
    """ displays a HTML page with the list of all State objects in the DB"""
    return render_template('9-states.html', state=storage.all(State))


@app.route("/states/<id>", strict_slashes=False)
def show_cities(id):
    """ displays a HTML page with the list of all cities of a State"""
    for st in storage.all(State).values():
        if st.id == id:
            return render_template('9-states.html', state=st)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(response_or_exc):
    """ removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

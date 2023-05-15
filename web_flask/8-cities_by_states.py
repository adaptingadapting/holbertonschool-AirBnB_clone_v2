#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slash=False)
def cities_by_states():
    """ commened function totally nicely commented """
    states_dict = storage.all(State)
    dict = {}
    for val in states_dict.values():
        dict[val] = val.cities
    return render_template('8-cities_by_states.html', dict=dict)


@app.teardown_appcontext
def close(exception):
    """Close database connection"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

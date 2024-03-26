#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of states."""
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)  # Sort states by name
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

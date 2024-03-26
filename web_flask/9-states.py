#!/usr/bin/python3
"""Starts a Flask web application."""
from flask import Flask, render_template
from models import storage, State, City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_states():
    """Display a HTML page with a list of all states."""
    states = storage.all(State)
    return render_template('9-states.html', states=states, id=None)


@app.route('/states/<id>', strict_slashes=False)
def list_cities(id):
    """Display a HTML page with the list of cities in a specific state."""
    states = storage.all(State)
    state = next((states['State.' + id] for
                  id in states if 'State.' + id in states), None)
    return render_template('9-states.html', states=states, id=id, state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

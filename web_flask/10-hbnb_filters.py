#!/usr/bin/python3
"""Starts a Flask web application."""
from flask import Flask, render_template
from models import storage, State, Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display the HTML page with filters."""
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    amenities = list(storage.all(Amenity).values())
    amenities.sort(key=lambda x: x.name)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""
Script that starts a Flask web application
"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def the_cities():
    """HTML with the cities"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close(self):
    """Close Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

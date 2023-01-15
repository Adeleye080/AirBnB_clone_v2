#!/usr/bin/python3
"""
Starts a Flask we application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db_session(exception):
    """ close storage session after each request """
    storage.close()


@app.route('/cities_by_states')
def get_states_list():
    """ renders jinja2 template with states variable. """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    storage.reload()
    app.run(host='0.0.0.0', port=5000, debug=True)

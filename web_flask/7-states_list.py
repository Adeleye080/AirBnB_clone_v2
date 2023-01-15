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
    """ runs everytime a request is made """
    storage.close()


@app.route('/states_list')
def get_states_list():
    """ passes state info to jinja2 template """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

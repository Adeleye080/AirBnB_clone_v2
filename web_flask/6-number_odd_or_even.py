#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def Home():
    """This is the Home Page"""
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>')
def C_is_fun(text):
    """displays 'C' followed by text added in route"""
    return "C {}".format(text)


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is_cool'):
    """display python followed by text, replacing '_' with space"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def is_number(n):
    """displays message if n is an integer"""
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ render html template """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """ render html template """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

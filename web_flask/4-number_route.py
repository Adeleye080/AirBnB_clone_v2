#!/usr/bin/python3
""" starts a Flask web application"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def Home():
    """ Print Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB():
    """ Print HBNB """
    return "HBNB"


@app.route('/c/<text>')
def C_is_fun(text):
    """ Print 'C ' followed by the value of text"""
    return "C {}".format(text)


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is_cool'):
    """ print web """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def is_number(n):
    """ Print integer """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

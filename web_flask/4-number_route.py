#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    '''a function to display text'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''a function to display text'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def helloc(text):
    '''this takes unput'''
    new = text.replace("_", " ")
    return "C {}".format(new)


@app.route("/python/", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hellopython(text):
    '''has defualt variables'''
    new = text.replace("_", " ")
    return "Python {}".format(new)


@app.route("/number/<int:n>", strict_slashes=False)
def numbern(n):
    '''set int variable'''
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')

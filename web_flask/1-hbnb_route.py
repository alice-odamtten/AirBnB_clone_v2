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


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')

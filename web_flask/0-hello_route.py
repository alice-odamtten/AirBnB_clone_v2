#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    '''a function to display text'''
    return "<p>Hello HBNB!</p>"


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')

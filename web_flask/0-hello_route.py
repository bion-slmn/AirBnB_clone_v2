#!/usr/bin/python3
''' This module  defines a a simple flask application'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''this view function returns Hello HBNB! when called on the
    browser, it acts like home page '''
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

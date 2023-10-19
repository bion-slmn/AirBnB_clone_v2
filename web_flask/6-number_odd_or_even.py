#!/usr/bin/python3
''' This module  defines a a simple flask application'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''this view function returns Hello HBNB! when called on the
    browser, it acts like home page '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_school():
    '''this view fuction is executed if the route is home_page/hbnb/ or
    "home_page/hbnb , the home_page is a placeholder'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def pass_variable(text):
    '''this view function is called when the route is home_page/c/variable or
    home_page/c/variable/ , home_page and variable are place holders'''
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    '''view function is called when the route is home_page/python/variable
    home_page/python/variable/ , home_page and variable are place holders'''
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''view function is called if n is a positive number'''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''function is called if n is a positive number and it displays a
    template'''
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''function is called if n is a positive number and it displays a template
    if n is odd it displays n is even or else n is odd'''
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

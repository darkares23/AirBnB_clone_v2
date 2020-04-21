#!/usr/bin/python3
"""
Init the flask aplication
"""


from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def HelloHBNB():
    """Routes display hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Sub route display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cIsFun(text):
    """Sub route display c is fun with a text"""
    return 'C %s' % escape(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text):
    """Sub route display Python is cool with a text"""
    return 'Python %s' % escape(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """Sub route display Python is cool with a text"""
    return '%s is a number' % escape(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Sub route display Python is cool with a text"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Sub route display Python is cool with a text"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

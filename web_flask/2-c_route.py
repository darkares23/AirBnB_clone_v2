#!/usr/bin/python3
"""
Init the flask aplication
"""


from flask import Flask, escape
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

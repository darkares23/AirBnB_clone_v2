#!/usr/bin/python3
"""
Init the flask aplication
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def HelloHBNB():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

#!/usr/bin/python3
"""
Init the flask aplication
"""


from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def tearDown(self):
    """handle teardpown and close the db at request end"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    """Route display a HTML page: (inside the tag BODY)"""
    states = storage.all('State').values()
    cities = storage.all('City').values()
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

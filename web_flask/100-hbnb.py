#!/usr/bin/python3
"""
Init the flask aplication
"""


from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def tearDown(self):
    """handle teardpown and close the db at request end"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def states():
    """Route display a HTML page: (inside the tag BODY)"""
    states = storage.all('State')
    users = storage.all('User')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    return render_template('100-hbnb.html',
                           states=states, users=users,
                           amenities=amenities, places=places)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

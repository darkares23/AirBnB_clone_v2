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


@app.route('/hbnb_filters', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states():
    """Route display a HTML page: (inside the tag BODY)"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

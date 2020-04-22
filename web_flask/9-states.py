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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Route display a HTML page: (inside the tag BODY)"""
    if id is not None:
        id = "State." + id
    states = storage.all('State')
    cities = storage.all('City')
    return render_template('9-states.html',
                           states=states, cities=cities, id=id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

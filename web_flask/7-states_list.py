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


@app.route('/states_list', strict_slashes=False)
def states():
    """Route to displays all states in db"""
    states_list = storage.all('State').values()
    return render_template('7-states_list.html', states_list=states_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

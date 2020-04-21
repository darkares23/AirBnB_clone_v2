#!/usr/bin/python3
"""
Init the flask aplication
"""


from flask import Flask, escape, render_template
from models import storage
app = Flask(__name__)

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.url_map.strict_slashes = False


@app.route('/states_list', strict_slashes=False)
def show_states_list():
    """Route to displays all states in db"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tearDown(error):
    """handle teardpown and close the db at request end"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

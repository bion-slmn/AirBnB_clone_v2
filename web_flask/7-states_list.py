#!/usr/bin/python3
'''this module uses flask and data bse to list
cities of a state'''
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    ''' we query the database to get the all the states in th database'''
    states = storage.all('State').values()
    sorted_states = sorted(states, key=lambda obj: obj.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    ''' closes the sessionto storage after a request'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')

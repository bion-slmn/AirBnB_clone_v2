#!/usr/bin/python3
'''this module uses flask and data bse to list
cities of a state'''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def state_list():
    ''' we query the database to get the all the states and state and cities
    associated with athat state in th database'''
    state_obj = storage.all('State').values()
    sorted_state_obj = sorted(state_obj, key=lambda obj: obj.name)
    return render_template('8-cities_by_states.html', states=sorted_state_obj)


@app.teardown_appcontext
def teardown(exception):
    ''' this method is called when the request has been completed or
    an exception has occurred to close the connection'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')

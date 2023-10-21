#!/usr/bin/python3
'''this module uses flask and data bse to list
cities of a state'''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state_list():
    ''' we query the database to get the all the states and state and cities
    associated with athat state in th database'''
    state_obj = storage.all('State').values()
    sorted_state_obj = sorted(state_obj, key=lambda obj: obj.name)
    return render_template('9-states.html', state=sorted_state_obj)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    '''displays the cities that of the state that match the id'''
    state_dict = storage.all('State')
    key = f'State.{id}'

    return render_template('9-states.html', state=state_dict, key=key)


@app.teardown_appcontext
def teardown(exception):
    ''' this method is called when the request has been completed or
    an exception has occurred to close the connection'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')

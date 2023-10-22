#!/usr/bin/python3
'''this module uses flask and data bse to list
cities of a state'''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def state_list():
    ''' we query the database to get the all the states and state and cities
    associated with athat state in th database'''
    #os.environ['HBNB_TYPE_STORAGE'] = 'db'
    state = storage.all('State').values()
    amenities = storage.all("Amenity").values()
    places = storage.all('Place').values()

    return render_template('100-hbnb.html', state=state,
                            amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exception):
    ''' this method is called when the request has been completed or
    an exception has occurred to close the connection'''
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

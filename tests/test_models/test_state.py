#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.city import City
from os import getenv
from sqlalchemy import DateTime, inspect, String
from models.base_model import BaseModel, Base
import unittest
from models import storage


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = State(name="Texas")
        self.assertEqual(type(new.name), str)

    def test_cities(self):
        '''test cities'''
        new = State()
        self.assertTrue(hasattr(new, 'cities'))

    @unittest.skipUnless(getenv('HBNB_MYSQL_DB') == 'db', 'database only')
    def test_class_atts(self):
        '''test class attributes of the clsss'''
        obj = State()

        inspector = inspect(obj)

        # get the table name
        self.assertTrue(inspector.get_table_name(), states)

        # for name
        name = inspector.columns['name']
        self.assertTrue(isinstance(name, String))
        self.assertEqual(name.type.length, 128)
        self.assertFalse(name.nullable)
        cities = inspector.columns['cities']

    @unittest.skipUnless(getenv('HBNB_MYSQL_DB') == 'db', 'database only')
    def test_cascade_delete(self):
        ''' test if it casede deete'''
        state = State(name="Texas")
        city = City(name="Austin", state_id=state.id)
        storage.new(city)
        storage.new(state)
        storage.save()
        self.assertEqual(len(storage.all()), 2)
        storage.delete(state)
        self.assertFalse(len(storage.all()))

    @unittest.skipUnless(getenv('HBNB_MYSQL_DB') == 'db', 'database only')
    def test_backref(self):
        # Create a State
        state = State(name="New York")
        storage.new(state)

        city1 = City(name="New York City", state_id=state.id)
        city2 = City(name="Albany", state_id=state.id)
        storage.new(city1)
        storage.new(city2)
        storage.save()

        # Use the backref to access the State from a City
        state_from_city1 = city1.state
        state_from_city2 = city2.state

        # Assert that both cities are associated with the same state
        self.assertEqual(state_from_city1, state_from_city2)

    @unittest.skipUnless(getenv('HBNB_MYSQL_DB') != 'db', 'database only')
    def test_cities(self):
        ''' test  cities for file storage'''
        state = State(name="New York")
        storage.new(state)

        city1 = City(name="New York City", state_id=state.id)
        city2 = City(name="Albany", state_id=state.id)
        storage.new(city1)
        storage.new(city2)
        storage.save()

        self.assertTrue(isinstance(state.cities, list))
        self.assertEqual(len(state.cities), 2)

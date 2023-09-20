#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from models.state import State
from models.city import City
from models.engine.db_storage import DBStorage
from os import getenv


class test_dbStorage(unittest.TestCase):
    """ Class to test the file storage method """

    @unittest.skipUnless(getenv('HBNB_TYPE_STORAGE') == 'db',
                         'only filestorage')
    def ytest_att(self):
        '''test attributes'''
        db = DBStorage()
        self.assertFalse(hasattr(db, engine))
        self.assertFalse(hasattr(db, _DBStorage__engine))
        self.assertTrue(isinstance(db._DBStorage__engine, engine))

    @unittest.skipUnless(getenv('HBNB_TYPE_STORAGE') == 'db',
                         'only filestorage')
    def rtest_all(self):
        ''' test all  method'''
        state = State(name="California")
        storage.new(state)

        # Create a City associated with the State
        city = City(name="Los Angeles", state_id=state.id)
        storage.new(city)
        storage.save()

        self.assertTrue(isinstance(storage.all(), dict))
        self.assertTrue(len(storage.all() == 2))
        self.assertTrue(len(storage.all(State) == 1))

    @unittest.skipUnless(getenv('HBNB_TYPE_STORAGE') == 'db',
                         'only filestorage')
    def test_new(self):
        ''' test new method  of db'''
        total = len(storage.all())
        state = State(name="California")
        storage.new(state)
        storage.save()
        self.assertTrue(total + 1 == len(storage.all()))

        # delete method
        storage.delete()
        self.assertTrue(total + 1 == len(storage.all()))
        storage.delete(state)
        self.assertTrue(total - 1 == len(storage.all()))

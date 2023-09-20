#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from models.state import State
from models.engine.file_storage import FileStorage
from os import getenv


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except as e:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
            self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        new_state = State()
        store = FileStorage()
        store.new(new)
        store.new(new_state)
        temp = store.all()
        print(temp)
        self.assertIsInstance(temp, dict)
        self.assertEqual(len(temp), 2)
        temp1 = store.all(State)
        self.assertEqual(len(temp1), 1)
        with self.assertRaises(TypeError):
            storage.all(State, BaseModel)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        for obj in storage.all().values():
            self.assertEqual(new.to_dict()['id'], obj.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
            self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)

    @unittest.skipUnless(getenv('HBNB_TYPE_STORAGE') != 'db',
                         'only filestorage')
    def test_delete(self):
        '''delete an obj  from __objects if it’s inside -
        if obj is equal to None, the method should not do anything'''
        fs = FileStorage()
        new_state = State()
        new_state.name = "California"
        fs.new(new_state)
        fs.save()
        all_states = fs.all(State)
        self.assertEqual(len(all_states.keys()), 1)
        fs.delete()
        self.assertEqual(len(all_states.keys()), 1)
        another_state = State()
        another_state.name = "Nevada"
        fs.new(another_state)
        fs.save()
        fs.delete(new_state)
        self.assertEqual(len(all_states.keys()), 1)
        # fs.delete('not_obj')
        self.assertEqual(len(all_states.keys()), 1)
        with self.assertRaises(TypeError):
            fs.delete(new_state, another_state)

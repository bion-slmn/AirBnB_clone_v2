#!/usr/bin/python3
""" """
from datetime import datetime
from sqlalchemy import DateTime, inspect, String
from models.base_model import BaseModel, Base
import unittest
from models import storage
from sqlalchemy.orm import declarative_base
import datetime
from uuid import UUID
import json
import os
from os import getenv


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except as e:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(getenv('HBNB_MYSQL_DB') != 'db', 'database only')
    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    @unittest.skipIf(getenv('HBNB_MYSQL_DB') != 'db', 'database only')
    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)
        with self.assertRaises(KeyError):
            n['_sa_instance_state']

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_Base(self):
        '''test the presence of instance Base'''
        self.assertTrue(isinstance(Base, type(declarative_base())))

        # base model doesnt inherit base
        self.assertFalse(issubclass(BaseModel, Base))

    @unittest.skipIf(getenv('HBNB_MYSQL_DB') == 'db', 'database only')
    def gtest_class_atts(self):
        '''test class attributes of the clsss'''
        obj = BaseModel()

        inspector = inspect(obj)
        # for id
        _id = inspector.columns['id']
        self.assertTrue(isinstance(_id, String))
        self.assertTrue(_id.primary_key)
        self.assertEqual(_id.type.length, 60)
        self.assertFalse(_id.nullable)

        created = inspector.columns['created_at']
        self.assertEqual(created.default, datetime.utcnow())
        self.assertTrue(isinstance(created, DateTime))
        self.assertFalse(created.nullable)

        updated = inspector.columns['created_at']
        self.assertEqual(updated.default, datetime.utcnow())
        self.assertTrue(isinstance(updated, DateTime))
        self.assertFalse(updated.nullable)

    @unittest.skipIf(getenv('HBNB_MYSQL_DB') != 'db', 'database only')
    def test_delete(self):
        ''' delete an object from the storage'''
        n = BaseModel()
        n.save()
        self.assertEqual(len(storage.all()), 1)
        n.delete()
        self.assertEqual(len(storage.all()), 0)
        with self.assertRaises(TypeError):
            n.delete(BaseModel)
